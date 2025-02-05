# DOCTOR-DASHBOARD
class Patient:
    def __init__(self, name, age, diagnosis, treatment):
        self.name = name
        self.age = age
        self.diagnosis = diagnosis
        self.treatment = treatment

    def update_treatment(self, new_treatment):
        self.treatment = new_treatment

    def display_patient_info(self):
        return f"Name: {self.name}, Age: {self.age}, Diagnosis: {self.diagnosis}, Treatment: {self.treatment}"
