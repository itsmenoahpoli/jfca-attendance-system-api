from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Depends
from typing import List
from .database.connection import db_get_collection, db_connect
from .database.utils import format_document


app = FastAPI()
allowedOrigins = []

db_connect()

app.add_middleware(
  CORSMiddleware,
  allow_origins=allowedOrigins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)




@app.get('/api/healthcheck')
def root():
  return {
    "status": "online",
    "has_errors": True
  }