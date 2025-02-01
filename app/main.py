from fastapi import FastAPI
from app.controllers import email_controller
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Email Classifier API",
    description="This API allows users to classify emails and manage email processing.",
    version="1.0.0",
    contact={
        "name": "Luiz Felipe de Lima Barbosa",
        "url": "https://github.com/LuizORAS",
    },
)

origins = [
    "https://email-automation-front-kappa.vercel.app/",
    "http://localhost:8000",
    "http://email-automation-front-kappa.vercel.app/home",
    "http://email-automation-front-kappa.vercel.app",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(email_controller.router)
