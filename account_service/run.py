from books_shared.utils import logger
from books_shared.utils.app import create_app

from servers.server import server

if __name__ == '__main__':
    logger.info("Start server ACCOUNT")
    create_app('ACCOUNT')
    server()