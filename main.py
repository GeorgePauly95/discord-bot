from pydantic import BaseModel
import os
from fastapi import FastAPI, Body, Header
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}
