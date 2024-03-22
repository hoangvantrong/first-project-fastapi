from fastapi import FastAPI, HTTPException, Response, status, Depends
from . import models, schemas, utils, oauth2
from .database import engine, get_db
from .routers import post, user, auth, vote
from .config import settings

from fastapi.middleware.cors import CORSMiddleware



# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def home_page():
    return {"Hello": "Welcome to the FastAPI"}

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)



    