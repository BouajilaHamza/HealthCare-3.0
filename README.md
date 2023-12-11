# HealthCare-3.0
Le patient est supervisé par le réseau médical (à distance). A chaque intervalle de temps, une mise à jour de l’état du patient se fait. Utilisez la technologie Blockchain pour assurer la traçabilité des différentes mises à jour et qui pourrait voir ces mises à jour.



### Remix Solidity IDE (https://remix.ethereum.org/)

### Ganache (https://www.trufflesuite.com/ganache)

### Environment Dev Ganache

### 
## Smart Contarct
```solidity
// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.9.0;
contract PatientContract {
    struct Patient {
        string PatientId;
        string First_Name;
        string Last_Name;
        int32 age;
        string maladie;
        string gender;
        string message;
    }

    mapping(string => Patient) public patientUpdates;

    // Constructor to initialize the contract
    constructor() {
        // You can add any initialization logic here
    }

    function addPatent(string memory patientid ,string memory firstname , string memory lastname ,int32  age,string memory maladie , string memory gender,string memory message) public {
        Patient memory
        p = Patient(patientid,firstname,lastname,age,maladie,gender,message);
        patientUpdates[patientid] =p;
    }

    function getPatientInfos(string memory patientId) public view returns (Patient memory){
        return patientUpdates[patientId];
    }


    function updatePatient(string memory patientId, string memory updateMessage,int32 newage) public returns (bool) {
        Patient memory p = patientUpdates[patientId];
        p.message = updateMessage;
        p.age = newage;
        patientUpdates[patientId] = p;
        return true;
    }

}
```