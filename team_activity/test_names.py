# CORE1: Declare test_make_full_name so that it tests make_full_name with
# variousnames, including long names, short names, and hyphenated names.
# Fix the mistake in the make_full_name function.
# CORE2: Declare test_extract_family_name so that it tests extract_family_name
# with various names, including long names, short names, and hyphenated names.
# CORE3: Declare test_extract_given_name so that it tests extract_given_name
# with various names, including long names, short names, and hyphenated names.
# Fix the mistake in the extract_given_name function.


from names import make_full_name, extract_family_name, extract_given_name
import pytest


def test_make_full_name():
    """Verify that the make_full_name
    function returns correct results.

    Parameters: none
    Return: nothing"""
    assert make_full_name("Sally", "Brown") == "Brown; Sally"
    assert make_full_name("Peter", "O'Brien") == "O'Brien; Peter"


def test_extract_family_name():
    """Verify that the extract_family_name
    function returns correct results.

    Parameters: none
    Return: nothing"""
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("O'Brien; Peter") == "O'Brien"


def test_extract_given_name():
    """Verify that the extract_given_name
    function returns correct results.

    Parameters: none
    Return: nothing"""
    assert extract_given_name("Brown; Sally") == "Sally"
    assert extract_given_name("O'Brien; Peter") == "Peter"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
