from typing import Annotated
from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from web3 import Web3
from app.models.model import PatientUpdate
from app.constants import contract_abi
from app.schemas.update_patient_schema import PatientUpdate





app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# Web3 configuration
w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))  # Update with your Ganache or private blockchain URL

# Smart Contract Address and ABI
contract_address = "0xfb547a7979e0Dc5b91f09D8FCcA12eeA09535ed5"  # Update with your deployed contract address


contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def get_contract():
    return contract

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/update_patient",response_class=HTMLResponse)
async def update_patient(request: Request,patient_id: Annotated[str, Form()], update_message: Annotated[str, Form()], contract=Depends(get_contract)):
    try:
        print(patient_id, update_message)
        tx_hash = contract.functions.updatePatient(patient_id,update_message).transact({'from': w3.eth.accounts[0]})
        tx_receipt = w3.eth.get_transaction_receipt(tx_hash)
     
        return templates.TemplateResponse("result.html",{"request": request,
                                                         "status": "success", 
                                                         "TransactionHash": tx_hash.hex(),
                                                         "BlockHash": tx_receipt.get('blockHash'),
                                                         "BlockNumber": tx_receipt.get('blockNumber'),
                                                         "TransactionIndex": tx_receipt.get('transactionIndex'),
                                                         "GasUsed": tx_receipt.get('gasUsed')})
    except Exception as e:
        return {"status": "error", "error_message": str(e)}
