import csv
import warnings

class Patient: 

    all_patients = []

    def __init__(self, DonorID, ABeta40: float , ABeta42: float, tTau: float, pTau: float):

        self.DonorID = DonorID
        self.ABeta40 = ABeta40
        self.ABeta42 = ABeta42
        self.tTau = tTau
        self.pTau = pTau
        self.sex = None
        self.death_age = None
        self.ed_lvl = None
        self.cog_stat = None
        self.age_symp_on = None
        self.age_diag = None 
        self.head_inj = None
        self.thal_score = None
        Patient.all_patients.append(self)

    def __repr__(self):
        return f"{self.DonorID} | sex: {self.sex} | ABeta40 {self.ABeta40} | tTau {self.tTau} | pTau {self.pTau} | Death Age {self.death_age} | Thal Score {self.thal_score}"


    def get_id(self):
        return self.DonorID

    @classmethod
    def combine_data(cls, filename: str):
            with open(filename, encoding="utf8") as f:
                reader = csv.DictReader(f)
                rows_of_patients = list(reader)
                #for line in csv create object
                for row in range(len(rows_of_patients)):
                    if Patient.all_patients[row].DonorID == rows_of_patients[row]["Donor ID"]:
                        Patient.all_patients[row].sex = rows_of_patients[row]["Sex"]
                        Patient.all_patients[row].death_age = rows_of_patients[row]["Age at Death"]
                        Patient.all_patients[row].ed_lvl = rows_of_patients[row]["Highest level of education"]
                        Patient.all_patients[row].cog_stat = rows_of_patients[row]["Cognitive Status"]
                        Patient.all_patients[row].age_symp_on = rows_of_patients[row]["Age of onset cognitive symptoms"]
                        Patient.all_patients[row].age_diag = rows_of_patients[row]["Age of Dementia diagnosis"]
                        Patient.all_patients[row].head_inj = rows_of_patients[row]["Known head injury"]
                        Patient.all_patients[row].thal_score = rows_of_patients[row]["Thal"]
                    else:
                        warnings.warn("IDs do not match.")
   
    @classmethod
    def instantiate_from_csv(cls, filename: str, other_file: str):
    #open csv and create list of all rows
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)
            rows_of_patients = list(reader)
            #for line in csv create object
            for row in rows_of_patients:
                Patient(
                    DonorID = row['Donor ID'],
                    ABeta40 = row['ABeta40 pg/ug'],
                    ABeta42 = row['ABeta42 pg/ug'],
                    tTau = row['tTAU pg/ug'],
                    pTau = row['pTAU pg/ug']
                )
            Patient.all_patients.sort(key = Patient.get_id)
            Patient.combine_data(other_file)
  