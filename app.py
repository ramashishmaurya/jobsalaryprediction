from fastapi import FastAPI 
from pydantic import BaseModel
from typing import Literal
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware  # ✅ add karo

model = joblib.load('./models.pkl')

app = FastAPI() 

# ✅ Ye block add karo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmployeeData(BaseModel):
    job_title: Literal["Backend Developer", "Cybersecurity Analyst" ,'Product Manager','AI Engineer ','Data Scientist','DevOps Engineer','Software Engineer','Data Analyst ','Cloud Engineer ','Machine Learning Engineer','Business Analyst','Frontend Developer']
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
    return {'message': 'Salary prediction API is running'}

@app.post('/predict')
def predict(data: EmployeeData):
    data = data.model_dump()
    input_df = pd.DataFrame([data])   

    prediction = model.predict(input_df)

    return {
        "predicted_salary": prediction.item()
    }