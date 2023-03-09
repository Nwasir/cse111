# Team Activity W08
# CORE 1: Within your program, the print_death_age function must print the name
# and age at death for each person in the people dictionary.
# CORE 2: The count_genders function must count and print the number of males
# and the number of females in the people dictionary.
# CORE 3: The print_marriages function must print the following for each
# marriage in the marriages dictionary:
#  - The name and age in the wedding year of the husband
#  - The year of the wedding
#  - The name and age in the wedding year of the wife

# Each value in the people dictionary is a list. These
# are the indexes of the elements in those lists.
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
    # human readable data about the number of marriages
    count_marriages(marriages_dict, people_dict)


def print_death_age(people_dict):
    """For each person in the people dictionary,
    print the person's name and age at death.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    # Print header
    print("Ages at Death")

    # Iterate through the dictionary
    for person_data in people_dict.values():
        # Person's name
        name = person_data[NAME_INDEX]
        # Person's DOB
        birth_year = person_data[BIRTH_YEAR_INDEX]
        # Person's year of death
        death_year = person_data[DEATH_YEAR_INDEX]
        # Person's age after death
        death_age = death_year - birth_year
        # Print people's name and age of death
        print(f"{name} {death_age}")
        print(f"{birth_year}-{death_year}")


def count_genders(people_dict):
    """Count and print the number of males
    and females in the people dictionary.

    Parameter
        people_dict: a dictionary that contains data about people
            Each item in the dictionary is in this format:
            person_key: [name, gender, birth_year, death_year]
    Return: nothing
    """
    # Set the number of males and females to zero
    males = 0
    females = 0

    # Print header
    print("Gender")

    # Iterate through the dictionary
    for person_data in people_dict.values():
        # Person's gender
        gender = person_data[GENDER_INDEX]
        # Checking if the gender is male.
        if gender == "M":
            # Find the total number of males
            males += 1
        # Checking if the gender is female.
        elif gender == "F":
            # Find the total number of females
            females += 1
        else:
            print("Invalid gender: ", gender)

    print("Number of males: ", males,
          "\nNumber of females: ", females)


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
    # Print header
    print("Marriages")

    # Iterating through the dictionary.
    for marriage_data in marriages_dict.values():
        # Husband_key in marriages_dict ex: "P203"
        husband_key = marriage_data[HUSBAND_KEY_INDEX]
        # Wife_key in marriages_dict ex: "P201"
        wife_key = marriage_data[WIFE_KEY_INDEX]
        # Date of marriage
        marriage_date = marriage_data[WEDDING_YEAR_INDEX]

        if husband_key in people_dict and wife_key in people_dict:
            # This is a list containing the husband's details in people_dict
            husband_data = people_dict[husband_key]
            # This is a list containing the wife's details in people_dict
            wife_data = people_dict[wife_key]
            # Extracts the husband's name from the list in people_dict
            husband_name = husband_data[NAME_INDEX]
            # Extracts the wife's name from the list in people_dict
            wife_name = wife_data[NAME_INDEX]
            # Extracts the husband's DOB from the list in people_dict
            husband_DOB = husband_data[BIRTH_YEAR_INDEX]
            # Extracts the wife's DOB from the list in people_dict
            wife_DOB = wife_data[BIRTH_YEAR_INDEX]
            # Calculate the husband's age at the time of marriage
            husband_marriage_age = marriage_date - husband_DOB
            # Calculate the wife's age at the time of marriage
            wife_marriage_age = marriage_date - wife_DOB
            # Print output
            print(f"{husband_name} {husband_marriage_age} > {marriage_date} < "
                  f"{wife_name} {wife_marriage_age}")
        else:
            print(f"Error: Husband's data for {husband_key} or wife's data "
                  f"for {wife_key} not found.")


def count_marriages(marriages_dict, people_dict):
    # Print header
    print("Number of Marriages")

    # List comprehension
    names_dict = {person_data[NAME_INDEX]: 0 for person_data in
                  people_dict.values()}

    # Iterating through the dictionary.
    for marriage_data in marriages_dict.values():
        # male_key in marriages_dict ex: "P203"
        husband_key = marriage_data[HUSBAND_KEY_INDEX]
        # female_key in marriages_dict ex: "P201"
        wife_key = marriage_data[WIFE_KEY_INDEX]

        if husband_key in people_dict and wife_key in people_dict:
            # This is a list containing the males' details in people_dict
            males_data = people_dict[husband_key]
            # This is a list containing the females' details in people_dict
            females_data = people_dict[wife_key]
            # Extracts the males' names from the list in people_dict
            males_name = males_data[NAME_INDEX]
            # Extracts the females' names from the list in people_dict
            females_name = females_data[NAME_INDEX]
            names_dict[males_name] += 1
            names_dict[females_name] += 1
        else:
            print(f"Error: male's key {husband_key} or wife's key{wife_key}"
                  f" not found.")

    for name, marriage_counter in names_dict.items():
        print(name, marriage_counter)


# If this file was executed like this:
# > python teach_solution.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
