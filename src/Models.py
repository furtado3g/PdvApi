from pydantic import BaseModel


class UserData(BaseModel):
  name : str
  email : str
  phone : str
  street : str
  zipcode : str
  house_no : str
  complement : str
  city : str
  state : str
  country : str
  username : str
  password : str
  role : str
  is_active : bool
  is_admin : bool
    
  
class LoginData(BaseModel):
  username: str
  password: str