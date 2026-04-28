from fastapi import FastAPI

from fastapi.middleware.cors import \
CORSMiddleware

from app.database import (
Base,
engine
)

from app.routers import (
reservations,
tables,
analytics
)


# Create tables automatically
Base.metadata.create_all(
bind=engine
)


app=FastAPI(
title="Restaurant Ops Platform"
)


# Allows frontend calls
app.add_middleware(
CORSMiddleware,
allow_origins=["*"],
allow_credentials=True,
allow_methods=["*"],
allow_headers=["*"]
)


# Register routers
app.include_router(
reservations.router
)

app.include_router(
tables.router
)

app.include_router(
analytics.router
)


@app.get("/")
def home():

 return {
   "message":"API running"
 }
