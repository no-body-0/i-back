from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import random, time

app = FastAPI(title="ImmuneOps API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Signup(BaseModel):
    email: str
    company: str | None = None

@app.get("/")
def root():
    return {"status": "ImmuneOps backend running"}

@app.get("/metrics")
def metrics():
    return {
        "rps": random.randint(6500, 9000),
        "latency_ms": random.randint(70, 120),
        "error_rate": round(random.uniform(0.01, 0.04), 3),
        "status": "HEALTHY"
    }

@app.get("/graph")
def graph():
    return {"points": [random.randint(40, 120) for _ in range(30)]}

@app.get("/ai-reasoning")
def ai():
    msgs = [
        "Traffic spike handled via auto-scaling.",
        "CPU anomaly resolved. No rollback needed.",
        "System stable. All SLOs within limits.",
        "Predictive analysis shows low failure risk."
    ]
    return {"message": random.choice(msgs), "time": int(time.time())}

@app.post("/signup")
def signup(data: Signup):
    return {"success": True, "email": data.email}
