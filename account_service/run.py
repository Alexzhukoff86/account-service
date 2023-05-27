from books_shared.utils import logger
from books_shared.utils.app import create_app

from account_service.services.migrator import migrate
from servers.server import server

if __name__ == '__main__':
    logger.info("Start server ACCOUNT")
    create_app()
    migrate()
    server()