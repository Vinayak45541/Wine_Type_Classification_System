import os
from fastapi import FastAPI
from .schema import WineInput
from .predictor import predict_wine
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Wine Type Classifier API")

# Allow the deployed frontend URL + local dev origin
FRONTEND_URL = os.environ.get("FRONTEND_URL", "http://localhost:5173")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[FRONTEND_URL, "http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Wine Prediction API Running"}

@app.post("/predict")
def predict(data: WineInput):
    return predict_wine(data)