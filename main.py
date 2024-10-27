from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
allowedOrigins = [
  'http://localhost:5173',
  'http://127.0.0.1:5173',
  'http://0.0.0.0:5173',
]

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