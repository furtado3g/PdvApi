class UserRepository:

    def __init__(self, db):
        self.db = db

    async def get_all(self):
        return await self.db.user.find_many()

    async def get_by_id(self, user_id):
        return await self.db.user.find_first(where={"id": user_id})

    async def get_by_email(self, email):
        return await self.db.user.find_first(where={"email": email})

    async def get_by_username(self, username):
        return await self.db.user.find_first(where={"username": username})

    async def create(self, user):
        return await self.db.user.create(data=user)

    async def update(self, user):
        return await self.db.user.update(data=user)

    async def delete(self, user_id):
        return await self.db.user.delete(where={"id": user_id})

    async def deactivate(self, user_id):
        return await self.db.user.update(data={"is_active": False}, where={"id": user_id})

    async def activate(self, user_id):
        return await self.db.user.update(data={"is_active": True}, where={"id": user_id})
