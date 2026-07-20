import type { PredictionResponse } from "../../models/PredictionResponse";

interface Props {
  result: PredictionResponse;
}

import "../../styles/PredictionResponse.css"

export default function PredictionResult({ result }: Props) {
  const confidence = Number((result.confidence * 100).toFixed(2));

  const getRiskColor = () => {
    if (confidence >= 80) return "#2e7d32";
    if (confidence >= 60) return "#ed6c02";
    return "#d32f2f";
  };

  return (
    <div className="prediction-card">

      <div className="prediction-header">
        <h2>🩺 Disease Prediction Result</h2>
      </div>

      <div className="prediction-body">

        <div className="prediction-item">
          <span className="label">Predicted Disease</span>

          <div
            className="prediction-badge"
            style={{ backgroundColor: getRiskColor() }}
          >
            {result.prediction}
          </div>
        </div>

        <div className="prediction-item">
          <span className="label">Model Confidence</span>

          <strong>{confidence}%</strong>

          <div className="progress">

            <div
              className="progress-bar"
              style={{
                width: `${confidence}%`,
                backgroundColor: getRiskColor(),
              }}
            />

          </div>

        </div>

        <div className="prediction-item">

          <span className="label">
            Clinical Recommendation
          </span>

          <div className="recommendation">

            {confidence >= 70
              ? "⚠ High confidence prediction. Recommend immediate specialist consultation and further diagnostic evaluation."
              : confidence >= 40
              ? "🟡 Moderate confidence prediction. Additional laboratory tests and physician review are recommended."
              : "🟢 Low confidence prediction. Clinical correlation and further assessment are advised before making a diagnosis."}

          </div>

        </div>

      </div>

    </div>
  );
}