from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import uvicorn
from typing import List
from src.vectordb import VectorDB
from config import(
    MODEL_NAME,
    PROJECT_ID,
    DATASET_NAME,
    VECTOR_TABLE_NAME,
    LOCATION
)


app = FastAPI()
templates = Jinja2Templates(directory="templates")
vector_db = VectorDB(MODEL_NAME, PROJECT_ID, DATASET_NAME, VECTOR_TABLE_NAME, LOCATION)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/search")
async def search(query: str = Form(...)):
    results = vector_db.similarity_search(query, k=100)
    results = [result.metadata for result in results]
    return {"query": query, "results": results}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)