from fastapi import FastAPI

app = FastAPI(
    title="NextGen Bank API",
    version="1.0.0",
    description="API for NextGen Bank application built with FastAPI",
)


@app.get("/")
async def home():
    return {"message": "Welcome to the NextGen Bank API!"}
