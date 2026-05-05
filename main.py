from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
import joblib
import numpy as np
import os

os.environ['CUDA_VISIBLE_DEVICES'] = '-1'


app = FastAPI()
templates = Jinja2Templates(directory="/home/rabboni/Desktop/loan-pred-app/tempates")

model = joblib.load("/home/rabboni/Desktop/loan-pred-app/loan_predict_xgb_model.pkl")

@app.get("/")
async def home(request : Request):
    return templates.TemplateResponse(request, name = "index.html")

@app.post("/predict")
async def predict(
    request: Request,
    no_of_dependents: int = Form(...),
    education: int = Form(...),
    self_employed: int = Form(...),
    income_annum: int = Form(...),
    loan_amount: int = Form(...),
    loan_term: int = Form(...),
    cibil_score: int = Form(...),
    residential_assets_value: int = Form(...),
    commercial_assets_value: int = Form(...),
    luxury_assets_value: int = Form(...),
    bank_asset_value: int = Form(...)
):
    features = [
        no_of_dependents, income_annum, loan_amount, loan_term, cibil_score,
        residential_assets_value, commercial_assets_value, luxury_assets_value, 
        bank_asset_value, education, self_employed
    ]

    input_array = np.array([features])
    prediction = model.predict(input_array)
    
    if prediction == 0:
        return templates.TemplateResponse(request, name = "sucess.html")
    else:
        return templates.TemplateResponse(request, name = "failed.html")