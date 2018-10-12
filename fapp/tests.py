from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from model_mommy import mommy
from fapp.models import BudgetModel, IncomeModel, ExpenseModel, MiniExpenseModel


class UsersTests(TestCase):
    def test_user_registration(self):
        response = self.client.post('/register/', {'username': 'testuser2', 'email': 'testuser2@gmail.com', 'password1': 'der123poi0987', 'password2': 'der123poi0987' })
        self.assertEqual(response.status_code, 302)


class BudgetsTestCase(TestCase):
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


class IncomesTestCases(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = mommy.make(User)
        self.client.force_login(self.user)
        self.budget = mommy.make(BudgetModel, user=self.user)
        budget = self.client.get(reverse('index'))
        self.budgetid = budget.context['budgets'][0].id
        self.url = reverse('view_incomes', kwargs={'budget_id': self.budgetid})
        self.incomes = mommy.make(IncomeModel, budget=self.budget, _quantity=10)
    
    def test_user_can_view_all_incomes(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(len(self.incomes), len(response.context['incomes']))

    def test_user_can_create_an_income(self):
        self.client.force_login(self.user)
        self.client.post(reverse('create_income', kwargs={'budget_id': self.budgetid}), {'name': 'income1', 'amount': 1200})
        response = self.client.get(self.url)
        self.assertEqual(11, len(response.context['incomes']))

    def test_user_can_edit_an_income(self):
        self.client.force_login(self.user)
        incomes = self.client.get(self.url)
        incomeid = incomes.context['incomes'][0].id
        self.client.post(reverse('edit_income', kwargs={'budget_id': self.budgetid, 'income_id': incomeid}), {'name': 'income2', 'amount': 2400})
        incomes = self.client.get(self.url)
        new_amount = incomes.context['incomes'][0].amount
        self.assertEqual(2400, new_amount)

    def test_user_can_delete_an_income(self):
        self.client.force_login(self.user)
        incomes = self.client.get(self.url)
        # import pdb; pdb.set_trace()
        incomeid = incomes.context['incomes'][0].id
        self.client.delete(reverse('delete_income', kwargs={'budget_id': self.budgetid, 'income_id': incomeid}))
        incomes = self.client.get(self.url)
        self.assertEqual(9, len(incomes.context['incomes']))


class ExpenseTestCases(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = mommy.make(User)
        self.client.force_login(self.user)
        self.budget = mommy.make(BudgetModel, user=self.user)
        budget = self.client.get(reverse('index'))
        self.budgetid = budget.context['budgets'][0].id
        self.url = reverse('view_expenses', kwargs={'budget_id': self.budgetid})
        self.expenses = mommy.make(ExpenseModel, budget=self.budget, _quantity=10)

    def test_user_can_view_all_expenses(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('view_expenses', kwargs={'budget_id': self.budgetid}))
        self.assertEqual(10, len(response.context['expenses']))

    def test_user_can_create_an_expense(self):
        self.client.force_login(self.user)
        self.client.post(reverse('create_expense', kwargs={'budget_id': self.budgetid}), {'name': 'name', 'amount': 2300})
        response = self.client.get(self.url)
        self.assertEqual(11, len(response.context['expenses']))

    def test_user_can_edit_an_expense(self):
        self.client.force_login(self.user)
        expenses = self.client.get(self.url)
        expenseid = expenses.context['expenses'][0].id
        self.client.post(reverse('edit_expense', kwargs={'budget_id': self.budgetid, 'expense_id': expenseid}), {'name': 'editedname', 'amount': 1200})
        edited_name = self.client.get(self.url).context['expenses'][0].name
        self.assertEqual('editedname', edited_name)

    def test_user_can_delete_an_expense(self):
        self.client.force_login(self.user)
        expenses = self.client.get(self.url)
        expenseid = expenses.context['expenses'][0].id
        self.client.post(reverse('delete_expense', kwargs={'budget_id': self.budgetid, 'expense_id': expenseid}))
        self.assertEqual(9, len(self.client.get(self.url).context['expenses']))
