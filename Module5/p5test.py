import unittest
import payroll

class P2Test(unittest.TestCase):
    def setUp(self):
        self.emp = payroll.Employee('12-3456789', 'John', 'Doe', '123 Anystreet', 'Anytown', 'Anystate', '98765')
    def testHourly(self):
        rate = 35.5
        self.emp.make_hourly(rate)
        for d in range(10):
            self.emp.classification.add_timecard(4.0 + d*0.5)
        self.assertEqual(self.emp.classification.compute_pay(), 62.5*rate)
    def testSalaried(self):
        salary = 10100.0
        self.emp.make_salaried(salary)
        self.assertEqual(self.emp.classification.compute_pay(), round(salary/24, 2))
    def testCommissioned(self):
        salary = 50000.0
        rate = 25
        self.emp.make_commissioned(salary, rate)
        for d in range(5):
            self.emp.classification.add_receipt(400.0 + d*25)
        self.assertEqual(self.emp.classification.compute_pay(), round(salary/24+2250.0*rate/100.0, 2))

if __name__ == '__main__':
    unittest.main()