import { useState } from "react";
import type { PredictionRequest } from "../../models/PredictionRequest";

interface Props {
  onSubmit: (request: PredictionRequest) => void;
}

export default function PredictionForm({ onSubmit }: Props) {
  const [form, setForm] = useState<PredictionRequest>({
    age: 52,
    bp: 145,
    glucose: 180,
    cholesterol: 240,
    bmi: 31.5,
    heart_rate: 92,
    oxygen_level: 96,
    symptoms: "chest pain fatigue dizziness",
    doctor_notes: "Patient reports chest pain and fatigue",
  });

  const updateField = (
    field: keyof PredictionRequest,
    value: string | number
  ) => {
    setForm((prev) => ({
      ...prev,
      [field]: value,
    }));
  };

  return (
    <div className="card">
      <h2>Disease Prediction</h2>
      <p className="text-muted">
        Enter patient clinical information to predict the disease.
      </p>

      <form
        onSubmit={(e) => {
          e.preventDefault();
          onSubmit(form);
        }}
      >
        <div className="grid grid-2">
          <div>
            <label>Age (Years)</label>
            <input
              type="number"
              value={form.age}
              onChange={(e) =>
                updateField("age", Number(e.target.value))
              }
              placeholder="Enter Age"
              required
            />
          </div>

          <div>
            <label>Blood Pressure (mmHg)</label>
            <input
              type="number"
              value={form.bp}
              onChange={(e) =>
                updateField("bp", Number(e.target.value))
              }
              placeholder="Enter Blood Pressure"
              required
            />
          </div>

          <div>
            <label>Glucose (mg/dL)</label>
            <input
              type="number"
              value={form.glucose}
              onChange={(e) =>
                updateField("glucose", Number(e.target.value))
              }
              placeholder="Enter Glucose"
              required
            />
          </div>

          <div>
            <label>Cholesterol (mg/dL)</label>
            <input
              type="number"
              value={form.cholesterol}
              onChange={(e) =>
                updateField("cholesterol", Number(e.target.value))
              }
              placeholder="Enter Cholesterol"
              required
            />
          </div>

          <div>
            <label>BMI</label>
            <input
              type="number"
              step="0.1"
              value={form.bmi}
              onChange={(e) =>
                updateField("bmi", Number(e.target.value))
              }
              placeholder="Enter BMI"
              required
            />
          </div>

          <div>
            <label>Heart Rate (bpm)</label>
            <input
              type="number"
              value={form.heart_rate}
              onChange={(e) =>
                updateField("heart_rate", Number(e.target.value))
              }
              placeholder="Enter Heart Rate"
              required
            />
          </div>

          <div>
            <label>Oxygen Level (%)</label>
            <input
              type="number"
              value={form.oxygen_level}
              onChange={(e) =>
                updateField("oxygen_level", Number(e.target.value))
              }
              placeholder="Enter Oxygen Level"
              required
            />
          </div>
        </div>

        <div>
          <label>Symptoms</label>
          <textarea
            rows={4}
            value={form.symptoms}
            onChange={(e) =>
              updateField("symptoms", e.target.value)
            }
            placeholder="Example: Chest pain, fatigue, dizziness..."
            required
          />
        </div>

        <div>
          <label>Doctor Notes</label>
          <textarea
            rows={5}
            value={form.doctor_notes}
            onChange={(e) =>
              updateField("doctor_notes", e.target.value)
            }
            placeholder="Clinical observations and physician notes..."
            required
          />
        </div>

        <div
          style={{
            display: "flex",
            justifyContent: "flex-end",
            marginTop: "20px",
          }}
        >
          <button type="submit">
            Predict Disease
          </button>
        </div>
      </form>
    </div>
  );
}