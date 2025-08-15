from patient import Patient

Patient.instantiate_from_csv('UpdatedLuminex.csv', 'UpdatedMetaData.csv')

for patient in Patient.all_patients:
    print(patient)