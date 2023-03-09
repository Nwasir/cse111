
from clothes import read_file
from os import path
from tempfile import mktemp
from pytest import approx
import pytest


def test_file():
    """Verify that the read_file function works correctly.
    Parameters: none
    Return: nothing
    """
    CLOTHES_INDEX_NUM = 0

    # Verify that the read_file function uses its filename
    # parameter by doing the following:
    # 1. Get a filename for a file that doesn't exist.
    # 2. Call the read_file function with the filename.
    # 3. Verify that the open function inside the read_file
    #    function raises a FileNotFoundError.
    filename = mktemp(dir=".", prefix="not", suffix=".csv")
    with pytest.raises(FileNotFoundError):
        read_file(filename, CLOTHES_INDEX_NUM)
        pytest.fail("read_file function must use its filename parameter")

    # Call the read_file function and store the returned
    # dictionary in a variable named clothe_dict.
    filename = path.join(path.dirname(__file__), "clothes.csv")
    clothe_dict = read_file(filename, CLOTHES_INDEX_NUM)

    # Verify that the read_dict function returns a dictionary.
    assert isinstance(clothe_dict, dict), \
        "read_dict function must return a dictionary:" \
        f" expected a dictionary but found a {type(clothe_dict)}"

    # Verify that the products dictionry contains exactly 10 items.
    length = len(clothe_dict)
    exp_len = 10
    assert length == exp_len, \
        "products dictionary has too" \
        f" {'few' if length < exp_len else 'many'} items:" \
        f" expected {exp_len} but found {length}"

    # Check each item in the clothes dictionary.
    check_clothes(clothe_dict, "top1", ["senator", 55])
    check_clothes(clothe_dict, "top2", ["etibor", 50])
    check_clothes(clothe_dict, "top3", ["elliot", 45])
    check_clothes(clothe_dict, "top4", ["danshiki", 40])
    check_clothes(clothe_dict, "top5", ["agbada", 50])
    check_clothes(clothe_dict, "top6", ["isi agu", 60])
    check_clothes(clothe_dict, "top7", ["jonathan", 40])
    check_clothes(clothe_dict, "top8", ["shirts", 30])
    check_clothes(clothe_dict, "top9", ["trousers", 30])
    check_clothes(clothe_dict, "top10", ["shorts", 25])
       

def check_clothes(clothes_dict, clothes_name, expected_value):
    """Verify that the data for one clothe number stored in the
    clothe dictionary is correct.

    Parameters
        clothe_dict: a dictionary that contains clothes data
        clothe_number: the clothe number of the clothes that this
            function will verify
        expected_value: the data that should be in the clothes
            dictionary for the clothe_number
    Return: nothing
    """
    assert clothes_name in clothes_dict
    actual_value = clothes_dict[clothes_name]
    length = len(actual_value)
    min_len = 2
    max_len = 3
    assert min_len <= length and length <= max_len, \
        f"value list for product {clothes_name} contains too" \
        f" {'few' if length < min_len else 'many'} elements:" \
        f" expected {min_len} or {max_len} elements but found {length}"

    if length == min_len:
        NAME_INDEX = 0
        PRICE_INDEX = 1
    else:
        NAME_INDEX = 1
        PRICE_INDEX = 2

   # Verify that the clothes name is correct.
    act_name = actual_value[NAME_INDEX]
    exp_name = expected_value[0]
    assert act_name == exp_name, \
        f"wrong name for product {clothes_name}: " \
        f"expected {exp_name} but found {act_name}"

    # Verify that the clothes price is correct.
    act_price = actual_value[PRICE_INDEX]
    if isinstance(act_price, str):
        act_price = float(act_price)
    exp_price = expected_value[1]
    assert act_price == approx(exp_price), \
        f"wrong price for clothes {clothes_name}: " \
        f"expected {exp_price} but found {act_price}"


# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
