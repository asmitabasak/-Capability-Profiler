from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

# Enable CORS for React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], # Vite default port
    allow_methods=["*"],
    allow_headers=["*"],
)

class DataItem(BaseModel):
    name: str
    value: int

@app.get("/api/health")
def health_check():
    return {"status": "online", "version": "1.0.0"}

@app.post("/api/data")
def process_data(item: DataItem):
    # This is where your AI/Logic/Database calls go
    return {"received": item, "message": "Success"}
