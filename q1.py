from datetime import datetime
from fastapi import FastAPI, HTTPException

app = FastAPI()
transactions = []

@app.post("/transactions", status_code=201)
def add_transaction(data: dict):
    if not data.get("user_id"):
        raise HTTPException(400, "user_id is required")

    if data.get("amount", 0) <= 0:
        raise HTTPException(400, "amount must be greater than 0")

    if data.get("type") not in ["credit", "debit"]:
        raise HTTPException(400, "type must be credit or debit")

    try:
        datetime.fromisoformat(data["timestamp"])
    except (ValueError, KeyError):
        raise HTTPException(400, "invalid timestamp")

    transactions.append(data)
    return data

@app.get("/transactions/{user_id}")
def get_transactions(user_id: str):
    return [t for t in transactions if t["user_id"] == user_id]

@app.get("/transactions/{user_id}/summary")
def get_summary(user_id: str):
    user_transactions = get_transactions(user_id)

    credit = sum(t["amount"] for t in user_transactions if t["type"] == "credit")
    debit = sum(t["amount"] for t in user_transactions if t["type"] == "debit")

    return {
        "total_credit": credit,
        "total_debit": debit,
        "balance": credit - debit
    }