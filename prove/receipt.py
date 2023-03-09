import csv
from datetime import datetime



def main():
    try:
        print("Inkom Emporium")
        #request_list = read_dict('request.csv', 0)
        
        # Calls the read_dictionary function and stores the
        # compound dictionary in a variable named products_dict.
        products_dict = read_dict('products.csv', 0)
        # Prints the products_dict.
        #print(products_dict)

        with open("request.csv","rt") as request_list:

            # Use the csv module to create a reader object that will read from
            # the opened CSV file
            reader = csv.reader(request_list)
            # The first row of the CSV file contains column headings and not
            # data, so this statement skips the first row of the CSV file
            next(reader)

            # for the products_dict elements
            P_NAME_INDEX = 0
            P_COST_INDEX = 1

            # for the requested elements
            R_PRODUCT_INDEX = 0
            R_QUANTITY_INDEX = 1

            total_product = 0
            subtotal = 0

            for line in request_list:
                product_num = line[R_PRODUCT_INDEX]
                quan_list = line[R_QUANTITY_INDEX]
                
                for key, value in products_dict.items():

                     name = value[P_NAME_INDEX]
                     cost = value[P_COST_INDEX]                   
                     item_total = float(cost) * float(quan_list)

                     if product_num == key:
                        total_product += int(quan_list)
                        
                        subtotal += item_total
                        print(f"- {name}: {quan_list} | ${cost}")          

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax
        print('number of item: {total_product:.0f}')
        print('Subtotal: {subtotal:.2f}')
        print('sales tax: {sales_tax:.2f}')
        print("total: {total:.2f}")
        print()
        print("Thank you for shopping at the Inkom Emporium.")

    except FileNotFoundError as not_found_err:
        # This code will be executed if the user enters
        # the name of a file that doesn't exist.
        print()
        print(type(not_found_err).__name__, not_found_err, sep=": ")
        
    except PermissionError as perm_err:     
        print(type(perm_err).__name__, perm_err, sep=": ")
        print("Please choose a different file")

    except KeyError as key_err:
        print(type(key_err).__name__, key_err)
       
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()

    # Use an f-string to print the current
    # day of the week and the current time.
    print(f"{current_date_and_time:%A %I:%M %p}")

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
    dictionary = {}
    # dictionary = { "D150" : [D150,1 gallon milk,2.85] }
    # dictionary["D150"] = [D150,1 gallon milk,2.85]
    # Open the CSV file for reading and store a reference to the opened
    # file in a variable named csv_file
    with open(filename, 'rt') as csv_file:
        # Use the csv module to create a reader object that will read from
        # the opened CSV file
        reader = csv.reader(csv_file)
        # The first row of the CSV file contains column headings and not
        # data, so this statement skips the first row of the CSV file
        next(reader)

        
        # Uses a loop that reads one at a time and processes each row
        # from the request.csv file.
        print("From products file")
        for row in reader:
            # dictionary["D150"] = [D150,1 gallon milk,2.85]
            #print(row[key_column_index], row)
            #dictionary[row[key_column_index]]  = row   # dictionary["D150"] = [D150,1 gallon milk,2.85]
            
            # dictionary["D150"] = row[1 gallon milk,2.85]
            key = row[0]
            price = row[2]
            # Append the current row at the end of the compound list.
            dictionary[key] = row
        print(dictionary)
           
    return dictionary 

# Call main to start this program.
if __name__ == "__main__":
    main()
