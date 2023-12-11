contract_abi =  [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "patientid",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "firstname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "lastname",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "age",
				"type": "int256"
			},
			{
				"internalType": "string",
				"name": "maladie",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "gender",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "message",
				"type": "string"
			}
		],
		"name": "addPatient",
		"outputs": [],
		"stateMutability": "nonpayable",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "patientId",
				"type": "string"
			}
		],
		"name": "getPatientInfos",
		"outputs": [
			{
				"components": [
					{
						"internalType": "string",
						"name": "PatientId",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "First_Name",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "Last_Name",
						"type": "string"
					},
					{
						"internalType": "int256",
						"name": "age",
						"type": "int256"
					},
					{
						"internalType": "string",
						"name": "maladie",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "gender",
						"type": "string"
					},
					{
						"internalType": "string",
						"name": "message",
						"type": "string"
					}
				],
				"internalType": "struct PatientContract.Patient",
				"name": "",
				"type": "tuple"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "patientUpdates",
		"outputs": [
			{
				"internalType": "string",
				"name": "PatientId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "First_Name",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "Last_Name",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "age",
				"type": "int256"
			},
			{
				"internalType": "string",
				"name": "maladie",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "gender",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "message",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "patientId",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "updateMessage",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "newage",
				"type": "int256"
			}
		],
		"name": "updatePatient",
		"outputs": [
			{
				"internalType": "bool",
				"name": "",
				"type": "bool"
			}
		],
		"stateMutability": "nonpayable",
		"type": "function"
	}
]