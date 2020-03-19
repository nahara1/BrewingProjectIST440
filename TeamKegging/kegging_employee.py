class Employee:
    def __init__(self, employee_id, employee_name, employee_role, employee_status, rfid):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_role = employee_role
        self.employee_status = employee_status
        self.rfid = rfid


    def __str__(self):
        return self.name