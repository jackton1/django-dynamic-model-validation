from django.apps import apps
from django.contrib.auth import get_user_model
from django.db import models
from django.test import TestCase

# Create your tests here.


class ModelFieldValidationTestCase(TestCase):

    @classmethod
    def get_model(cls, app_label, model_name, attrs):
        model = apps.get_model(app_label, model_name)
        attrs['__module__'] =  model.__module__
        return type('CustomTestModel', (model,), attrs)

    @classmethod
    def setUpTestData(cls):
        cls.super_user = get_user_model().objects.create(username='super-test-user', is_superuser=True)
        cls.user = get_user_model().objects.create(username='test-user')

    def test_conditional_required_fields_raises_exception(self):
        attrs =  {
            'CONDITIONAL_REQUIRED_TOGGLE_FIELDS': [
                (lambda instance: instance.user.is_active, ['fixed_price', 'percentage', 'amount'],),
            ],
        }
        TestModel = self.get_model('demo', 'TestModel', attrs)

        with self.assertRaises(ValueError) as e:
            TestModel.objects.create(user=self.user)

        self.assertEqual(
            e.exception.message['__all__'].message,
            u'Please provide a valid value for any of the following fields: Fixed price, Percentage, '
            u'Amount',
        )


    def test_required_fields_raises_exception(self):
        TestModel = self.get_model('demo', 'TestModel', {'REQUIRED_FIELDS': ['percentage']})

        with self.assertRaises(ValueError) as e:
            TestModel.objects.create(user=self.user)

        self.assertEqual(
            e.exception.message['percentage'].message,
            u'Please provide a value for: "percentage".'
        )


