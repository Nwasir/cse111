def main():
    try:
        # Create and print a list named fruit.
        fruit_list = ["pear", "banana", "apple", "mango"]
        print(f"\noriginal: {fruit_list}")

        #Add code to reverse and print fruit_list.
        fruit_list.reverse()
        print(f"reverse: {fruit_list}")

        #Append "orange" to the end of fruit_list and print the list.
        fruit_list.append('orange')
        print(f"append Orange: {fruit_list}")

        #Add code to find where "apple" is located in fruit_list and insert 
        #"cherry" before "apple" in the list and print the list.
        fruit_list.insert(1, "cherry")
        print(f"insert Cherry: {fruit_list}")

        #remove "banana" from fruit_list and print the list
        fruit_list.remove("banana")
        print(f"remove Banana: {fruit_list}")

        #Add code to pop the last element from fruit_list and
        #print the popped element and the list.
        fruit_list.pop()
        print(f"pop orange: {fruit_list}")

        #Add code to sort and print fruit_list.
        fruit_list.sort()
        print(f"sorted: {fruit_list}")

        #Add code to clear and print fruit_list.
        fruit_list.clear()
        print(f"cleared: {fruit_list}\n")

    except IndexError as index_err:
        print(type(index_err).__name__, index_err, sep=": ")
    
    
# Call main to start this program.
if __name__ == "__main__":
    main()