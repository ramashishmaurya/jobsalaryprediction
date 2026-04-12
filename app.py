from fastapi import FastAPI 
from pathlib import Path
from pydantic import BaseModel
from typing import Literal
import joblib
import pandas as pd

import joblib

model =joblib.load('./model.pkl')



app = FastAPI() 

class EmployeeData(BaseModel):
    job_title: Literal["Backend Developer" ,"Cybersecurity Analyst"]
    experience_years: int
    education_level: str
    skills_count: int
    industry: str
    company_size: str
    location: str
    remote_work: str
    certifications: int

@app.get('/')
def home():
    return{'message':'Salary prediction API is running'}

@app.post('/predict')
def predict(data:EmployeeData):
    data = data.model_dump()
    input_df = pd.DataFrame([data])[0]
    prediction = model.predict(input_df)[0]

    return {
        "predicted_salary": prediction
    }