
from abc import ABC, abstractmethod

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
        self.classification = Salaried(salary)

    def make_commissioned(self, commission, salary):
        self.classification = Commissioned(commission,salary)
    
    def issue_payment(self):
        self.compute_pay()

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
        return round(total_hours_worked * self.hourly_rate, 2)

class Salaried(Classification):
    def __init__(self, salary):
        self.salary = salary

    def compute_pay(self):
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
        return round(self.salary/24 + commission ,2)

    