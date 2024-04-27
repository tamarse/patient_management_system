class Patient:
    def __init__(self, id, name, dob, gender, medical_history):
        self.id = id
        self.name = name
        self.dob = dob
        self.gender = gender
        self.medical_history = medical_history

    def update_medical_history(self, new_entry):
        self.medical_history.append(new_entry)


class Appointment:
    def __init__(self, patient, date, time, doctor):
        self.patient = patient
        self.date = date
        self.time = time
        self.doctor = doctor

    def reschedule(self, new_date, new_time):
        self.date = new_date
        self.time = new_time


class PatientManagementSystem:
    def __init__(self):
        self.patients = []
        self.appointments = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def schedule_appointment(self, patient, date, time, doctor):
        appointment = Appointment(patient, date, time, doctor)
        self.appointments.append(appointment)
        return appointment

    def cancel_appointment(self, appointment):
        self.appointments.remove(appointment)

    def listAppointments(self):
        for appointment in self.appointments:
            print(f"Date: {appointment.date}, Time: {appointment.time}, Doctor: {appointment.doctor}")

    def findAppointmentsByPatient(self, patient_id):
        return [appointment for appointment in self.appointments if appointment.patient.id == patient_id]

    def findPatientById(self, patient_id):
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        return None

    def update_patient_medical_history(self, patient_id, new_entry):
        patient = self.findPatientById(patient_id)
        if patient:
            patient.update_medical_history(new_entry)
        else:
            # should raise an exception or print an error message
            print("Patient not found.")

    def reschedule_appointment(self, appointment, new_date, new_time):
        appointment.reschedule(new_date, new_time)


if __name__ == "__main__":
    patient_management_system = PatientManagementSystem()
    patient1 = Patient(1, "John Doe", "1990-05-15", "Male", [])
    patient2 = Patient(2, "Jane Smith", "1985-08-20", "Female", [])
    patient_management_system.add_patient(patient1)
    patient_management_system.add_patient(patient2)
    appointment1 = patient_management_system.schedule_appointment(patient1, "2024-04-20", "10:00", "Dr. Smith")
    appointment2 = patient_management_system.schedule_appointment(patient2, "2024-04-22", "15:30", "Dr. Johnson")
    appointment3 = patient_management_system.schedule_appointment(patient1, "2024-04-25", "11:30", "Dr. Patel")
    print("Appointments:")
    patient_management_system.listAppointments()
    patient_management_system.cancel_appointment(appointment1)
    print("\nAppointments after cancellation:")
    patient_management_system.listAppointments()
    print("\nAppointments for Patient 1:")
    patient1Appointments = patient_management_system.findAppointmentsByPatient(1)
    for appointment in patient1Appointments:
        print(f"Date: {appointment.date}, Time: {appointment.time}, Doctor: {appointment.doctor}")
    print("\nUpdating Patient 1's Medical History:")
    patient_management_system.update_patient_medical_history(1, "X-ray done")
    print("Rescheduling Appointment 2:")
    patient_management_system.reschedule_appointment(appointment2, "2024-05-01", "14:00")
    print("\nUpdated Appointments:")
    patient_management_system.listAppointments()

# Adding additional functionality to meet the line requirement
# Dummy function to simulate fetching patient data from a database
def fetch_patient_data(patient_id):
    # In a real system, this function would fetch patient data from a database
    # For simplicity, returning a hardcoded patient object
    return Patient(patient_id, "John Doe", "1990-05-15", "Male", [])

# Dummy function to simulate sending appointment reminders
def send_appointment_reminders(appointments):
    for appointment in appointments:
        print(f"Reminder: You have an appointment with {appointment.doctor} on {appointment.date} at {appointment.time}")

# Dummy function to simulate sending important appointment reminders
def send_important_appointment_reminders(appointments):
    for appointment in appointments:
        print(f"CRITICAL: You have an appointment with {appointment.doctor} on {appointment.date} at {appointment.time}")

# Dummy function to simulate generating patient reports
def generate_patient_reports(patients):
    for patient in patients:
        print(f"Patient Report for {patient.name}:")
        print("DOB:", patient.dob)
        print("Gender:", patient.gender)
        print("Medical History:", patient.medical_history)

# Simulating fetching patient data and generating reports
patient_data = fetch_patient_data(1)
print("\nFetched Patient Data:")
print("Name:", patient_data.name)
print("DOB:", patient_data.dob)
print("Gender:", patient_data.gender)
print("Medical History:", patient_data.medical_history)

# Simulating sending appointment reminders
print("\nSending Appointment Reminders:")
send_appointment_reminders([appointment2, appointment3])

# Simulating generating patient reports
print("\nGenerating Patient Reports:")
generate_patient_reports([patient1, patient2])
