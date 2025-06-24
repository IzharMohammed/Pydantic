from pydantic import BaseModel, field_validator, model_validator, computed_field 

class User(BaseModel):
    username: str  # Field declaration with type hint

    @field_validator("username")
    def username_length(cls, v):
        """
        Validates that username has at least 4 characters.
        
        Args:
            cls: The model class (User)
            v: The value being validated (username string)
            
        Returns:
            The validated username if checks pass
            
        Raises:
            ValueError: If username is too short
        """
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters")
        return v

'''
Key Points:

Validates a single field (username)

Runs before the model is instantiated

Must return the validated value (or modified version)

Can access only the field being validated
''' 


class SignUpData(BaseModel):
    password: str
    confirm_password: str  # Field to match against password

    @model_validator(mode='after')
    def password_match(cls, values):
        """
        Validates that password and confirm_password match.
        Runs AFTER individual field validations.
        
        Args:
            cls: The model class (SignUpData)
            values: Dict-like object containing all field values
            
        Returns:
            The validated model values if checks pass
            
        Raises:
            ValueError: If passwords don't match
        """
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values

'''
Key Points:

Validates relationships between multiple fields

mode='after' means it runs after individual field validations

Receives all field values in a values object

Can modify multiple fields before returning
''' 

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        """
        Computed field that calculates price × quantity.
        Automatically updates when price or quantity changes.
        
        Returns:
            The computed total price as float
        """
        return self.price * self.quantity

'''
Key Points:

Creates a read-only field derived from other fields

Recomputes whenever accessed

Included in model's .model_dump() output

Type hinted with return annotation (-> float)
'''

# Valid User
user = User(username="izhar")

# Invalid User
try:
    user=User(username="izh")
except ValueError as e:
    print(e)  # "Username must be at least 4 characters"

# Valid SignUp
signup = SignUpData(password="secret",confirm_password="secret")

# Invalid SignUp
try:
    signup = SignUpData(password="secret", confirm_password="wrong")
except ValueError as e:
    print(e)  # "Passwords do not match"


# Product with computed field
product = Product(price=9.99, quantity=3)
print(product.total_price) # 29.97