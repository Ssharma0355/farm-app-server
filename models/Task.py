from datetime import datetime
from pydantic import BaseModel, Field
from typing import Union

class Task(BaseModel):
    title:str = Field(...)
    des:str = Field(...)
    is_completed:Union[bool, None] = False
    created_at:datetime = Field(default=datetime.now())

class EnterName(BaseModel):
    name:str = Field(...)
    email:str = Field(...)
    # is_student: Union[bool, None] = False
