# Team Activity: W09

# Problem Statement: A common task for many knowledge workers is to use a
# number, key, or ID to find information about a person. For example, a
# knowledge worker may use a phone number or e-mail address as a key to find
# (or look up) additional information about a customer. During this activity,
# your team will write a Python program that uses a student's I-Number to look
# up the student's name.

# CORE 1: Open the students.csv file for reading, skip the first line of text
# in the file because it contains only headings, and read the other lines of
# the file into a dictionary. The program must store each student I-Number as
# a key and each I-Number name pair or each name as a value in the dictionary.
# CORE 2: Get an I-Number from the user, use the I-Number to find the
# corresponding student name in the dictionary, and print the name.
# CORE 3: If a user enters an I-Number that doesn't exist in the dictionary,
# your program must print the message, "No such student" (without the quotes).
# STRETCH 1: Add code to remove dashes from the I-Number that the user enters.
# This will allow the user to enter I-Numbers with dashes or without dashes and
# still allow the computer to search in the dictionary.
# STRETCH 2: When a user enters an I-Number, your program should ensure it is
# a valid I-Number.
# a. If there are too few digits in the I-Number, your program should print,
# "Invalid I-Number: too few digits" (without the quotes).
# b. If there are too many digits in the I-Number, your program should print,
# "Invalid I-Number: too many digits" (without the quotes).
# c. If the given I-Number contains any characters besides digits and dashes,
# your program should output "Invalid I-Number" (without the quotes).


import csv


def main():
    # Index of the I-Number in the students.csv file
    I_NUMBER_INDEX = 0

    # Index of the I-Number in the students.csv file
    STUDENT_NAME_INDEX = 1

    # Read the contents of the students.csv file into a compount dictionary
    # named students_dict. Use the I_NUMBER as the keys in the dictionary.

    students_dict = read_dict("students.csv", I_NUMBER_INDEX)
    # print(students_dict)

    # Set user_i_number to an empty string
    user_i_number = ""
    # Set more_entries to "yes"
    more_entries = "yes"

    # Use a loop to ask the user to re-enter a student I-Number
    while user_i_number not in students_dict or more_entries == "yes":
        # Ask the user to enter a student I-Number
        user_i_number = input("Please enter a student I-Number "
                              "(ex: 751766201): ").replace("-", "")

        # Check if the user_i_number includes only digits
        if user_i_number.isdigit():
            # Check if the user_i_number is in the students_dict
            if user_i_number in students_dict:
                # Get the student's name
                name = students_dict[user_i_number][STUDENT_NAME_INDEX]
                print(name)

                # Ask user if they want to enter another student I-Number
                more_entries = input("Would you like to enter another student "
                                     "I-Number? (yes/no): ")

            # Check if the user_i_number is less than 9 digits
            elif len(user_i_number) < 9:
                print("Invalid I-Number: too few digits")
            # Check if the user_i_number is more than 9 digits
            elif len(user_i_number) > 9:
                print("Invalid I-Number: too many digits")
            else:
                print("No such student")
        else:
            print("Invalid I-Number: invalid character(s)")
    print("Thank you for using our school database. Goodbye")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will store the data from the CSV file
    dictionary = {}

    # Open the CSV file for reading and store a reference to the opened
    # file in a variable named csv_file
    with open(filename, "rt") as csv_file:
        # Use the csv module to create a reader object that will read from
        # the opened CSV file
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column headings and not
        # data, so this statement skips the first row of the CSV file
        next(reader)
        # Read the rows in the CSV file one row at a time. The reader object
        # returns each row as a list.
        for row_list in reader:
            # If the current row is not blank, add the data from the current
            # to the dictionary.
            if len(row_list) != 0:
                # From the current row, retrieve the data from the column
                # that contains the key.
                key = row_list[key_column_index]
                # Store the data from the current row into the dictionary.
                dictionary[key] = row_list

        return dictionary


# Call main to start this program.
if __name__ == "__main__":
    main()
