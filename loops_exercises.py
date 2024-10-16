# Exercise 1 
for i in range(1,11):
    print(i)

# Exercise 2
names = ['John', 'Doe', 'Jane', 'Smith', 'Tom']
for a, b in enumerate(names):
	print(f"{b} -","Comprimento -", len(b))
     
# Exercise 3
for i in range(len(names)):
    if names[i] == "Smith":
        print(i)  
        
# Exercise 4
names = ['John', 'Doe', 'Jane', 'Smith', 'Tom']
for a, b in enumerate(names):
    if b == "Smith":
        print(f"Indice de Smith: {a}")

# Exercise 5    
names = ['John', 'Doe', 'Jane', 'Smith', 'Tom']
for a, b in enumerate(names):
    if a == 2:
        print(f"Valor de Indice: {b}")

# Exercise 6 
for i in range(1,11):
    if i % 3 == 0:
        print("Fritz")
    else:
        print(i)
      
# Exercise 7
x = 1
while x <= 10:
     print(x)
     x += 1 

# Exercise 8
import random
z= 0
while z != 5:
     z = random.randint(1,10)
     print(f"random number",z)

# Exercise 9
names = ['John', 'Doe', 'Jane', 'Smith', 'Tom']
for name in names:
    if ("a" in name or "e" in name) and  ("o" in name or "m" in name):
        print(f"Nome: {name}")