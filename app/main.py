from fastapi import FastAPI
from config import RunConfig
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


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=RunConfig.host,
        port=RunConfig.port,
        reload=True)
