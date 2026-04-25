from fastapi import FastAPI 
from pydantic import BaseModel
from fastapi.responses import FileResponse
from typing import Literal
import joblib
import pandas as pd
from fastapi.middleware.cors import CORSMiddleware 

model = joblib.load('./models.pkl')

app = FastAPI() 

# this code is for the middleware browser and backend 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EmployeeData(BaseModel):
    job_title: Literal["Backend Developer", "Cybersecurity Analyst" ,'Product Manager','AI Engineer','Data Scientist','DevOps Engineer','Software Engineer','Data Analyst','Cloud Engineer ','Machine Learning Engineer','Business Analyst','Frontend Developer']
    experience_years: int
    education_level: str
    skills_count: int
    industry: str
    company_size: str
    location: str
    remote_work: str
    certifications: int


@app.get("/")
async def serve_frontend():
    return FileResponse("index.html")

@app.post('/predict')
def predict(data: EmployeeData):
    data = data.model_dump()
    input_df = pd.DataFrame([data])   

    prediction = model.predict(input_df)

    return {
        "predicted_salary": prediction.item()
    }
