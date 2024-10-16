# Exercise 1
my_list= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def number_is_even(n: int) -> bool:
    return n % 2 == 0
even_squares = [n**2 for n in my_list if number_is_even(n)]
print(even_squares) 





 # Exercise 2   
existing_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
names_to_check = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'George', 'Hannah']

def check_name(name: str) -> bool: # function template

    return name in existing_list

names_in_list = [name for name in names_to_check if check_name(name)]
print(names_in_list) 


