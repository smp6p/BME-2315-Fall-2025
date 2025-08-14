import csv 
import warnings

class Patient:

    all_patients = []

    def __init__(self, id: str, ABeta40: float, ABeta42 :float, tTAU: float, pTAU: float):
        self.id = id
        self.ABeta40 = ABeta40
        self.ABeta42 = ABeta42
        self.tTAU = tTAU
        self.pTAU = pTAU
        self.sex = None
        self.age = None
        Patient.all_patients.append(self)

    def __repr__(self):
        return f"ID: {self.id} | {self.sex} {self.age}yr old"

    def get_id(self):
        return self.id

        
    @classmethod
    def combine_data(cls, filename: str):
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            #for line in csv create object
            for row in range(len(rows)):
                if Patient.all_patients[row].id == rows[row]["\ufeffID"]:
                    Patient.all_patients[row].sex = rows[row]["Sex"]
                    Patient.all_patients[row].age = rows[row]["Age at Death"]
                else:
                    warnings.warn("IDs do not match") 

    @classmethod
    def instantiate_from_csv(cls, filename: str, other_file:str):
        #open csv and create list of all rows
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows = list(reader)
            #for line in csv create object
            for row in rows:
                Patient(
                    id = row["\ufeffID"],
                    ABeta40 = row['ABeta40 pg/ug'],
                    ABeta42 = row["ABeta42 pg/ug"],
                    tTAU = row["tTAU pg/ug"],
                    pTAU = row["pTAU pg/ug"]
                )
            Patient.all_patients.sort(key = Patient.get_id)
            Patient.combine_data(other_file)
            
