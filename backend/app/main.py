from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .config import settings
from .database import Base, engine
from . import models  # 👈 IMPORTANT: ensures User/TicketLog are registered
from .routes import auth_routes, predict_routes, health_routes

# Create tables (SQLite dev). In production you'd use migrations.
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

# CORS for React dev on http://localhost:5173
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "TicketBrain backend running"}


app.include_router(health_routes.router)
app.include_router(auth_routes.router)
app.include_router(predict_routes.router)
