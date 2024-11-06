from models import User
from repository import UserRepository

class UserService:
    UserRepository = UserRepository()

    def create(self, user: User):
        self.UserRepository.create(user)

    def list_all(self) -> list:
        return self.UserRepository.list_all()

    def update(self, old_name: str ,user: User):
        self.UserRepository.update(old_name, user)

    def delete(self, id):
        self.UserRepository.delete(id)