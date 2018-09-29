import pytest as pytest
import coding_interview.code.multiply as mp

''' 
You can just run it by going to Python Terminal 

H:\rravuri\PythonTraining\coding_interview>pytest ./test
will look for all files starting with test_*.py  or ending with *_test.py

H:\rravuri\PythonTraining\coding_interview>pytest ./test/test_multiply.py
to run a specific test program

'''

def test_multiply():
    assert mp.multiply(2, 5) == 10
    assert mp.multiply(2, 0) == 0
    assert mp.multiply(2, None) is None
    assert mp.multiply(-10, 5) == -50
    assert mp.multiply(-10, -5) == 50
    assert mp.multiply("Bad Input", 5)


def test_raises_exception_on_non_number_type_arguments():
    with pytest.raises(TypeError):
        mp.multiply("Bad Input", 5)
