
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

    def make_hourly(self, rate):
        self.classification = Hourly(rate)
    
    def make_salaried(self, rate):
        self.classification = Salaried(rate)

    def make_commisioned(self, rate):
        self.classification = Commisioned(rate)
    
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
        pass

class Commisioned(Classification):
    def __init__(self, commision_rate):
        self.commision_rate = commision_rate
        self.reciepts = []
    
    def add_reciepts(self, reciept_list):
        self.reciepts.append(reciept_list)

    def compute_pay(self):
        pass
    