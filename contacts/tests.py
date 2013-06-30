"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from contacts.models import Contact

class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class ContactTests(TestCase):
	def test_str(self):
		c = Contact(first_name='Mike')
		self.assertEqual(str(c), 'Mike')

from django.test.client import RequestFactory
from contacts.views import ContactListView

class ContactListViewTests(TestCase):
	def test_no_contacts_in_context(self):
		
		factory = RequestFactory()
		request = factory.get('/')

		response = ContactListView.as_view()(request)
		self.assertEquals(
			list(response.context_data['object_list']),
			[],
		)
	def test_contacts_in_context(self):
		factory = RequestFactory()
		request = factory.get('/')
		
		c = Contact.objects.create(first_name='Mike')
		
		response = ContactListView.as_view()(request)

		self.assertEquals(
			list(response.context_data['object_list']),
			[c],
		)
	
	







