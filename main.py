from fastapi import FastAPI
from pydantic import BaseModel
from typing import Literal

app = FastAPI()

@app.get('/home')
def home():
    return {"message":"Data is transafering right "}

class EmployeeData(BaseModel):
    job_title:str
    experience_years: int
    education_level: str
    skills_count: int
    industry: str
    company_size: str
    location: str
    remote_work: str
    certifications: int


data1 = {
    "job_title": "Data Analyst",
    "experience_years": 2,
    "education_level": "Bachelor",
    "skills_count": 3,
    "industry": "IT",
    "company_size": "Medium",
    "location": "Mumbai",
    "remote_work": "Yes",
    "certifications": 1
}


data2 = EmployeeData(**data1) 

@app.get('/result')
def result():
    return data2


@app.delete('/delete-field/{field}')
def delete(field: str):
    if hasattr(data2, field):
        setattr(data2, field, None)  # modify original object
        return {"message": f"{field} deleted"}
    return {"message": "field not found"}