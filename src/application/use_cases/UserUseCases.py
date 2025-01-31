from src.adapters.Repositories.UserRepository import UserRepository
from src.domain.Entities.User import User


class UserUseCases:

    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_user(self, user_id):
        return self.repository.get_by_id(user_id)

    def create_user(self, user: User):
        return self.repository.create(user)

    def update_user(self, user: User):
        return self.repository.update(user)

    def delete_user(self, user: User):
        return self.repository.delete(user.id)

    def activate_user(self, user: User):
        return self.repository.activate(user.id)

    def deactivate_user(self, user: User):
        return self.repository.deactivate(user.id)

    def get_all_users(self):
        return self.repository.get_all()

    def get_user_by_id(self, user_id):
        return self.repository.get_by_id(user_id)