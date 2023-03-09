import pytest
from ot import take_input


def test_input():
    assert take_input(3) == 15
    

def test_input2():
    assert take_input(3.1)  == -1
    
pytest.main(["-v", "--tb=line", "-rN", __file__])