from pydantic import BaseModel, Field, model_validator, EmailStr
from fastapi import UploadFile
import json 
class SNewProduct(BaseModel):
    title: str = Field(max_length=50)
    description: str = Field(max_length=800)
    price: float = Field(ge = 0)
    quantity: int = Field(ge = 0)
    img_path : str = None

    @model_validator(mode='before')
    @classmethod
    def validate_to_json(cls, value):
        if isinstance(value, str):
            return cls(**json.loads(value))
        return value
    

class SProduct(SNewProduct):
    id : int


class SProductOutput(SNewProduct):
    id : int
    title: str = Field(max_length=50)
    description: str = Field(max_length=800)
    price: float = Field(ge = 0)
    quantity: int = Field(ge = 0)



class SNewUser(BaseModel):
    name : str = Field(min_length=3, max_length=20)
    surname : str = Field(min_length=3, max_length=20)
    email : EmailStr = Field(min_length=6)
    password : str = Field(min_length=6)

class SUser(SNewUser):
    id : int

class SUserLogin(BaseModel):
    email : EmailStr = Field(min_length=6)
    password : str = Field(min_length=6)




