from unittest import TestCase

from account_service.models.account import AccountModel
from tests.base_test import BaseTest


class TestAccountModel(TestCase):

    def test_account_model(self):
        account = AccountModel(name='John Doe', email="john.doe@example.com")
        self.assertEqual(account.name, "John Doe")
        self.assertEqual(account.email, "john.doe@example.com")

