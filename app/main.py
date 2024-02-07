from fastapi import FastAPI, HTTPException
from db.database import check_db_connection
from fastapi.middleware.cors import CORSMiddleware
from core.config import FRONTEND_URL
from users.handler import user_router
from auth.handler import auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        FRONTEND_URL,
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Visit /docs for server documentation"}


# Heartbeat endpoint
@app.get("/heartbeat", tags=["heartbeat"])
async def heartbeat():
    if check_db_connection():
        return {"message": "Database connection is healthy."}
    else:
        raise HTTPException(status_code=500, detail="Database connection error")


app.include_router(user_router)
app.include_router(auth_router)
