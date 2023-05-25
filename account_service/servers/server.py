from concurrent import futures

import grpc

from grpc_reflection.v1alpha import reflection


import books_shared.protopy.account_pb2 as pb
import books_shared.protopy.account_pb2_grpc as rpc
from account_service.services.account import AccountService
from books_shared.utils import logger
from books_shared.utils.config import Config


def server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_AccountServiceServicer_to_server(
        AccountService(), server
    )
    names = (
        pb.DESCRIPTOR.services_by_name['AccountService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(names, server)
    server.add_insecure_port(f"[::]:{Config.account_server_port}")
    logger.info(f"Start server on [::]:{Config.account_server_port}")
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    server()
