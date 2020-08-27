from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

MAX_WAIT = 10
class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    ## helper function 01
    def wait_for_row_in_list_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('id_list_table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > MAX_WAIT:
                    raise e
                time.sleep(0.5)

    def test_can_start_a_list_and_retrieve_it_later_for_one_user(self):
        ## in unit.test we use hard url, in LSTC we use attribute
       self.browser.get(self.live_server_url)
       self.assertIn('To-Do', self.browser.title,'Failed to find To-Do')
       header_text = self.browser.find_element_by_tag_name('h1').text
       self.assertIn('To-Do',header_text)

       inputbox = self.browser.find_element_by_id('id_new_item')
       self.assertEqual(
               inputbox.get_attribute('placeholder'),
               'Enter a to-do item'
               )

       inputbox.send_keys(' Buy peacock feathers')

       inputbox.send_keys(Keys.ENTER)
       self.wait_for_row_in_list_table('1: Buy peacock feathers')

       inputbox = self.browser.find_element_by_id('id_new_item')
       inputbox.send_keys('Use peacock feathers to make a fly')
       inputbox.send_keys(Keys.ENTER)

    ## watch out for find_element and find_elements, with 's' means returning more than one.
    ## find_element raises execption if no matches found, find_elements may return []
       self.wait_for_row_in_list_table('2: Use peacock feathers to make a fly')
       self.wait_for_row_in_list_table('1: Buy peacock feathers')

       # satisfied she goes back to sleep.


    def test_multiple_users_can_start_different_lists_from_URLs(self):
        # Edith starts a new list
        self.browser.get(self.live_server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        self.wait_for_row_in_list_table('1: Buy peacock feathers')
        edith_list_url = self.browser.current_url
        #check if the string matches the url regex format
        self.assertRegex(edith_list_url,'/lists/.+')

        # Now a new user Frank visits the website
        ## start a new webpage seesion
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Fank visit the site and there is no Edith's lists
        self.browser.get(self.live_server_url)
        pagetext = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',pagetext)
        self.assertNotIn('Use peacock feathers to make a fly', pagetext)

        # Fank starts a new list by entering a new item
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy notepad')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1:Buy notepad')

        # Frank got his own url
        frank_list_url = self.browser_current_url
        self.assertRegec(frank_list_url, '/lists/.+')
        self.assertNotEqual(edith_list_url, frank_list_url)

        # Strill this page kept frank's to-do list without showing edith's
        pagetext = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers',pagetext)
        self.assertIn('But notepad', pagetext)

        # satisfied, They both went to sleep
        self.assertFail('Test is finished!')

# This is for python test to launch, django doesn't need it
#if __name__ == '__main__':
#    unittest.main(warnings='ignore')
