# Example 9

def main():
    try:
        with open("contacts.csv", "rt") as contacts_file:
            for line in contacts_file:
                print(line)

    except PermissionError as perm_err:
        print(perm_err)

if __name__ == "__main__":
    main()