contract_abi =  [
	{
		"inputs": [],
		"stateMutability": "nonpayable",
		"type": "constructor"
	},
	{
		"anonymous": "false",
		"inputs": [
			{
				"indexed": "false",
				"internalType": "string",
				"name": "patientid",
				"type": "string"
			},
			{
				"indexed": "false",
				"internalType": "string",
				"name": "newfirstname",
				"type": "string"
			},
			{
				"indexed": "false",
				"internalType": "string",
				"name": "newlastname",
				"type": "string"
			},
			{
				"indexed": "false",
				"internalType": "int256",
				"name": "newage",
				"type": "int256"
			},
			{
				"indexed": "false",
				"internalType": "string",
				"name": "newmaladie",
				"type": "string"
			},
			{
				"indexed": "false",
				"internalType": "string",
				"name": "newmessage",
				"type": "string"
			}
		],
		"name": "PatientUpdated",
		"type": "event"
	},
	{
		"inputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"name": "Patients",
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
		"inputs": [],
		"name": "getAllPatients",
		"outputs": [
			{
				"internalType": "string[]",
				"name": "",
				"type": "string[]"
			}
		],
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
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "patientIDs",
		"outputs": [
			{
				"internalType": "string",
				"name": "",
				"type": "string"
			}
		],
		"stateMutability": "view",
		"type": "function"
	},
	{
		"inputs": [
			{
				"internalType": "uint256",
				"name": "",
				"type": "uint256"
			}
		],
		"name": "patients",
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
				"name": "patientid",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "newfirstname",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "newlastname",
				"type": "string"
			},
			{
				"internalType": "int256",
				"name": "newage",
				"type": "int256"
			},
			{
				"internalType": "string",
				"name": "newmaladie",
				"type": "string"
			},
			{
				"internalType": "string",
				"name": "newmessage",
				"type": "string"
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