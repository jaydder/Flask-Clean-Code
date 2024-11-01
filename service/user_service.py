from models import User
from repository import UserRepository

class UserService:
    UserRepository = UserRepository()

    def create(self, user: User):
        self.UserRepository.create(user)

    def list_all(self) -> list:
        return self.UserRepository.list_all()
