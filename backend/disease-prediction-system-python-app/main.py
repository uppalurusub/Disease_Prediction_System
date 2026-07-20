from fastapi import FastAPI
from routers.prediction_router import router

app = FastAPI(
    title="Disease Prediction System",
    version="1.0"
)

app.include_router(router)

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)