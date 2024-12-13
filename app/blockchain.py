from web3 import Web3
import json

# Connect to Polygon Mumbai via Infura
infura_url = "https://polygon-mumbai.infura.io/v3/YOUR_INFURA_PROJECT_ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Load Contract
contract_address = "YOUR_CONTRACT_ADDRESS"
with open("contract/AdverseEventReport_abi.json") as f:
    abi = json.load(f)

contract = web3.eth.contract(address=contract_address, abi=abi)

# Store adverse event on the blockchain
def store_event_on_blockchain(drug_name, adverse_event, reporter):
    tx = contract.functions.addReport(drug_name, adverse_event, reporter).buildTransaction({
        "from": web3.eth.accounts[0],  # Replace with a funded account
        "gas": 2000000,
        "gasPrice": web3.toWei("20", "gwei"),
        "nonce": web3.eth.getTransactionCount(web3.eth.accounts[0])
    })
    signed_tx = web3.eth.account.sign_transaction(tx, private_key="YOUR_PRIVATE_KEY")
    tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
    return web3.toHex(tx_hash)

# Fetch reports from the blockchain
def fetch_reports_from_blockchain():
    return contract.functions.getReports().call()
