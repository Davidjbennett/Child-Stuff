
from abc import ABC, abstractmethod
import p5
import os, os.path, shutil

PAY_LOGFILE = ""
employees = []

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

    def getEmp_Id(self):
        return self.emp_id

    def setClassfication(self, claass):
        self.classification = claass
    
    def getClassification(self):
        return self.classification

    def make_hourly(self, hrate):
        self.classification = Hourly(hrate)
    
    def make_salaried(self, salary):
        self.classification = Salary(salary)

    def make_commissioned(self, commission, salary):
        self.classification = Commissioned(commission,salary)
    
    def issue_payment(self):
        # s = ("Mailing "+ str(self.classification.compute_pay())+ " to "+ emp.first_name, emp.last_name, "at", emp.address, emp.city, emp.state, emp.zipcode)
        # if isinstance(self.classification, Hourly):
        #     self.classification.timecard = []

        # if isinstance(self.classification, Commissioned):
        #     self.classification.receipts = []
        
        # return s
        with open(PAY_LOGFILE, 'a') as f:
            name = self.first_name, self.last_name
            addr = self.address + " " + self.city + ", " + self.state + " " + self.zipcode
            amount = f'{self.classification.compute_pay()}'
            print("Mailing ",amount,"to",name,"at",addr)

class Classification:
    def __init__(self):
        pass

    @abstractmethod
    def compute_pay(self):
        pass

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

class Salary(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
        # with open(PAY_LOGFILE, 'a') as f:

        return round(self.salary / 24, 2)

class Commissioned(Classification):
    def __init__(self, commission_rate, salary):
        self.commission_rate = commission_rate
        self.salary = salary
        self.receipts = []
    
    def add_receipts(self, reciept_list):
        self.receipts.append(reciept_list)

    def compute_pay(self):
        commission = 0
        for x in self.receipts:
            commission += (x * (self.commission_rate/100))
        self.receipts = []
        return round(self.salary/24 + commission ,2)

    