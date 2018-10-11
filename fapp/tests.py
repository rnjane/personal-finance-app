from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from model_mommy import mommy
from fapp.models import BudgetModel


class UsersTests(TestCase):
    def test_user_registration(self):
        response = self.client.post('/register/', {'username': 'testuser2', 'email': 'testuser2@gmail.com', 'password1': 'der123poi0987', 'password2': 'der123poi0987' })
        self.assertEqual(response.status_code, 302)


class BudgetsViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('index')
        self.user = mommy.make(User)
        self.budgets = mommy.make(BudgetModel, user=self.user ,_quantity=10)

    def test_view_all_budgets(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(len(self.budgets), len(response.context['budgets']))

    def test_budget_list_displays_users_budgets_only(self):
        user2 = mommy.make(User)
        mommy.make(BudgetModel, user=user2)
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(len(self.budgets), len(response.context['budgets']))

    def test_user_create_a_budget_succesful(self):
        user3 = mommy.make(User)
        self.client.force_login(user3)
        self.client.post('/create-budget/', {'user': user3, 'name': 'testb'})
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['budgets']), 1)

    def test_user_delete_a_budget_succesful(self):
        user4 = mommy.make(User)
        self.client.force_login(user4)
        mommy.make(BudgetModel, user=user4, _quantity=2)
        budgets = self.client.get(self.url)
        budgetid = budgets.context['budgets'][0].id
        self.client.delete(reverse('delete_budget', kwargs={'budget_id': budgetid}))
        response = self.client.get(self.url)
        self.assertEqual(len(response.context['budgets']), 1)

    def test_user_can_edit_a_budget(self):
        self.client.force_login(self.user)
        budgets = self.client.get(self.url)
        budgetid = budgets.context['budgets'][0].id
        self.client.post(reverse('edit_budget', kwargs={'budget_id': budgetid}), {'name': 'newname'})
        budgets = self.client.get(self.url)
        new_name = budgets.context['budgets'][0].name
        self.assertEqual(new_name, 'newname')
