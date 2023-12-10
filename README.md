# HealthCare-3.0
Le patient est supervisé par le réseau médical (à distance). A chaque intervalle de temps, une mise à jour de l’état du patient se fait. Utilisez la technologie Blockchain pour assurer la traçabilité des différentes mises à jour et qui pourrait voir ces mises à jour.



### Remix Solidity IDE (https://remix.ethereum.org/)
## Smart Contarct
```solidity
// SPDX-License-Identifier: GPL-3.0

pragma solidity >=0.8.2 <0.9.0;
contract PatientContract {
    struct Update {
        string message;
        uint256 timestamp;
    }

    mapping(string => Update[]) public patientUpdates;

    // Constructor to initialize the contract
    constructor() {
        // You can add any initialization logic here
    }

    function updatePatient(string memory patientId, string memory updateMessage) public returns (bool) {
        tryUpdatePatient(patientId, updateMessage);
        return true;
    }

    function tryUpdatePatient(string memory patientId, string memory updateMessage) internal {
        // Manually set a gas limit, adjust as needed
        uint256 gasLimit = 2000000;

        // Estimate gas consumption for the updatePatientInternal function
        uint256 gasEstimation = gasleft();
        updatePatientInternal(patientId, updateMessage);
        gasEstimation = gasEstimation - gasleft();

        // Check if gas consumption is below the specified limit
        require(gasEstimation <= gasLimit, "Gas limit exceeded");

        // Update patient with the actual gas limit
        updatePatientInternal(patientId, updateMessage);
    }

    function updatePatientInternal(string memory patientId, string memory updateMessage) internal {
        Update memory newUpdate = Update({
            message: updateMessage,
            timestamp: block.timestamp
        });
        patientUpdates[patientId].push(newUpdate);
    }

    function getPatientUpdatesCount(string memory patientId) public view returns (uint256) {
        return patientUpdates[patientId].length;
    }
}
```