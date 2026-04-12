from fastapi import FastAPI
from pydantic import BaseModel, ConfigDict
from typing import Optional
app = FastAPI()

class Discri(BaseModel):
    id: Optional[int] = None
    name: str
    model_config = ConfigDict(str_max_length=10)

     
