import unittest
from payroll import *
import os, os.path, shutil

PAY_LOGFILE = ""
Employees = []

def load_employees():
    with open("employees.csv", "r") as reader:
        reader.readline()

        while reader:
            emp = reader.readline().split(',')
            if emp[0] == '':
                return
            new_emp = Employee(emp[0],emp[1],emp[2],emp[3],emp[4],emp[5],emp[6])
            if emp[7] == "3":
                new_emp.make_hourly(emp[10])
                new_emp.setClassfication(emp[7])
            elif emp[7] == "2":
                new_emp.make_commissioned(emp[9],emp[8])
                new_emp.setClassfication(emp[7])
            else:
                new_emp.make_salaried(emp[8])
                new_emp.setClassfication(emp[7])
            
            if new_emp not in Employees:
                Employees.append(new_emp)

def process_timecards():
    with open("timecards.csv", "r") as reader:
        hours = [] 
        emphours = []       
    
        while reader:
            emphours = reader.readline().split(',')
            if emphours[0] == '':
                return

            for i in Employees:
                if emphours[0] == i.getEmp_Id():
                    if i.getClassification() == '3' :
                        i.add_timecard(emphours[1:])
                    elif i.getClassification() == '2':
                        return
                    else:
                        return
                    
def process_receipts():
    with open("receipts.csv", "r") as reader:

       while reader:
            empCommision = reader.readline().split(',')
            if empCommision[0] == '':
                return 

            for i in Employees:
                if empCommision[0] == i.getEmp_Id():
                    employee = i
                    # print(employee.getClassification())
                    # i.add_receipts(empCommision[1:])
                    

def run_payroll():
    pass

def find_employee_by_id(id):
    for i in Employees:
        if id == i.getEmp_Id():
            return i

def main():
    load_employees() # You will implement the first three of these functions
    process_timecards()
    process_receipts()
    run_payroll() # This function is given to you in Part 2

    # # Save copy of payroll file; delete old file
    # shutil.copyfile(PAY_LOGFILE, 'paylog_old.txt')
    # if os.path.exists(PAY_LOGFILE):
    #     os.remove(PAY_LOGFILE) # You define PAY_LOGFILE = ‘paylog.txt’ globally

    # # Change Issie Scholard to Salaried by changing the Employee object:
    # emp = find_employee_by_id('51-4678119')
    # emp.make_salaried(134386.51)
    # emp.issue_payment()

    # # Change Reynard,Lorenzin to Commissioned; add some receipts
    # emp = find_employee_by_id('11-0469486')
    # emp.make_commissioned(50005.50, 27)
    # clas = emp.classification
    # clas.add_receipt(1109.73)
    # clas.add_receipt(746.10)
    # emp.issue_payment()

    # # Change Jed Netti to Hourly; add some hour entries
    # emp = find_employee_by_id('68-9609244')
    # emp.make_hourly(47)
    # clas = emp.classification
    # clas.add_timecard(8.0)
    # clas.add_timecard(8.0)
    # clas.add_timecard(8.0)
    # clas.add_timecard(8.0)
    # clas.add_timecard(8.0)
    # emp.issue_payment()
    
if __name__ == '__main__':
 main()

    