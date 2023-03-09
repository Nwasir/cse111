# STRETCH1: In the United States, mailing addresses are supposed to be written
# in this form: number street, city, state zipcode
# For example: 525 S Center St, Rexburg, ID 83460
# write a test function named test_extract_city that
# verifies that the extract_city function works correctly.

# STRETCH2: Write a test function named test_extract_state that verifies that
# the extract_state function works correctly.

# STRETCH3: Write a test function named test_extract_zipcode that verifies that
# the extract_zipcode function works correctly.

# 525 S Center St, Rexburg, ID 83460
# 24305 Town Center Dr, Santa Clarita, CA 91355

from address import extract_city, extract_state, extract_zipcode
import pytest


def test_extract_city():
    """ Verify that the extract_city
    function returns correct results.

    Parameters: none
    Return: nothing"""
    full_address = "525 S Center St, Rexburg, ID 83460"
    assert extract_city(full_address) == "Rexburg"

    full_address = "24305 Town Center Dr, Santa Clarita, CA 91355"
    assert extract_city(full_address) == "Santa Clarita"


def test_extract_state():
    """ Verify that the extract_state
    function returns correct results.

    Parameters: none
    Return: nothing"""
    full_address = "525 S Center St, Rexburg, ID 83460"
    assert extract_state(full_address) == "ID"

    full_address = "24305 Town Center Dr, Santa Clarita, CA 91355"
    assert extract_state(full_address) == "CA"


def test_extract_zipcode():
    """ Verify that the extract_zipcode
    function returns correct results.

    Parameters: none
    Return: nothing"""
    full_address = "525 S Center St, Rexburg, ID 83460"
    assert extract_zipcode(full_address) == "83460"

    full_address = "24305 Town Center Dr, Santa Clarita, CA 91355"
    assert extract_zipcode(full_address) == "91355"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
