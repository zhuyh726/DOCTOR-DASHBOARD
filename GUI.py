import tkinter as tk
from tkinter import messagebox

# 数据类：医生类
class Doctor:
    def __init__(self, name, specialty, hospital, schedule):
        self.name = name
        self.specialty = specialty
        self.hospital = hospital
        self.schedule = schedule
        self.patients = []  # 病人列表

    def add_patient(self, patient_name):
        self.patients.append(patient_name)

    def remove_patient(self, patient_name):
        if patient_name in self.patients:
            self.patients.remove(patient_name)
        else:
            return "Patient not found!"

    def get_schedule(self):
        return self.schedule

# GUI类：医生仪表板
class DoctorDashboard:
    def __init__(self, root, doctor):
        self.root = root
        self.root.title(f"Doctor Dashboard - {doctor.name}")
        self.doctor = doctor

        # 创建标签和显示信息
        self.label_name = tk.Label(root, text=f"Doctor: {doctor.name}", font=('Arial', 14))
        self.label_name.pack(pady=5)

        self.label_specialty = tk.Label(root, text=f"Specialty: {doctor.specialty}", font=('Arial', 12))
        self.label_specialty.pack(pady=5)

        self.label_hospital = tk.Label(root, text=f"Hospital: {doctor.hospital}", font=('Arial', 12))
        self.label_hospital.pack(pady=5)

        self.label_schedule = tk.Label(root, text=f"Schedule: {doctor.get_schedule()}", font=('Arial', 12))
        self.label_schedule.pack(pady=5)

        # 病人管理区域
        self.label_patients = tk.Label(root, text="Patients", font=('Arial', 12))
        self.label_patients.pack(pady=10)

        self.patient_listbox = tk.Listbox(root, height=6, width=50)
        self.patient_listbox.pack(pady=10)
        self.update_patient_list()

        # 输入框和按钮
        self.entry_patient = tk.Entry(root, width=40)
        self.entry_patient.pack(pady=5)

        self.add_patient_button = tk.Button(root, text="Add Patient", command=self.add_patient)
        self.add_patient_button.pack(pady=5)

        self.remove_patient_button = tk.Button(root, text="Remove Patient", command=self.remove_patient)
        self.remove_patient_button.pack(pady=5)

    # 更新病人列表显示
    def update_patient_list(self):
        self.patient_listbox.delete(0, tk.END)
        for patient in self.doctor.patients:
            self.patient_listbox.insert(tk.END, patient)

    # 添加病人
    def add_patient(self):
        patient_name = self.entry_patient.get()
        if patient_name:
            self.doctor.add_patient(patient_name)
            self.update_patient_list()
            self.entry_patient.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a patient's name.")

    # 移除病人
    def remove_patient(self):
        patient_name = self.entry_patient.get()
        if patient_name:
            result = self.doctor.remove_patient(patient_name)
            if result == "Patient not found!":
                messagebox.showerror("Error", result)
            else:
                self.update_patient_list()
                self.entry_patient.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a patient's name to remove.")

# 运行GUI
if __name__ == "__main__":
    doctor = Doctor(name="Dr. John Doe", specialty="Cardiology", hospital="Heart Clinic", schedule="Mon-Fri 9 AM - 5 PM")
    root = tk.Tk()
    dashboard = DoctorDashboard(root, doctor)
    root.mainloop()
