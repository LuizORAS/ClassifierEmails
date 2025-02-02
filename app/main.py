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
    "https://email-automation-front-luizs-projects-4d67f0b6.vercel.app/",
    "https://email-automation-front-git-master-luizs-projects-4d67f0b6.vercel.app/",
    "https://vercel.com/luizs-projects-4d67f0b6/email-automation-front/8yBGWKmgDkaSivgy88uB8MX5zzcq"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(email_controller.router)
