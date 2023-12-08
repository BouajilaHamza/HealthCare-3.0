from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from web3 import Web3
from model import PatientUpdate


app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Web3 configuration
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))  # Update with your Ganache or private blockchain URL

# Smart Contract Address and ABI
contract_address = "0x1234567890123456789012345678901234567890"  # Update with your deployed contract address
contract_abi = [...]  # Update with your contract ABI

contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def get_contract():
    return contract

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/update_patient")
async def update_patient(update: PatientUpdate, contract=Depends(get_contract)):
    try:
        # Call the smart contract method to update patient
        tx_hash = contract.functions.updatePatient(update.patient_id, update.update_message).transact()
        tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)
        return {"status": "success", "transaction_hash": tx_hash.hex()}
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
