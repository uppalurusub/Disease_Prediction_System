import joblib
import pandas as pd


class DiseasePredictor:

    def __init__(self):

        # Load trained pipeline
        self.model = joblib.load(
            "trained_models/ensemble_model.pkl"
        )

        # Load label encoder
        self.label_encoder = joblib.load(
            "trained_models/label_encoder.pkl"
        )

    def predict(self, request):

        # Create dataframe
        input_data = pd.DataFrame([{

            "age": request.age,

            "bp": request.bp,

            "glucose": request.glucose,

            "cholesterol": request.cholesterol,

            "bmi": request.bmi,

            "heart_rate": request.heart_rate,

            "oxygen_level": request.oxygen_level,

            "combined_text":
                request.symptoms + " " +
                request.doctor_notes

        }])

        # Predict
        prediction = self.model.predict(
            input_data
        )[0]

        # Probabilities
        probabilities = self.model.predict_proba(
            input_data
        )[0]

        # Decode prediction
        disease_name = (
            self.label_encoder.inverse_transform(
                [prediction]
            )[0]
        )

        return {

            "prediction": disease_name,

            "confidence": round(
                float(max(probabilities)),
                4
            )

        }