import csv
from datetime import datetime

# for the requested elements
ORDERED_INDEX = 0
ORDERED_QUANTITY_INDEX = 1

# for the products_dict elements
CLOTHES_INDEX = 0
NAME_INDEX = 1
PRICE_INDEX = 2

def main():

    print("\nWelcome to Jimrex Collection")
    print("\nYour Personality depends on what you wear")
    print('\n Names and Prices of native wears\n in Jimrex Collection\n')
        
    try:
        clothe_dict = read_file("clothes.csv", CLOTHES_INDEX)
        
        # Open the CSV file for reading and store a reference
        # to the opened file in a variable named csv_file.
        print("\nOrdered items: ")
        with open("order.csv", "rt") as csv_file:

            # Use the csv module to create a reader object
            # that will read from the opened CSV file.
            reader = csv.reader(csv_file)

            # The first row of the CSV file contains column
            # headings and not data, so this statement skips
            # the first row of the CSV file.
            next(reader)

         
            # counter for the amount of ordered items
            ordered_items_total = 0
            subtotal = 0
            
            for row_list in reader:
                ordered_product = row_list[ORDERED_INDEX]
                ordered_quantity = row_list[ORDERED_QUANTITY_INDEX]

                for key, clothes in clothe_dict.items():

                    name = clothes[NAME_INDEX]
                    cost = clothes[PRICE_INDEX]
                    
                    if ordered_product == key:
                        ordered_items_total += int(ordered_quantity)
                        same_item_total = float(
                            cost) * float(ordered_quantity)
                        subtotal += same_item_total
                        
                        print(f"You selected {ordered_quantity} {name} at the cost of: {cost}")

            tax = subtotal * 0.06
            total = subtotal + tax
            print(f"\n************************************************")
            print(f"\nNumber of items selected is: {ordered_items_total}")
            print(f"\nSubtotal: ${subtotal:.2f}")
            print(f"Sales Tax: {tax:.2f}")
            print(f"\nTotal: ${total:.2f}")

            print(f"\n*****************************************")
            print(f"\nThanks for your patronage.")
           
            
    except (FileNotFoundError, PermissionError) as error:
        print(error)
        print("Please choose a different file.")

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
        print("Please enter a valid ID.")
    
    time(CLOTHES_INDEX)


def read_file(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    # Create an empty dictionary that will
    # store the data from the CSV file.
    dictionary = {}

    # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # The first row of the CSV file contains column
        # headings and not data, so this statement skips
        # the first row of the CSV file.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:

            # From the current row, retrieve the data
            # from the column that contains the key.
            # This will use the column that will be used as key
            key = row_list[key_column_index]
            name = row_list[NAME_INDEX]
            price = row_list[PRICE_INDEX]
            print(name, price)
            #print(NAME_INDEX, PRICE_INDEX)
            # Store the data from the current row
            # into the dictionary.
            dictionary[key] = row_list

    # Return the dictionary.
    return dictionary

def time(current_date_and_time):
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%A %I:%M %p}\n")


if __name__ == "__main__":
    main()
 