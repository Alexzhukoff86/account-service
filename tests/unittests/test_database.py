import pytest

from account_service.models.account import AccountModel
from books_shared.utils.app import app
from tests.base_test import BaseTest


class TestDatabase(BaseTest):

    def test_do_not_save_account(self):
        account = AccountModel(name="John", email="john@example.com")
        with self.app_context():
            self.assertListEqual(account.find_all(), [])

    def test_create_account(self):
        account = AccountModel(name="John", email="john@example.com")
        with self.app_context():
            self.assertIsNone(AccountModel.find_by_email('john@example.com'))
            account.save_to_db()
            self.assertIsNotNone(AccountModel.find_by_email('john@example.com'))
            account.delete()
            self.assertIsNone(AccountModel.find_by_email('john@example.com'))

    def test_get_account_by_id(self):
        account = AccountModel(name="John", email="john@example.com")
        with self.app_context():
            account.save_to_db()
            expected_account = AccountModel.fynd_by_id(account.id)
            self.assertEqual(expected_account.name, "John")
            self.assertEqual(expected_account.email, "john@example.com")
            account.delete()

    def test_get_all_accounts(self):
        account_count = 3
        with self.app_context():
            for i in range(account_count):
                account = AccountModel(name=f"John{i}", email=f"john{i}@example.com")
                account.save_to_db()
            accounts = AccountModel.find_all()
            self.assertEqual(len(accounts), account_count)
            for account in accounts:
                account.delete()
