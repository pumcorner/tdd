from django.test import TestCase
from lists.models import Item

# Create your tests here.

class HomePageTest(TestCase):

        def test_uses_home_template(self):

            response = self.client.get('/')
            self.assertTemplateUsed(response,'home.html')

        def test_can_save_a_POST_request(self):

            response = self.client.post('/',data={'item_text':'A new list item'})

            self.assertEqual(Item.objects.count(),1)

            new_item = Item.objects.first()
            self.assertEqual(new_item.text, 'A new list item')

            # response.content.decode() get the item_text
            # instead of compiring with text constants we compire a html template we are using
            # response.status.code == 302 means the webpage has been redirected
            # response.status.code == 200 means the webpage has been rendered
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response['location'], '/lists/the-only-one-identifier/')

        def test_redirects_atfer_POST(self):
            response = self.client.post('/',data={'item_text':'A new list item'})
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response['location'], '/lists/the-only-one-identifier/')

        def test_only_save_item_when_necessary(self):

            self.client.get('/')
            self.assertEqual(Item.objects.count(),0)

class ItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'Item the second')

## regression test, to test view function when new url is involved
class ListViewTest(TestCase):

    def test_displays_all_lists_item(self):
        Item.objects.create(text = 'item 1')
        Item.objects.create(text = 'item 2')

        response = self.client.get('/lists/the-only-one-identifier/')

        ## assertContains could recognize the bytes in response
        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')

    def test_use_list_view_template(self):
        response = self.client.get('/lists/the-only-one-identifier/')
        self.assertTemplateUsed(response, 'list.html')
