class Appointment:
    def __init__(self, appointment_id, client_name, date, time, status):
        self.appointment_id = appointment_id
        self.client_name = client_name
        self.date = date
        self.time = time
        self.status = status

    def update_status(self, new_status):
        self.status = new_status

    def __str__(self):
        return f"Appointment ID: {self.appointment_id}, Client: {self.client_name}, Date: {self.date}, Time: {self.time}, Status: {self.status}"

class AppointmentSchedulingSystem:
    def __init__(self):
        self.appointments = []

    def add_appointment(self, appointment):
        self.appointments.append(appointment)

    def update_appointment_status(self, appointment_id, new_status):
        for appointment in self.appointments:
            if appointment.appointment_id == appointment_id:
                appointment.update_status(new_status)
                return f"Appointment {appointment_id} status updated to {new_status}"
        return f"Appointment {appointment_id} not found"

    def display_appointments(self):
        for appointment in self.appointments:
            print(appointment)

# Example usage
if __name__ == "__main__":
    system = AppointmentSchedulingSystem()
    appointment1 = Appointment(1, "Alice", "2023-10-01", "10:00 AM", "Scheduled")
    appointment2 = Appointment(2, "Bob", "2023-10-02", "11:00 AM", "Scheduled")

    system.add_appointment(appointment1)
    system.add_appointment(appointment2)

    system.display_appointments()

    print(system.update_appointment_status(1, "Completed"))
    system.display_appointments()