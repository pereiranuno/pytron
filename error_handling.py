



#Exercise 2

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        print("Cannot divide by zero")
        return 0

def calculate_average(numbers):
    try:
        total = sum(numbers)
        average = divide(total, len(numbers))
        return average
    except TypeError:
        print("List contains non-numeric values")
        return 0

# Exemplo de utilização
numbers = [1, 2, 3, 4]
print(calculate_average(numbers))  # Saída esperada: 2.5

empty_numbers = []
print(calculate_average(empty_numbers))  # Saída: "Cannot divide by zero" e depois 0

invalid_numbers = [1, "two", 3]
print(calculate_average(invalid_numbers))  # Saída: "List contains non-numeric values" e depois 0


#a= "a" +2"
#print (f"{a}")


print(1**'a')

