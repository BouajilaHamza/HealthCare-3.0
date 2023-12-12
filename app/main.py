from typing import Annotated
from fastapi import FastAPI, Form, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from web3 import Web3
from app.models.model import PatientUpdate
from app.constants import contract_abi
from app.schemas.update_patient_schema import PatientUpdate
import numpy as np
from fastapi.encoders import jsonable_encoder



app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
app.mount("/assets", StaticFiles(directory="app/assets"), name="assets")

templates = Jinja2Templates(directory="app/templates")

w3 = Web3(Web3.HTTPProvider('http://localhost:7545'))  # Update with your Ganache or private blockchain URL

contract_address = "0x440c50002e510e34BB02c307bE4379604B36a02A"  # Update with your deployed contract address


contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def get_contract():
    return contract


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})



@app.post("/add_patient",response_class=HTMLResponse)
async def add_patient(  request: Request,
                        patient_id: Annotated[str, Form()],
                        first_name: Annotated[str, Form()],
                        last_name: Annotated[str, Form()],
                        age: Annotated[int, Form()],
                        gender: Annotated[str, Form()],
                        illness:Annotated[str , Form()],
                        message: Annotated[str, Form()], 
                        contract=Depends(get_contract)):
    try:        
        tx_hash = contract.functions.addPatient(patient_id,first_name,last_name,age,gender,illness,message).transact({'from': w3.eth.accounts[1]})
        patient_receipt = contract.functions.getPatientInfos(patient_id).call()
        return templates.TemplateResponse("result.html",{"request": request,"status": "success", "PatientID": patient_receipt[0],"First_Name":patient_receipt[1],"Last_Name": patient_receipt[2],"Age": patient_receipt[3],"Gender":patient_receipt[4],"Illness":patient_receipt[5],"Message": patient_receipt[6]})
    except Exception as e:
        return  templates.TemplateResponse("result.html",{"request": request,"status": "error",  "error_message": str(e)})
    
    
    


@app.post("/update_patient",response_class=HTMLResponse)
async def update_patient(  request: Request,
                        patient_id: Annotated[str, Form()],
                        first_name: Annotated[str, Form()],
                        last_name: Annotated[str, Form()],
                        age: Annotated[int, Form()],
                        illness:Annotated[str , Form()],
                        message: Annotated[str, Form()], 
                        contract=Depends(get_contract)):
    try:        
        tx_hash = contract.functions.updatePatient(patient_id,first_name,last_name,age,illness,message).transact({'from': w3.eth.accounts[1]})
        patient_receipt = contract.functions.getPatientInfos(patient_id).call()
        return templates.TemplateResponse("result.html",{"request": request,"status": "success", "PatientID": patient_receipt[0],"First_Name":patient_receipt[1],"Last_Name": patient_receipt[2],"Age": patient_receipt[3],"Gender":patient_receipt[5],"Illness":patient_receipt[4],"Message": patient_receipt[6]})
    except Exception as e:
        return  templates.TemplateResponse("result.html",{"request": request,"status": "error", 
                                                          "error_message": str(e)})



@app.post("/get_patient",response_class=HTMLResponse)
async def get_patient(request: Request,
                         patient_id: Annotated[str, Form()],
                         contract=Depends(get_contract)):
    try:        
        patient_receipt = contract.functions.getPatientInfos(patient_id).call()
        return templates.TemplateResponse("result.html",{"request": request,"status": "success", 
                                                         "PatientID": patient_receipt[0],
                                                         "First_Name":patient_receipt[1],
                                                         "Last_Name": patient_receipt[2],
                                                         "Age": patient_receipt[3],
                                                         "Gender":patient_receipt[4],
                                                         "Illness":patient_receipt[5],
                                                         "Message": patient_receipt[6]})
    except Exception as e:
        return  templates.TemplateResponse("result.html",{"request": request,"status": "error", 
                                                          "error_message": str(e)})
