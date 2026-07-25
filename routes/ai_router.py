import joblib as jb
import pandas as pd
from fastapi import APIRouter
from models import PredictionRequest, PredictionResponse

router = APIRouter(tags=["AI"], prefix="/ai")
model = jb.load("models/model.pkl")
scaler = jb.load("models/scaler.pkl")
columns = jb.load("models/columns.pkl")


@router.get("/")
def ai_health_check():
    return {"status", "healthy"}


@router.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict(request: PredictionRequest):
    input = pd.DataFrame([request.model_dump()])[columns]
    scaled_input = scaler.transform(input)
    price = model.predict(scaled_input)[0]
    return {"house_price": price}
