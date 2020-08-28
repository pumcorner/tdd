from django.test import TestCase
from lists.models import Item,List

# Create your tests here.

class HomePageTest(TestCase):

        def test_uses_home_template(self):

            response = self.client.get('/')
            self.assertTemplateUsed(response,'home.html')

class ItemAndListModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()

        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'Item the second'
        ## Never forget that list needs item as column one
        second_item.list = list_
        second_item.save()

        saved_lists = List.objects.first()
        self.assertEqual(saved_lists, list_)

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(),2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.text, 'Item the second')
        self.assertEqual(second_saved_item.list, list_)

## regression test, to test view function when new url is involved
class ListViewTest(TestCase):

    def test_displays_all_lists_item(self):
        list_ = List.objects.create()
        Item.objects.create(text = 'item 1', list = list_)
        Item.objects.create(text = 'item 2', list = list_)

        response = self.client.get('/lists/the-only-one-identifier/')

        ## assertContains could recognize the bytes in response
        self.assertContains(response, 'item 1')
        self.assertContains(response, 'item 2')

    def test_use_list_view_template(self):
        response = self.client.get('/lists/the-only-one-identifier/')
        self.assertTemplateUsed(response, 'list.html')

class NewListTest(TestCase):

    def test_can_save_a_POST_request(self):

        ## This post should build a new list and create a item using data
        #(?) The salsh /new makes its a actual URL than a action URL that modifies databases
        self.client.post('/lists/new', data={'item_text': 'A new list item'})
        self.assertEqual(Item.objects.count(),1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new list item')

        ## response.content.decode() get the item_text
        ## instead of compiring with text constants we compire a html template we are using
        ## response.status.code == 302 means the webpage has been redirected
        ## response.status.code == 200 means the webpage has been rendered
    def test_redirects_atfer_POST(self):
        response = self.client.post('/lists/new',data={'item_text':'A new list item'})
        ## The following one could replace twolines
        self.assertRedirects(response, '/lists/the-only-one-identifier/')
