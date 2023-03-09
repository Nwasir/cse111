import random

def main():
    numbers_list = [16.2, 75.1, 52.3]
    print (numbers_list)
    append_random_numbers(numbers_list)
    print(numbers_list)
    append_random_numbers(numbers_list, 3)
    print(numbers_list)     

    house_equipment = ['plate', 'spoon', 'chair', 'table']
    append_random_words(house_equipment, 1)
    print(house_equipment)

def append_random_numbers(numbers_list, quantity=1):
    for _ in range(quantity):
        pseudo_randoms = random.uniform(0, 10)
        pseudo_rounds = round(pseudo_randoms, 1)
        numbers_list.append(pseudo_rounds)
   

def append_random_words(word_list, quantity=1):
    house_equipments = ['bed', 'cupboard', 'generator', 'television']
    for i in range(quantity): 
        pseudo_words = random.choice(house_equipments, 1)  
        i.append(pseudo_words)

if __name__ == "__main__":
    main()
