import bcrypt


class UserController:
    
  @classmethod
  async def create_user(self, data:dict): 
    await self.db.connect()
    user = {
        'name':data["name"],
        'email':data["email"],
        'phone':data["phone"],
        'street':data["street"],
        'zipcode':data["zipcode"],
        'house_no':data["house_no"], 
        'complement':None if "complement" not in data else data["complement"],
        'city':data["city"],
        'state':data["state"],
        'country':data["country"],
        'username':data["username"],
        'password': bcrypt.hashpw(data["password"].encode('utf-8'), salt=bcrypt.gensalt()).decode("utf-8"),
        'role':data["role"],
        'is_active':data["is_active"],
        'is_admin':data["is_admin"],
    }
    if await self.db.user.find_unique(where={
        "username": user["username"]
    }):
        await self.db.disconnect()
        return {
            "status":"error", 
            "message": "Nome de usuário já esta em uso!"
        }
    elif await self.db.user.find_unique(where={
        "email": user["email"]
    }) :
        await self.db.disconnect()
        return {
            "status": "error",
            "message": "Email já esta em uso!"
        }
    else: 
        r = await self.db.user.create(data=user)
        await self.db.disconnect()
        return r