from dataclasses import dataclass
from typing import List

@dataclass
class Doctor:
    name: str
    specialty: str
    hospital: str
    schedule: str
    patients: List[str] = None  # 用一个默认的空列表来存储病人

    def __post_init__(self):
        if self.patients is None:
            self.patients = []  # 确保如果没有提供病人列表，则默认为空列表

    def add_patient(self, patient_name: str):
        self.patients.append(patient_name)

    def get_schedule(self):
        return self.schedule
