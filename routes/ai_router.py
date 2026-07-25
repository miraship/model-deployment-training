import joblib
from fastapi import APIRouter
from models import PredictionRequest, PredictionResponse

router = APIRouter(tags=["AI"], prefix="/ai")
model = joblib.load("models/model.pkl")
scaler = joblib.load("models/scaler.pkl")
columns = joblib.load("models/columns.pkl")


@router.get("/")
def ai_health_check():
    return {"status", "healthy"}


@router.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict(request: PredictionRequest):
    pass
