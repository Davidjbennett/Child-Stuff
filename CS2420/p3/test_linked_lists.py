import random
import io
import sys
import pytest
import math
from course import Course
from courselist import CourseList
from main import main as mn


def test_course_creation():
    # make sure that an empty course is correct
    c = Course()
    assert c.name() == ""
    c.number() == 0 
    assert c.credit_hr() == 0.0
    assert c.grade() == 0.0
    assert c.next == None

def test_course_creation_with_parameters():
    c = Course(1234, "Test Name", 3.0, 3.72)
    assert c.number() == 1234
    assert c.name() == "Test Name"
    assert c.credit_hr() == 3.0
    assert c.grade() == 3.72
    assert c.next == None

    with pytest.raises(ValueError):
        Course("cat")
    with pytest.raises(ValueError):
        Course(1234, None)
    with pytest.raises(ValueError):
        Course(1234, "Test Name", "cat")
    with pytest.raises(ValueError):
        Course(1234, "Test Name", 3.0, "cat")
    with pytest.raises(ValueError):
        Course(-1)
    with pytest.raises(ValueError):
        Course(1234, "Test Name", -2.1)
    with pytest.raises(ValueError):
        Course(1234, "Test Name", 0.0, -2.0)


def test_empty_courselist():
    cl = CourseList()
    assert cl.head == None
    assert cl.size() == 0
    assert cl.calculate_gpa() == 0.0
    assert cl.calculate_gpa() == 0.0
    assert cl.is_sorted()

def test_insert():
    random.seed(0)
    cl = CourseList()
    for _ in range(37):
        cl.insert(Course(random.randrange(1000, 7000), "test", 1.0, 2.0))

    assert cl.size() == 37
    assert cl.is_sorted()

def test_remove():
    random.seed(0)
    cl = CourseList()
    courseNumbers = []
    for _ in range(37):
        courseNumbers.append(random.randrange(1000, 7000))
    for number in courseNumbers:
        cl.insert(Course(number, "test", 1.0, 2.0))

    course = cl.find(courseNumbers[0])
    assert course.number() == courseNumbers[0]
    course = cl.find(courseNumbers[10])
    assert course.number() == courseNumbers[10]
    course = cl.find(courseNumbers[36])
    assert course.number() == courseNumbers[36]

    for i in range(0, 30, 3):
        cl.remove(courseNumbers[i])

    assert cl.size() == 27
    assert cl.is_sorted()

def test_remove_all():
    cl = CourseList()
    cl.insert(Course(1000))
    for _ in range(20):
        cl.insert(Course(1200))
    cl.insert(Course(1800))
    assert cl.size() == 22
    cl.remove_all(1200)
    assert cl.size() == 2


def test_gpa():
    random.seed(0)
    cl = CourseList()
    total_credits = 0.0
    total_grade_points = 0.0
    for _ in range(10):
        credits = random.uniform(1.0, 5.0)
        grade = random.uniform(0.0, 4.0)
        total_credits += credits
        total_grade_points += credits * grade
        cl.insert(Course(1234, "Test", credits, grade))

    assert math.isclose(cl.calculate_gpa(), total_grade_points / total_credits)

def test_iterate_list():
    cl = CourseList()
    cl.insert(Course(1000))
    for _ in range(20):
        cl.insert(Course(1200))
    totalCourses = 0
    for _ in cl:
        totalCourses += 1
    assert totalCourses == 21


def test_code_quality():
    from pylint import epylint as lint
    import re
    
    (pylint_stdout, pylint_stderr) = lint.py_run('course.py', return_std=True)
    expected = 8.5
    actual = pylint_stdout.getvalue()
    x = re.findall('[0-9]+', actual)[0]
    x = float(x)
    assert x >= expected
    
    (pylint_stdout, pylint_stderr) = lint.py_run('courselist.py', return_std=True)
    expected = 8.5
    actual = pylint_stdout.getvalue()
    x = re.findall('[0-9]+', actual)[0]
    x = float(x)
    assert x >= expected
