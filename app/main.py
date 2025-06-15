from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config import settings
import uvicorn
from models import db_helper
from contextlib import asynccontextmanager
from api import router as api_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    # startup
    await db_helper.init()

    yield

    # shotdown
    await db_helper.dispose_all()


app = FastAPI(lifespan=lifespan)
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_config.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.run.host,
        port=settings.run.port,
        reload=True)
