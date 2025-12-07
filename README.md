# 🎫 TicketBrain — AI-Powered Support Ticket Prioritization System

TicketBrain is a full-stack Machine Learning application that automatically classifies customer support tickets into **High / Medium / Low priority** using NLP-based text classification.

This project demonstrates production-level ML engineering skills, including:

- Data preprocessing and model training
- Model serving via FastAPI
- Secure authentication
- REST API design
- React dashboard integration
- End-to-end system orchestration

---

## 🚀 Project Goal

Support teams receive hundreds or thousands of tickets daily. Manual triage slows response time and can cause high-priority incidents to be overlooked.

**TicketBrain uses AI to automatically triage tickets** so that urgent issues are handled first.

---

## 🧠 Machine Learning

**Model:**
- TF-IDF vectorizer
- Logistic Regression classifier
- 3-class prediction: `High`, `Medium`, `Low`

**Training Pipeline:**

Raw CSV → Text Cleaning → TF-IDF Encoding →  
Model Training → Evaluation → Saved Pipeline (`.joblib`)

---

## 🔌 Backend (FastAPI)

**Core features:**
- User registration & login (JWT authentication)
- ML inference endpoint
- Confidence score output
- Health check API

**Endpoints**

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/auth/register` | POST | Create new user |
| `/auth/login` | POST | Authenticate user |
| `/predict` | POST | Run ticket classification |
| `/health` | GET | API health status |

**Sample Response**

```json
{
  "priority_label": "high",
  "priority_score": 0.56
}
```
## 📸 Demo Screenshots

### 🔐 Login Screen
![Login Screen](https://github.com/abdulmannaan502/ticketbrain/blob/3c5cbb4a8dc30fffd06e6fe17bb7475828587f3c/Img/login.png)

---

### 🎫 Ticket Submission & Priority Prediction
![Ticket Priority](https://github.com/abdulmannaan502/ticketbrain/blob/233b94cdd9a39b6306c01c525bfc069074137765/Img/tp.png)

---

### ✅ Prediction Result Page
![Response](https://github.com/abdulmannaan502/ticketbrain/blob/233b94cdd9a39b6306c01c525bfc069074137765/Img/result.png)

---

## 🌐 Frontend (React + TypeScript)

**Features**
- Secure login screen
- Protected dashboard
- Ticket submission form
- Priority + confidence display

**Routes**
- `/login`
- `/predict`

---

## 🧱 Architecture

[ React UI ] → [ FastAPI Backend ] → [ ML Pipeline ]

---

## ⚙️ Local Setup

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open API docs:

http://127.0.0.1:8000/docs

---

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open app:

http://localhost:5173

---

## 📦 Frontend Production Build

```bash
npm run build
```

Static output:

`frontend/dist/`

Can be deployed to GitHub Pages, Netlify, or Vercel.

---

## 🗃️ Project Structure

```
ticketbrain/
├── backend/
│   ├── app/
│   │   ├── routes/
│   │   ├── ml/
│   │   └── schemas.py
│   └── requirements.txt
├── frontend/
│   └── src/
│       └── pages/
└── README.md
```

---

## 🎓 Academic Relevance

Demonstrates:

- Applied NLP & ML pipelines
- Secure backend API design
- Full-stack system integration
- Real-world MLOps foundations

Perfect for MSc AI portfolio and ML engineering roles.

---

## 📈 Future Improvements

- Batch ticket submission
- Topic clustering
- Active learning feedback
- SLA prediction
- Dashboard analytics

---

## 👤 Author

**Abdul Mannaan**

GitHub: https://github.com/abdulmannaan502

---

## ✅ License

MIT License
