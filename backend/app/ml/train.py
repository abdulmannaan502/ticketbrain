import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
import joblib
from huggingface_hub import hf_hub_download

ARTIFACTS_DIR = Path(__file__).parent / "artifacts"
ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

def load_and_preprocess():
    # Download CSV from HF Dataset
    csv_path = hf_hub_download(
        repo_id="abdulmannaan1/ticketbrain-tickets",  # <— your dataset repo
        filename="tickets_raw.csv",
        repo_type="dataset",
    )
    print("Loading dataset from:", csv_path)
    df = pd.read_csv(csv_path)

    required_cols = ["subject", "body", "priority", "language"]
    for col in required_cols:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")

    df = df[required_cols].copy()
    df = df.dropna(subset=["priority"])

    df["subject"] = df["subject"].fillna("")
    df["body"] = df["body"].fillna("")
    df["text"] = (df["subject"] + " " + df["body"]).str.strip()
    df = df[df["text"].str.len() > 0]

    X = df["text"]
    y = df["priority"]

    return X, y

# rest of train.py unchanged…



def build_pipeline():
    """
    Creates an NLP pipeline:
    - TfidfVectorizer
    - Multiclass Logistic Regression
    """
    text_clf = Pipeline(
        steps=[
            (
                "tfidf",
                TfidfVectorizer(
                    ngram_range=(1, 2),
                    max_features=50000,
                    min_df=3,
                ),
            ),
            (
                "clf",
                LogisticRegression(
                    max_iter=1000,
                    n_jobs=-1,
                ),
            ),
        ]
    )
    return text_clf


def main():
    X, y = load_and_preprocess()

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y,  # keep class balance
    )

    print(f"Train size: {X_train.shape[0]}, Test size: {X_test.shape[0]}")

    pipeline = build_pipeline()

    print("\nTraining model...")
    pipeline.fit(X_train, y_train)

    print("\nEvaluating on test set...")
    y_pred = pipeline.predict(X_test)
    report = classification_report(y_test, y_pred)
    print(report)

    # Save pipeline (includes vectorizer + classifier + label mapping)
    model_path = ARTIFACTS_DIR / "ticket_priority_pipeline.joblib"
    joblib.dump(pipeline, model_path)
    print(f"\nSaved trained pipeline to: {model_path}")

    # Show class order (for later reference)
    print("Model classes (order):", pipeline.classes_)


if __name__ == "__main__":
    main()
