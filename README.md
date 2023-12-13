# HealthCare-3.0
Le patient est supervisé par le réseau médical (à distance). A chaque intervalle de temps, une mise à jour de l’état du patient se fait. Utilisez la technologie Blockchain pour assurer la traçabilité des différentes mises à jour et qui pourrait voir ces mises à jour.



### Remix Solidity IDE (https://remix.ethereum.org/)

### Ganache (https://www.trufflesuite.com/ganache)

### Deploy Smart Contract
- open Remix Solidity IDE
- copy/paste code from file SmartContract.sol
- select compiler version 0.8.19+commit.c4cbbb05
- select tab Run
- select Environment Web3 Provider **Dev Ganache**
- click button Deploy
- copy/paste address contract in file main.py

### Install Environment Python
```pip install -r requirements.txt```

### Run Python Script
- open terminal
- run command 
```uvicorn main:app --reload```
- open browser
- go to url http://127.0.0.1:8000

