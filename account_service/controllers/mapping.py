from books_shared.utils.mapping import BaseMapping

from account_service.models.account import AccountModel
from books_shared.protopy.account_pb2 import Account


class AccountMapping(BaseMapping):

    @staticmethod
    def sql_to_proto(sql: AccountModel) -> Account:
        account = Account(id=sql.id, name=sql.name, email=sql.email)
        return account

    @staticmethod
    def proto_to_sql(proto: Account) -> AccountModel:
        account = AccountModel(name=proto.name, email=proto.email)
        return account
