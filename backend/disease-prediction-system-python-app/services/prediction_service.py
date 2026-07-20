from implementations.disease_predictor import DiseasePredictor

predictor = DiseasePredictor()

def predict_disease(request):
    result = predictor.predict(request)
    return result