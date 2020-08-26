from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    #helper function 01
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        # in unit.test we use hard url, in LSTC we use attribute
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
       time.sleep(2)
       self.check_for_row_in_list_table('1: Buy peacock feathers')

       inputbox = self.browser.find_element_by_id('id_new_item')
       inputbox.send_keys('Use peacock feathers to make a fly')
       inputbox.send_keys(Keys.ENTER)
       time.sleep(2)

    # watch out for find_element and find_elements, with 's' means returning more than one.
    # find_element raises execption if no matches found, find_elements may return []
       self.check_for_row_in_list_table('1: Buy peacock feathers')
       self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

       #self.assertTrue(
               # in python 3.6+ we could use f"str"to insert local variables in curly syntax
               #any(row.text == '1: Buy peacock frather' for row in rows),f"New to-do item did not show in table. Content were \n {table.text}"
#       )

       #self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
       self.fail('Finish the test!')
# This is for python test to launch, django doesn't need it
#if __name__ == '__main__':
#    unittest.main(warnings='ignore')
        
