from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    description : str
    price : float
    quantity : int
    
    # use if no base model    
    # def __init__(self, id: int, name: str, descriptiom : str, price : float, quantity : int):
    #     self.id = id
    #     self.name = name
    #     self.description = descriptiom
    #     self.price = price
    #     self.quantity = quantity
    
    
class UserCreate(BaseModel):
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str