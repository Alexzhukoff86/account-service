from faker import Faker

from account_service.models.account import AccountModel
from books_shared.utils import logger

from books_shared.utils.app import app

fake = Faker()


def migrate():
    for i in range(100):
        logger.info(f"Migrate test users")
        first_name = fake.unique.first_name()
        last_name = fake.unique.last_name()
        user = AccountModel(name=f"{first_name} {last_name}",
                            email=f"{first_name.lower()}.{last_name.lower()}@example.com")
        logger.info(f"Fake user {user.name} {user.email}")
        with app.app_context():
            user.save_to_db()
