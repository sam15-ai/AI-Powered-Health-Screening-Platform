from fastapi import FastAPI

from models.database import Base, engine
from routers.auth import router as auth_router


app = FastAPI(
    title="AI-Powered Health Screening Platform API",
    description=(
        "Backend API for AI-assisted preliminary health screening workflows."
    ),
    version="0.1.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_router)


@app.get("/")
def read_root() -> dict[str, str]:
    return {
        "message": "Welcome to the AI-Powered Health Screening Platform backend."
    }
