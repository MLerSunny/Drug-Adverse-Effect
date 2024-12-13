import streamlit as st
import requests

backend_url = "http://127.0.0.1:8000"  # Replace with ngrok or FlashAPI URL

st.title("Drug Adverse Event Reporting System")

# Submit Adverse Event Report
st.header("Submit Adverse Event Report")
drug_name = st.text_input("Drug Name")
adverse_event = st.text_area("Adverse Event Description")
reporter = st.text_input("Reporter")
if st.button("Submit to Blockchain"):
    response = requests.post(f"{backend_url}/store_event/", json={
        "drug_name": drug_name,
        "adverse_event": adverse_event,
        "reporter": reporter
    })
    st.write("Transaction Hash:", response.json().get("transaction_hash"))

# Fetch Reports from Blockchain
st.header("View Reports")
if st.button("Fetch Reports"):
    response = requests.get(f"{backend_url}/fetch_reports/")
    reports = response.json().get("reports", [])
    for report in reports:
        st.write(report)
