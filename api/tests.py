from django.test import TestCase
from fapp.models import Budget, MiniBudget

class ModelTestCase(TestCase):
    def setUp(self):
        self.name = 'My Budget'
        self.amount = 100000.0
        self.budget = Budget(name = self.name, amount = self.amount)

    def test_create_budget(self):
        old_count = Budget.objects.count()
        self.budget.save()
        new_count = Budget.objects.count()
        self.assertNotEqual(old_count, new_count)

