from fastapi import FastAPI
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse

load_dotenv()
import os
from pymongo import MongoClient
from contextlib import asynccontextmanager
from routes import books

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    app.mongodb_client = MongoClient(host=os.getenv("MONGO_DB_URL"))
    app.database = app.mongodb_client["test"]
    print("Connected to the MongoDB database!")
    yield
    app.mongodb_client.close()


app = FastAPI(lifespan=lifespan)
app.include_router(books.router)

@app.get("/")
async def read_root():
    return RedirectResponse("/docs")
