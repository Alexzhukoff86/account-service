import grpc
import pytest

from books_shared.protopy.account_pb2 import *


@pytest.fixture(scope='module')
def grpc_client():
    client_channel = grpc.insecure_channel(f"[::]:50051")
    from books_shared.protopy.account_pb2_grpc import AccountServiceStub
    return AccountServiceStub(client_channel)


@pytest.fixture(autouse=True)
def cleanup(grpc_client):
    empty = google_dot_protobuf_dot_empty__pb2.Empty()
    response = grpc_client.DeleteAllAccounts(empty)


def test_create_account(grpc_client):
    request = CreateAccountRequest(name='Test Test', email='test_test@example.com')
    response = grpc_client.CreateAccount(request)
    assert response.id is not None


def test_get_account(grpc_client):
    request = CreateAccountRequest(name='Test Test', email='test_test@example.com')
    response = grpc_client.CreateAccount(request)
    request = GetAccountRequest(id=1)
    response = grpc_client.GetAccount(request)
    assert response is not None


def test_get_all_accounts(grpc_client):
    response = grpc_client.CreateAccount(CreateAccountRequest(name='Test Test', email='test_test@example.com'))
    empty = google_dot_protobuf_dot_empty__pb2.Empty()
    response = grpc_client.GetAccountList(empty)
    assert len(response.accounts) == 1
