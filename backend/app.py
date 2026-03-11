#aProject/backend/app.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors  import CORSMiddleware
from dotenv import load_dotenv
from pydantic import BaseModel
import os
from gen import generateImage

origins=["http://localhost:3000", "http://127.0.0.1:3000"]

load_dotenv()
default_url = os.getenv("default_url", "https://i.ytimg.com/vi/t5FBwq-kudw/maxresdefault.jpg")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=['*'],
    allow_headers=['*'],
    )

@app.get("/generate/{prompt}/{n_images}")
def generate(prompt:str, n_images:int):
    result = generateImage(prompt, n_images)
    return result


