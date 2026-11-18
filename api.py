from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import chunk_text

app = FastAPI()

class ChunkRequest(BaseModel):
    text: str
    size: int = 50
    overlap: int = 10


@app.get("/")
def status():
    return {"status": "ok"}

@app.post("/chunks")
def create_chunks(request: ChunkRequest):
    try:
        chunks = chunk_text(request.text, request.size, request.overlap)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"count": len(chunks),
            "chunks": chunks}