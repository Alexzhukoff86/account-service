import grpc

import books_shared.protopy.account_pb2 as pb
import books_shared.protopy.account_pb2_grpc as rpc
from account_service.controllers.mapping import AccountMapping
from account_service.models.account import AccountModel
from books_shared.utils.app import app
from books_shared.utils import logger


class AccountService(rpc.AccountServiceServicer):

    def GetAccount(self, request, context):
        logger.info(f'Get request {request}')
        with app.app_context():
            account_sql = AccountModel.fynd_by_id(request.id)
            logger.info(f"Account sql {account_sql}")
        if not account_sql:
            context.abort(grpc.StatusCode.NOT_FOUND, "Account not found")
        return pb.GetAccountResponse(account=AccountMapping.sql_to_proto(account_sql))

    def CreateAccount(self, request, context):
        logger.info(f'Get request create account {request}')
        with app.app_context():
            if AccountModel.find_by_email(request.email):
                context.abort(grpc.StatusCode.ALREADY_EXISTS, "Account already exists")
            account_sql = AccountModel(name=request.name, email=request.email)
            account_sql.save_to_db()
            logger.info(f"Account {account_sql.id}")
        return pb.CreateAccountResponse(id=account_sql.id)
