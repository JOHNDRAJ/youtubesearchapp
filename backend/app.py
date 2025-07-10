# backend/app.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.src.script import generate_vids  # this is the module that generates titles, URLs, thumbnails
app = FastAPI(debug=True)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],               # in prod, lock this down!
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/videos")
async def list_videos(query: str | None = None):
    videos = generate_vids(query)
    return {"videos": videos}
