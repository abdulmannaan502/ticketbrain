import { useState } from "react";
import api from "../api";

export default function Predict() {
  const [subject, setSubject] = useState("");
  const [body, setBody] = useState("");
  const [result, setResult] = useState<{
    priority_label: string;
    priority_score: number;
  } | null>(null);

  async function predict() {
    const res = await api.post("/ml/predict", { subject, body });
    setResult(res.data);
  }

  const priorityClass =
    result?.priority_label === "high"
      ? "badge badge-high"
      : result?.priority_label === "medium"
      ? "badge badge-medium"
      : "badge badge-low";

  return (
    <div className="app-root">
      <div className="card">
        <h1 className="card-title">Ticket Priority Prediction</h1>
        <p className="card-subtitle">
          Enter a support ticket to estimate its urgency using the trained NLP
          model.
        </p>

        <div className="form-group">
          <label className="label">Subject</label>
          <input
            className="input"
            placeholder="Server outage affecting all customers"
            value={subject}
            onChange={e => setSubject(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label className="label">Description</label>
          <textarea
            className="textarea"
            placeholder="Describe the user impact, frequency, and affected systems..."
            value={body}
            onChange={e => setBody(e.target.value)}
          />
        </div>

        <button className="btn btn-primary" onClick={predict}>
          Predict priority
        </button>

        {result && (
          <div className="result-box">
            <div className="result-title">Model prediction</div>
            <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
              <span className={priorityClass}>
                {result.priority_label.toUpperCase()}
              </span>
              <span className="confidence-text">
                Confidence: {(result.priority_score * 100).toFixed(2)}%
              </span>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}
