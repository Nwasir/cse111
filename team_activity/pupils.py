# Team Activity W11
# CORE 1: A function named print_list that takes a list as a parameter and
# prints the list with each element of the list on a separate line.
# CORE 2: A function named main that calls read_compound_list and print_list.
# CORE 3: Statements in the main function that sort the students_list by
# birthdate from oldest to youngest.
# STRETCH 1: Within the main function, replace the code that sorts the
# students_list by birthdate, with code that sorts the students_list
# by given name.
# STRETCH 2: Within the main function, replace the code that sorts the
# students_list by birthdate, with code that sorts the students_list by birth
# month and day. In other words, the code should sort the students_list by
# birthdate but ignore the year when a student was born.


import csv


# Each row in the pupils.csv file contains three elements.
# These are the indexes of the elements in each row.
GIVEN_NAME_INDEX = 0
SURNAME_INDEX = 1
BIRTHDATE_INDEX = 2


def main():
    PUPILS_FILENAME = "pupils.csv"
    # Call the read_compound_list and store its returned value in students_list
    students_list = read_compound_list(PUPILS_FILENAME)

    # Write a lambda function that will extract the birthdate from a student
    birthdate = lambda student_list: student_list[BIRTHDATE_INDEX]
    # Write a call to the Python built-in sorted function that will sort the
    # students_list by date of birth
    sorted_list_by_dob = sorted(students_list, key=birthdate)

    # Write a lambda function that will extract the given name from a student
    given_name = lambda student_list: student_list[GIVEN_NAME_INDEX]
    # Write a call to the Python built-in sorted function that will sort the
    # students_list by given name
    sorted_list_by_gn = sorted(students_list, key=given_name)

    # Write a lambda function that will extract the birthdate from a student
    # and ignore the year of birth
    birth_day_month = lambda student_list: student_list[BIRTHDATE_INDEX][5:]
    # Write a call to the Python built-in sorted function that will sort the
    # students_list by day and month of birth
    sorted_list_by_md = sorted(students_list, key=birth_day_month)

    # Print heading
    print("Ordered from Oldest to Youngest")
    print_list(sorted_list_by_dob)

    # Print heading
    print("\n\nOrdered by Given Name")
    print_list(sorted_list_by_gn)

    # Print heading
    print("\n\nOrdered by Birth Month and Day")
    print_list(sorted_list_by_md)


def read_compound_list(filename):
    """Read the text from a CSV file into a compound list.
    The compound list will contain small lists. Each small
    list will contain the data from one row of the CSV file.

    Parameter
        filename: the name of the CSV file to read.
    Return: the compound list
    """
    # Create an empty list.
    compound_list = []

    # Open the CSV file for reading.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader
        # object that will read from the opened file.
        reader = csv.reader(csv_file)

        # The first line of the CSV file contains column headings
        # and not a student's I-Number and name, so this statement
        # skips the first line of the CSV file.
        next(reader)

        # Process each row in the CSV file.
        for row in reader:

            # Append the current row at the end of the compound list.
            compound_list.append(row)

    return compound_list


def print_list(a_list):
    """
    `print_list` takes a list of students and prints each student in the list
    on separate lines
    :param a_list: a list of strings
    """
    # Iterating through the list and printing each element.
    for student in a_list:
        print(student)


# If this file is executed like this:
# > python add_area_code.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()
