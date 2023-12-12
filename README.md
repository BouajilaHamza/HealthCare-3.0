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
        int age;
        string maladie;
        string gender;
        string message;
    }

    mapping(string => Patient) public Patients;
    string[] public patientIDs;
    Patient[]public patients;
    constructor() {
        // You can add any initialization logic here
    }

    function addPatient(string memory patientid ,string memory firstname , string memory lastname ,int  age,string memory maladie , string memory gender,string memory message) public {
        Patient memory p = Patient(patientid,firstname,lastname,age,maladie,gender,message);
        Patients[patientid] = p;
        patientIDs.push(patientid);
    }




    function getPatientInfos(string memory patientId) public view returns (Patient memory){
        return Patients[patientId];
    }
    // Déclaration d'un événement qui émet les informations d'un patient mis à jour
    event PatientUpdated(string patientid, string newfirstname, string newlastname, int newage, string newmaladie, string newmessage);

    function updatePatient(string memory patientid ,string memory newfirstname , string memory newlastname ,int  newage,string memory newmaladie ,string memory newmessage) public returns (bool) {
        Patient memory p = Patients[patientid];
        p.message = newmessage;
        p.age = newage;
        p.First_Name = newfirstname;
        p.Last_Name = newlastname;
        p.maladie = newmaladie;
        Patients[patientid] = p;
        // Émission de l'événement
        emit PatientUpdated(patientid, newfirstname, newlastname, newage, newmaladie, newmessage);
        // Vérification de la condition postérieure: les informations ont été mises à jour correctement
        assert(Patients[patientid].age == newage);
    return true;
    }


    function getAllPatients() public returns (string[] memory) {

    for (uint i = 0; i < patientIDs.length; i++) {
        // Get the patient ID
        string memory patientId = patientIDs[i];
        // Get the patient details from the mapping
        Patient memory patient = Patients[patientId];
        // Add the patient to the array
        patients.push(patient);
        
    }
    // Return the array of patients
    return patientIDs;
}
}

```