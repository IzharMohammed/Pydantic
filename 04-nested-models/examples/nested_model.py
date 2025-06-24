from pydantic import BaseModel
from typing import Optional,List

class Address(BaseModel):
    street:str
    city:str
    postal_code:str

class User(BaseModel):
    id:int
    name:SyntaxError
    address:Address

class Comment(BaseModel):
    id:int
    content:str
    replies:Optional[List['Comment']]=None

Comment.model_rebuild()

address = Address(
    street = "123 something",
    city = "Jaipur",
    postal_code = "10001",
)

user = User(
    id= 1,
    name= "Hitesh",
    address = address,
)

comment=Comment(
    id=1,
    content="1st comment",
    replies=[
        Comment(id=2,content="reply 1"),
        Comment(id=3,content="reply 2")
    ]
)