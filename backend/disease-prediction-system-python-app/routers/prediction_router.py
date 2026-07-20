from fastapi import APIRouter
from models.request_models import DiseasePredictionRequest
from services.prediction_service import predict_disease

router = APIRouter(prefix="/predict", tags=["Prediction"])

@router.post("/")
def predict(request: DiseasePredictionRequest):
    return predict_disease(request)