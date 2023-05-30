import unittest

from account_service.controllers.mapping import AccountMapping
from account_service.models.account import AccountModel
from books_shared.protopy.account_pb2 import Account


class TestMapping(unittest.TestCase):

    def test_from_sql_to_proto_mapping(self):
        account = AccountModel(name='john', email='john@example.com')
        account_proto = AccountMapping.sql_to_proto(account)
        self.assertEqual(type(account_proto), Account)
        self.assertEqual(account_proto.name, account.name)
        self.assertEqual(account_proto.email, account.email)

    def test_from_proto_to_sql_mapping(self):
        account_proto = Account(name='john', email='john')
        account = AccountMapping.proto_to_sql(account_proto)
        self.assertEqual(type(account), AccountModel)
        self.assertEqual(account.name, account_proto.name)
        self.assertEqual(account.email, account_proto.email)