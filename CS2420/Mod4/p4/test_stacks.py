import unittest
from stack import Stack
from main import eval_postfix as epf
from main import in2post as i2p
from main import main as mn
import io
import sys

class TestStack(unittest.TestCase):
    def test_stack_creation(self):
        stk = Stack()
        self.assertEqual(stk.size(), 0)
        self.assertRaises(IndexError, stk.pop)

    def test_stack_push_pop(self):
        stk = Stack()
        stk.push(1)
        stk.push(3.14)
        stk.push("cat")
        self.assertEqual(stk.size(), 3)
        self.assertEqual(stk.top(), "cat")
        self.assertEqual(stk.size(), 3)
        self.assertEqual(stk.pop(), "cat")
        self.assertEqual(stk.size(), 2)
        self.assertAlmostEqual(stk.pop(), 3.14)
        self.assertEqual(stk.pop(), 1)
        self.assertEqual(stk.size(), 0)
        self.assertRaises(IndexError, stk.top)
        self.assertRaises(IndexError, stk.pop)

        for i in range(100):
            stk.push(i)
        self.assertEqual(stk.size(), 100)
        stk.clear()
        self.assertEqual(stk.size(), 0)

class TestEvaluation(unittest.TestCase):
    def test_equation_1(self):
        self.assertAlmostEqual(epf("4"), 4.0)

    def test_equation_2(self):
        self.assertAlmostEqual(epf("5 7 +"), 12.0)
        
    def test_equation_3(self):
        self.assertAlmostEqual(epf("5 7 *"), 35.0)
        
    def test_equation_4(self):
        self.assertAlmostEqual(epf("5 3 -"), 2.0)

    def test_equation_5(self):
        self.assertAlmostEqual(epf("5 5 /"), 1.0)
        
    def test_equation_6(self):
        self.assertAlmostEqual(epf("8 5 * 3 +"), 43.0)

    def test_equation_7(self):
        self.assertAlmostEqual(epf("8 5 3 + *"), 64.0)

    def test_equation_8(self):
        self.assertAlmostEqual(epf("8 3 5 * + 7 -"), 16.0)

    def test_equation_9(self):
        self.assertAlmostEqual(epf("8 3 + 5 6 - *"), -11.0)
        
    def test_equation_10(self):
        self.assertAlmostEqual(epf("8 3 + 2 7 - *"), -55.0)

    def test_equation_11(self):
        self.assertAlmostEqual(epf("8 3 + 2 * 7 -"), 15.0)
    
    def test_equation_12(self):
        self.assertAlmostEqual(epf("8 5 * 3 2 - 7 3 * - +"), 20.0)
    
    def test_equation_13(self):
        self.assertAlmostEqual(epf("8 5 * 3 + 7 - 5 3 * -"), 21.0)

    def test_equation_14(self):
        self.assertAlmostEqual(epf(" 7 9 * 7 + 5 6 * - 3 + 4 -"), 39.0)

    def test_bad_postfix(self):
        self.assertRaises(SyntaxError,  epf, " 7 9 * 7 + 5 6 * - 3 + 4 - +")
        self.assertRaises(ValueError, epf, [None])

class TestIn2Postfix(unittest.TestCase):
    def test_infix_1(self):
        postfix = i2p("4")
        self.assertEqual(postfix.replace(" ", ""), "4")
    def test_infix_2(self):
        postfix = i2p("5 + 7")
        self.assertEqual(postfix.replace(" ", ""), "5 7 +".replace(" ", ""))
    def test_infix_3(self):
        postfix = i2p("7 * 5")
        self.assertEqual(postfix.replace(" ", ""), "7 5 *".replace(" ", ""))
    def test_infix_4(self):
        postfix = i2p("( 5 - 3 )")
        self.assertEqual(postfix.replace(" ", ""), "5 3 -".replace(" ", ""))
    def test_infix_5(self):
        postfix = i2p("5 / 5")
        self.assertEqual(postfix.replace(" ", ""), "5 5 /".replace(" ", ""))
    def test_infix_6(self):
        postfix = i2p("8 * 5 + 3")
        self.assertEqual(postfix.replace(" ", ""), "8 5 * 3 +".replace(" ", ""))
    def test_infix_7(self):
        postfix = i2p("8 * ( 5 + 3 )")
        self.assertEqual(postfix.replace(" ", ""), "8 5 3 + *".replace(" ", ""))
    def test_infix_8(self):
        postfix = i2p("8 + 3 * 5 - 7")
        self.assertEqual(postfix.replace(" ", ""), "8 3 5 * + 7 -".replace(" ", ""))
    def test_infix_9(self):
        postfix = i2p("( 8 + 3 ) * ( 5 - 6 )")
        self.assertEqual(postfix.replace(" ", ""), "8 3 + 5 6 - *".replace(" ", ""))
    def test_infix_10(self):
        postfix = i2p("( ( 8 + 3 ) * ( 2 - 7 ) )")
        self.assertEqual(postfix.replace(" ", ""), "8 3 + 2 7 - *".replace(" ", ""))
    def test_infix_11(self):
        postfix = i2p("( ( 8 + 3 ) * 2 ) - 7")
        self.assertEqual(postfix.replace(" ", ""), "8 3 + 2 * 7 -".replace(" ", ""))
    def test_infix_12(self):
        postfix = i2p("( 8 * 5 ) + ( ( 3 - 2 ) - 7 * 3 )")
        self.assertEqual(postfix.replace(" ", ""), "8 5 * 3 2 - 7 3 * - +".replace(" ", ""))
    def test_infix_13(self):
        postfix = i2p("( ( 8 * 5 + 3 ) - 7 ) - ( 5 * 3 )")
        self.assertEqual(postfix.replace(" ", ""), "8 5 * 3 + 7 - 5 3 * -".replace(" ", ""))
    def test_infix_14(self):
        postfix = i2p("7 * 9 + 7 - 5 * 6 + 3 - 4")
        self.assertEqual(postfix.replace(" ", ""), "7 9 * 7 + 5 6 * - 3 + 4 -".replace(" ", ""))
    def test_infix_bad_expression(self):
        self.assertRaises(SyntaxError, i2p, "( 8 + 3 ) * ( 5 - 6 ) )")
    def test_infix_bad_param(self):
        self.assertRaises(ValueError, i2p, [None])

class TestCodingStandards(unittest.TestCase):
    def test_code_quality(self):
        from pylint import epylint as lint
        (pylint_stdout, _) = lint.py_run("main.py", return_std=True)
        output = pylint_stdout.getvalue()
        offset = output.rfind(" been rated at ")
        if offset != -1:
            output = output[offset:]
            end = output.find('/')
            output = output[15:end]
            score = float(output)
            self.assertGreaterEqual(score, 8.5)
        (pylint_stdout, _) = lint.py_run("stack.py", return_std=True)
        output = pylint_stdout.getvalue()
        offset = output.rfind(" been rated at ")
        if offset != -1:
            output = output[offset:]
            end = output.find('/')
            output = output[15:end]
            score = float(output)
            self.assertGreaterEqual(score, 8.5)


