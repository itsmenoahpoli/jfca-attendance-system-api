from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.modules.sms.controller import smsRouter
from app.modules.auth.controller import authRouter
from app.modules.accounts.controller import accountsRouter


app = FastAPI()
allowedOrigins = ['*']

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
app.include_router(authRouter)
app.include_router(accountsRouter)


@app.get('/api/healthcheck')
def root():
  return {
    "status": "online",
    "has_errors": True
  }