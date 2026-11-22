from grade_calculator import average, grade, is_pass, highest_mark

def test_average():
    assert average([80, 90, 70]) == 80

def test_grade_a():
    assert grade(95) == "A"

def test_grade_b():
    assert grade(80) == "B"

def test_grade_c():
    assert grade(65) == "C"

def test_grade_f():
    assert grade(25) == "F"

def test_pass():
    assert is_pass([80, 75, 90]) == True

def test_fail():
    assert is_pass([80, 30, 90]) == False

def test_highest_mark():
    assert highest_mark([80, 95, 70]) == 95