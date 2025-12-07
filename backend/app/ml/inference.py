from pathlib import Path
from typing import Tuple
import joblib

ARTIFACTS_DIR = Path(__file__).parent / "artifacts"

_pipeline = None  # cached pipeline


def load_pipeline():
    global _pipeline
    if _pipeline is None:
        model_path = ARTIFACTS_DIR / "ticket_priority_pipeline.joblib"
        if not model_path.exists():
            raise FileNotFoundError(
                f"Model file not found at {model_path}. Have you run train.py?"
            )
        _pipeline = joblib.load(model_path)
        print("Loaded pipeline with classes:", _pipeline.classes_)
    return _pipeline


def predict_priority(subject: str, body: str) -> Tuple[str, float]:
    """
    Returns:
      - predicted label (string)
      - confidence score (float between 0 and 1)
    """
    pipeline = load_pipeline()

    text = f"{subject or ''} {body or ''}".strip()
    if not text:
        raise ValueError("Both subject and body are empty.")

    proba = pipeline.predict_proba([text])[0]
    classes = pipeline.classes_
    best_idx = int(proba.argmax())

    label = classes[best_idx]
    score = float(proba[best_idx])

    return label, score
