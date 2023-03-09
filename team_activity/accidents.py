# CORE 1: Add exception handling code that prints a useful error message when
# the computer raises FileNotFoundError or PermissionError.
# CORE 2: Add exception handling code that prints a useful error message when
# the computer raises ValueError while it is converting the percentage entered
# by the user to a float.
# CORE 3: Add code that prints a useful error message when the user enters a
# percentage that is less than 0 or greater than 100. Hint: you could add an
# if statement immediately after the line of code that gets the percentage from
# the user.

# STRETCH 1: Add exception handling code to handle ZeroDivisionError that might
# be raised by the estimate_reduction function. This exception handling code
# should print a useful error message that includes the filename and line
# number of the line that contains zero (0) in the "Fatal Crashes" column.
# STRETCH 2: Add exception handling code to handle csv.Error that might be
# raised by the csv module. This exception handling code should print a useful
# error message that includes the filename and line number of the line that is
# formatted incorrectly.

# print(f"{zero_div_err}\n{filename} contains 0 at line {line_number} "
# f"in the Fatal Crashes column.")
# print(f"{csv.err}\n{filename} contains an incorrect formatted value at"
# f" line {line_number} in the Fatal Crashes column.")

# Import the csv module so that it can be used
# to read from the accidents.csv file.
import csv


# Column numbers from the accidents.csv file.
YEAR_COLUMN = 0
FATALITIES_COLUMN = 1
INJURIES_COLUMN = 2
CRASHES_COLUMN = 3
FATAL_CRASHES_COLUMN = 4
DISTRACT_COLUMN = 5
PHONE_COLUMN = 6
SPEED_COLUMN = 7
DUI_COLUMN = 8
FATIGUE_COLUMN = 9


def main():
    try:
        # Prompt the user for a filename and open that text file.
        filename = input("Name of file that contains NHTSA data: ")
        with open(filename, "rt") as text_file:
            while True:
                try:
                    # Prompt the user for a percentage.
                    perc_reduc = float(input(
                        "Percent reduction of texting while driving "
                        "[0, 100]: "))
                    if perc_reduc < 0:
                        print(f"Error: {perc_reduc} is too low. Please enter "
                              f"a different number.")
                    elif perc_reduc > 100:
                        print(f"Error: {perc_reduc} is too high. Please enter "
                              f"a different number.")
                    else:
                        break
                except ValueError as val_err:
                    print(f"{val_err}")

            print()
            print(f"With a {perc_reduc}% reduction in using a cell",
                  "phone while driving, approximately this",
                  "number of injuries and deaths would have",
                  "been prevented in the USA.", sep="\n")
            print()
            print("Year, Injuries, Deaths")

            # Use the csv module to create a reader
            # object that will read from the opened file.
            reader = csv.reader(text_file)

            # The first line of the CSV file contains column headings
            # and not a student's I-Number and name, so this statement
            # skips the first line of the CSV file.
            next(reader)

            # Process each row in the CSV file.
            for line_number, row in enumerate(reader, 2):
                year = row[YEAR_COLUMN]

                # Call the estimate_reduction function.
                injur, fatal = estimate_reduction(
                        row, PHONE_COLUMN, perc_reduc)

                # Print the estimated reductions
                # in injuries and fatalities.
                print(year, injur, fatal, sep=", ")
    except FileNotFoundError as file_not_found:
        print(f"{file_not_found}\n.Please choose a different file.")
    except PermissionError as perm_err:
        print(f"{perm_err}\nPlease choose a different file.")
    except ZeroDivisionError as zero_div_err:
        print(f"{zero_div_err}\n{filename} contains 0 at line {line_number} "
              f"in the Fatal Crashes column.")
    except csv.Error as csv_err:
        print(f"{csv.err}\n{filename} contains an incorrect formatted value at"
              f" line {line_number}.")


def estimate_reduction(row, behavior_key, perc_reduc):
    """Estimate and return the number of injuries and deaths that
    would not have occurred on U.S. roads and highways if drivers
    had reduced a dangerous behavior by a given percentage.

    Parameters
        row: a CSV row of data from the U.S. National Highway Traffic
            Safety Administration (NHTSA)
        behavior_key: heading from the CSV file for the dangerous
            behavior that drivers could reduce
        perc_reduc: percent that drivers could reduce a dangerous
            behavior
    Return: The number of injuries and deaths that may have been
        prevented
    """
    behavior = int(row[behavior_key])
    fatal_crashes = int(row[FATAL_CRASHES_COLUMN])
    ratio = perc_reduc / 100 * behavior / fatal_crashes

    fatalities = int(row[FATALITIES_COLUMN])
    injuries = int(row[INJURIES_COLUMN])

    reduc_fatal = int(round(fatalities * ratio, 0))
    reduc_injur = int(round(injuries * ratio, 0))
    return reduc_injur, reduc_fatal


# If this file was executed like this:
# > python accidents.py
# then call the main function. However, if this file
# was simply imported, then skip the call to main.
if __name__ == "__main__":
    main()
