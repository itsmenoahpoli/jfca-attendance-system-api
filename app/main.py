from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from src.modules.sms.controller import smsRouter


app = FastAPI()
allowedOrigins = []

app.add_middleware(
  CORSMiddleware,
  allow_origins=allowedOrigins,
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

'''
API Routes
'''
app.include_router(smsRouter)


@app.get('/api/healthcheck')
def root():
  return {
    "status": "online",
    "has_errors": True
  }