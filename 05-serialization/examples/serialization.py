from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    createdAt: datetime
    address: Address
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S')}
    )
    
# create a user instance
user = User(
    id= 1,
    name= "izhar",
    email= "izhar@hc.com",
    createdAt = datetime(2024, 3, 15, 14, 30),
    address= Address(
        street = "something",
        city = "kurnool",
        zip_code = "001144"
    ),
    is_active = False,
    tags = ["premium", "subscriber"],
)

# Using model_dump() -> dict
python_dict=user.model_dump()
print(type(python_dict))
print(python_dict)
'''
<class 'dict'>
{'id': 1, 'name': 'izhar', 'email': 'izhar@hc.com', 'is_active': False, 'createdAt': datetime.datetime(2024, 3, 15, 14, 30), 'address': {'street': 'something', 'city': 'kurnool', 'zip_code': '001144'}, 'tags': ['premium', 'subscriber']}
'''

print("-------------------------")
# Using model_dump_json()
json_str = user.model_dump_json()
print(type(json_str))
print(json_str)
'''
<class 'str'>
{"id":1,"name":"izhar","email":"izhar@hc.com","is_active":false,"createdAt":"15-03-2024 14:30:00","address":{"street":"something","city":"kurnool","zip_code":"001144"},"tags":["premium","subscriber"]}
'''