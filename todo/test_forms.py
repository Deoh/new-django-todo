from django.test import TestCase
from .forms import ItemForm

# Create your tests here.


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})  # instantiate a form without a name to simulate a user who submitted the form without filling it out
        self.assertFalse(form.is_valid())  # testing that the form is not valid
        self.assertIn('name', form.errors.keys())  # testing the error occurred on the name field
        self.assertEqual(form.errors['name'][0], 'This field is required.')  # testing the specific error message is what we expect 'this field is required'

    def test_the_don_field_is_not_required(self):
        form = ItemForm({'name': 'test done checkbox'})  # instantiate a form with just a name
        self.assertTrue(form.is_valid())  # testing that the form is valid

    def test_fields_are_explicit_in_form_metaclass(self):
        """test to ensure that the only fields that are displayed in
            the Itemform are the name and done fields"""
        form = ItemForm()  # instantiate an emty form
        self.assertEqual(form.Meta.fields, ['name', 'done'])  # testing the form.meta.fields attribute is equal to a list with NAME and DONE in it.
