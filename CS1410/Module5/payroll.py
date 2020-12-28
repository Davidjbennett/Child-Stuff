from abc import ABC, abstractmethod
import os, os.path, shutil

PAY_LOGFILE = "paylog.txt"
Employees = []

class Employee:
    def __init__(self, emp_id, first_name, last_name,address, city, state, zipcode):
        self.emp_id = emp_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.classification = None

    def make_hourly(self, rate):
        self.classification = Hourly(rate)
    
    def make_commissioned(self, salary, commission_rate):
        self.classification = Commissioned(salary,commission_rate)
    
    def make_salaried(self, salary):
        self.classification = Salary(salary)

    def issue_payment(self):
        with open(PAY_LOGFILE, 'a') as f:
            name = self.first_name + " " + self.last_name
            addr = self.address
            city = self.city
            state = self.state
            zipcode = self.zipcode
            amount = f'{self.classification.compute_pay()}'
            print("Mailing",amount,"to",name,"at",addr,city,state,zipcode,file=f)
class Classification:
    def __init__(self):
        pass

    @abstractmethod
    def compute_pay(self):
        pass

class Salary(Classification):
    def __init__(self, salary):
        self.salary = float(salary)

    def compute_pay(self):
        return round(self.salary / 24, 2)

class Commissioned(Classification):
    def __init__(self, salary, commission_rate):
        self.salary = salary
        self.commission_rate = commission_rate
        self.receipts = []
    
    def add_receipt(self, reciept_list):
        self.receipts.append(reciept_list)

    def compute_pay(self):
        total_receipts = 0
        for receipt in self.receipts:
            total_receipts += receipt
        self.receipts = []
        return round(self.salary/24 + (total_receipts * self.commission_rate/100), 2)
class Hourly(Classification):
    def __init__(self,hourly_rate):
        self.hourly_rate = hourly_rate
        self.timecard = []

    def add_timecard(self, card):
        self.timecard.append(card)
    
    def compute_pay(self):
        total_hours_worked = 0
        for hours in self.timecard:
            total_hours_worked += hours
        self.timecard = []
        return round(total_hours_worked * self.hourly_rate, 2)


def load_employees():
    with open("employees.csv", "r") as reader:
        reader.readline()

        while reader:
            emp = reader.readline().strip().split(',')
            if emp[0] == '':
                return
            new_emp = Employee(emp[0],emp[1],emp[2],emp[3],emp[4],emp[5],emp[6])
            if emp[7] == "3":
                new_emp.make_hourly(float(emp[10]))
            elif emp[7] == "2":
                new_emp.make_commissioned(float(emp[8]),float(emp[9]))
            else:
                new_emp.make_salaried(float(emp[8]))
            
            if new_emp not in Employees:
                Employees.append(new_emp)

def process_timecards():
    with open("timecards.csv", "r") as tc:
        while tc:
            timecard = tc.readline().strip('\n').split(',')
            emp = find_employee_by_id(timecard[0])

            if emp is None:
                return
            if isinstance(emp.classification, Hourly):
                for hours in range(1, len(timecard)-1):
                    emp.classification.add_timecard(float(hours))
                    
def process_receipts():
    with open("receipts.csv", "r") as tc:

       while tc:
            receipts = tc.readline().strip('\n').split(',')
            emp = find_employee_by_id(receipts[0])

            if emp is None:
                return 
            if isinstance(emp.classification, Commissioned):
                for hours in range(1, len(receipts)-1):
                    emp.classification.add_receipt(float(hours))
      
def run_payroll():
    if os.path.exists(PAY_LOGFILE):
        os.remove(PAY_LOGFILE)
    for emp in Employees:
        emp.issue_payment()

def find_employee_by_id(id):
    for emp in Employees:
        if id == emp.emp_id:
            return emp


