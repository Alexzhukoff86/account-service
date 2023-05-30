from account_service.models.account import AccountModel
from books_shared.utils.app import app
from tests.base_test import BaseTest


class TestDatabase(BaseTest):

    def test_do_not_save_account(self):
        account = AccountModel(name="John1", email="john1@example.com")
        with self.app_context():
            self.assertListEqual(account.find_all(), [])

    def test_create_account(self):
        account = AccountModel(name="John2", email="john2@example.com")
        with self.app_context():
            self.assertIsNone(AccountModel.find_by_email('john2@example.com'))
            account.save_to_db()
            self.assertIsNotNone(AccountModel.find_by_email('john2@example.com'))

    def test_get_account_by_id(self):
        account = AccountModel(name="John3", email="john3@example.com")
        with self.app_context():
            account.save_to_db()
            expected_account = AccountModel.fynd_by_id(account.id)
            self.assertEqual(expected_account.name, "John3")
            self.assertEqual(expected_account.email, "john3@example.com")
