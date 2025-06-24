from fastapi import FastAPI, Depends
from pydantic import BaseModel, EmailStr

app=FastAPI()

class UserSignUp(BaseModel):
    username:str
    email:EmailStr
    password:str
    
class Settings(BaseModel):
    app_name:str="codeFire App"
    admin_email:str="admin@codefire.com"

def get_settings(): 
    """Dependency that returns a Settings instance"""
    return Settings()


@app.post('/signup')
def signup(user:UserSignUp):
    return {'message': f'User {user.username} signed up successfully'}

@app.get('/settings')
def get_settings_endpoint(settings:Settings=Depends(get_settings)):
    """
    Application settings endpoint
    - Uses dependency injection for Settings
    - Returns current application settings
    """
    return settings
    