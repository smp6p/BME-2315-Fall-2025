from patient import Patient

Patient.instantiate_from_csv("luminex_data.csv","metadata.csv")

for patient in Patient.all_patients:
    print(patient)