from datetime import datetime
import json


class User:
    def __init__(self,
                 id: int = None,
                 name: str = None,
                 email: str = None,
                 phone: str = None,
                 street: str = None,
                 zipcode: str = None,
                 house_no: str = None,
                 complement: str = None,
                 city: str = None,
                 state: str = None,
                 country: str = None,
                 username: str = None,
                 password: str = None,
                 role: str = None,
                 is_active: bool = None,
                 is_admin: bool = None,
                 created_at: datetime = None,
                 updated_at: datetime = None,
                 ):
        self.id = id
        self.name = name
        self.email = email
        self.phone = phone
        self.street = street
        self.zipcode = zipcode
        self.house_no = house_no
        self.complement = complement
        self.city = city
        self.state = state
        self.country = country
        self.username = username
        self.password = password
        self.role = role
        self.is_active = is_active
        self.is_admin = is_admin
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "street": self.street,
            "zipcode": self.zipcode,
            "house_no": self.house_no,
            "complement": self.complement,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "is_active": self.is_active,
            "is_admin": self.is_admin,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def to_insert(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "street": self.street,
            "zipcode": self.zipcode,
            "house_no": self.house_no,
            "complement": self.complement,
            "city": self.city,
            "state": self.state,
            "country": self.country,
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "is_active": self.is_active,
            "is_admin": self.is_admin,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    def from_dict(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.email = data["email"]
        self.phone = data["phone"]
        self.street = data["street"]
        self.zipcode = data["zipcode"]
        self.house_no = data["house_no"]
        self.complement = data["complement"]
        self.city = data["city"]
        self.state = data["state"]
        self.country = data["country"]
        self.username = data["username"]
        self.password = data["password"]
        self.role = data["role"]
        self.is_active = data["is_active"]
        self.is_admin = data["is_admin"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        return self

    def to_json(self):
        return json.dumps(self.to_dict())

    def __repr__(self):
        return f"<User {self.id}>"

    def __str__(self):
        return f"User {self.id}"
