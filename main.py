from beanie import init_beanie
from fastapi import FastAPI, Request
from motor.motor_asyncio import AsyncIOMotorClient
import sys

import uvicorn
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import HTMLResponse

from src.models.models import Link
from contextlib import asynccontextmanager

from src.api.v1.routers import router as link_router
from fastapi.templating import Jinja2Templates

sys.path.append('templates')
templates = Jinja2Templates(directory="/Users/aleksanderkibin/PycharmProjects/short_link_service/templates")


@asynccontextmanager
async def lifespan(_: FastAPI):
    client = AsyncIOMotorClient('mongodb://localhost:27017')
    await init_beanie(database=client.db_name, document_models=[Link])
    yield
    client.close()


app = FastAPI(
    lifespan=lifespan,
    title='Post creator',
    description='Short link Service',
    version='0.1.0',
    docs_url='/api/openapi',
    openapi_url='/api/openapi.json',
)

origins = [
    "http://localhost",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(link_router)


@app.get('/', response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host='0.0.0.0',
        port=8000,
        reload=True,
    )
