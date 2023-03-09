# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
from textwrap import fill
from tkinter import N
from unicodedata import name
import itertools

NAME_INDEX = 0
GENDER_INDEX = 1
BIRTH_YEAR_INDEX = 2
DEATH_YEAR_INDEX = 3

# Each value in the marriages dictionary is a list.
# These are the indexes of the elements in those lists.
HUSBAND_KEY_INDEX = 0
WIFE_KEY_INDEX = 1
WEDDING_YEAR_INDEX = 2


def main():
    people_dict = {
        # Each item in the people dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "P". Each value is a list of data about a person.
        # Each item in the dictionary is in this format:
        # person_key: [name, gender, birth_year, death_year]
        "P143": ["Lola Park", "F", 1663, 1706],
        "P338": ["Savanna Foster", "F", 1674, 1723],
        "P201": ["Tiffany Hughes", "F", 1689, 1747],
        "P203": ["Ignacio Torres", "M", 1693, 1758],
        "P128": ["Yasmin Li", "F", 1701, 1716],
        "P342": ["Trent Ross", "M", 1705, 1757],
        "P202": ["Samyukta Nguyen", "M", 1717, 1774],
        "P132": ["Joel Johnson", "M", 1724, 1800],
        "P445": ["Whitney Nelson", "F", 1757, 1823],
        "P318": ["Khalid Ali", "M", 1759, 1814],
        "P317": ["Davina Patel", "F", 1775, 1860],
        "P313": ["Enzo Ruiz", "M", 1782, 1782],
        "P475": ["Lauren Smith", "F", 1800, 1802],
        "P455": ["Lucas Ross", "M", 1800, 1853],
        "P435": ["Jamal Gray", "M", 1810, 1831],
        "P204": ["Fatima Soares", "F", 1812, 1898],
        "P206": ["Ephraim Foster", "M", 1831, 1885],
        "P500": ["Peter Price", "M", 1832, 1878],
        "P207": ["Rosalina Jimenez", "F", 1875, 1956],
        "P425": ["Rachel Johnson", "F", 1876, 1940],
        "P121": ["Vanessa Bennet", "F", 1880, 1960],
        "P152": ["Jose Castillo", "M", 1884, 1931],
        "P205": ["Liam Myers", "M", 1902, 1950],
        "P465": ["Isabella Lopez", "F", 1907, 1959],
        "P168": ["Megan Anderson", "F", 1909, 1945]
    }

    marriages_dict = {
        # Each item in the marriages dictionary is a key value pair.
        # Each key is a unique identifier that begins with the
        # letter "M". Each value is a list of data about a marriage.
        # Each item in the dictionary is in this format:
        # marriage_key: [husband_key, wife_key, wedding_year]
        "M48": ["P203", "P201", 1711],
        "M45": ["P342", "P338", 1722],
        "M36": ["P203", "P201", 1724],
        "M47": ["P202", "P445", 1774],
        "M21": ["P132", "P445", 1775],
        "M59": ["P132", "P317", 1792],
        "M63": ["P318", "P445", 1804],
        "M12": ["P318", "P317", 1808],
        "M54": ["P435", "P204", 1830],
        "M34": ["P455", "P204", 1853],
        "M55": ["P500", "P317", 1859],
        "M52": ["P206", "P204", 1875],
        "M78": ["P152", "P121", 1905],
        "M50": ["P152", "P425", 1917],
        "M64": ["P205", "P465", 1925],
        "M62": ["P152", "P207", 1925],
        "M70": ["P152", "P168", 1928]
    }

    # Call the print_death_age function to print
    # each person's name and age at death.
    print_death_age(people_dict)

    # Print a blank line.
    print()

    # Call the count_genders function to count
    # and print the number of males and females.
    count_genders(people_dict)

    # Print a blank line.
    print()

    # Call the print_marriages function to print
    # human readable data about the marriages.
    print_marriages(marriages_dict, people_dict)

    # Print a blank line.
    print()

    # Call the count_marriages function to print
    # the number of times each persons got married, and
    # the person with the highest number of time.
    count_marriages(people_dict, marriages_dict) 


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    print('Age at death')
    for values in people_dict.values():
        birth_y = values[BIRTH_YEAR_INDEX]
        death_y = values[DEATH_YEAR_INDEX]
        death_age = death_y - birth_y
        name = values[NAME_INDEX]
        # Print the names and the age at death
        print(name, death_age)
        print(birth_y, '-', death_y)
        print()


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    male_gender = 0
    female_gender = 0

    for values in people_dict.values():
        gender = values[GENDER_INDEX]
        if gender == "M":
            male_gender += 1
        elif gender == "F":
            female_gender += 1
    print('Genders')
    print(f"Numbers of Male: {male_gender}")
    print(f"Numbers of Female: {female_gender}")


def print_marriages(marriages_dict, people_dict):
    """For each marriage in the marriages dictionary, print
    the husband's name, his age at wedding, the wedding year,
    the wife's name, and her age at wedding.

    Parameters
        marriages_dict: a dictionary that contains data about
            marriages. Each item in the dictionary is in this format:
            marriage_key: [husband_key, wife_key, wedding_year]
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    for values in marriages_dict.values():
        men = values[HUSBAND_KEY_INDEX]
        wife = values[WIFE_KEY_INDEX]
        marriage_year = values[WEDDING_YEAR_INDEX]
        # Extracting the values of husbands and wife from people_dict.
        men_info = people_dict[men]
        wife_info = people_dict[wife]
        # Extracting the names of the husbands and wife from people_dict.
        husb_name = men_info[NAME_INDEX]
        wife_name = wife_info[NAME_INDEX]
        # Extracting the husbands and wives years of birth.
        husb_birth_year = men_info[BIRTH_YEAR_INDEX]
        wife_birth_year = wife_info[BIRTH_YEAR_INDEX]
        # Computing the husbands and wives age at the year they married.
        husb_wed_age = marriage_year - husb_birth_year
        wife_wed_age = marriage_year - wife_birth_year
        # Printing the result.
        print(f'{husb_name} {husb_wed_age} > {marriage_year} < {wife_name} {wife_wed_age}')
    
        # print(f'{men_name} {wed_age} > {marriage_year} < {wife_name} {wed_age}')
def count_marriages(people_dict, marriage_dict):
    """This function will count the numbers of times each persons in the people_dict got married
    and then print out the records. it will also print the person that got married the most and the number of times.
    
    Parameters
        people_dict: a dictionary of people with thier details using a key value to record them
        marriage_dict: a dictionary of marriage records of the people in the people_dict dictionary.
        
    Return: nothing
    """
    # A variable for the highest married person. 
    highest = 0
    # An opened list variable for the marriage values keys.
    new_list = []
    
    # Converting the keys in the people_dict into a list.
    key_list = list(people_dict.keys())

    # Converting the values in the marriage_dict into a compound list.
    value_mar_list = list(marriage_dict.values())

    # Iterating through each list in the compound list I just created (value_mar_list).
    for i in value_mar_list:
        # Appending the husbands value in to the list I opened earlier (new_list)
        new_list.append(i[HUSBAND_KEY_INDEX])
        # Appending the wives value in to the list I opened earlier (new_list)
        new_list.append(i[WIFE_KEY_INDEX])
    
    # Iterating through the key_list I created from the people_dict
    for item in key_list:
        # Checking if the items appeared more than once in the new_list I created from the husbands and wives values in the marriage_dict 
        if new_list.count(item) > 0:
            # Storing the return integer into a variable
            count = new_list.count(item)
        else:
            count = 0
        # Getting the values from people_dict using the item from the key_list which are the keys of people_dict.
        n_f = people_dict[item]
        # Extracting the name from the returned values
        name = n_f[NAME_INDEX]
        # Printing the name and count.
        print(name, count)
        # Computing for the highest person with the most marriage
        if count > highest:
            # The variable highest at this point will take the value of count
            highest = count
            # The highest married person's name.
            h_name = name
    # Printing the highest person name and the numbers of times he/she got married.
    print() 
    print(f'{h_name} married the most: {highest} times')
    print()
 


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
