from fastapi import FastAPI
from app.blockchain import store_event_on_blockchain, fetch_reports_from_blockchain

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Drug Adverse Effect Monitoring System"}

@app.post("/store_event/")
def store_event(drug_name: str, adverse_event: str, reporter: str):
    # Call blockchain logic to store the event
    tx_hash = store_event_on_blockchain(drug_name, adverse_event, reporter)
    return {"transaction_hash": tx_hash}

@app.get("/fetch_reports/")
def fetch_reports():
    # Fetch all reports from the blockchain
    reports = fetch_reports_from_blockchain()
    return {"reports": reports}
