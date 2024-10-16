

def my_function(country = "Norway"):
    print("I am from " + country)

def myft(x):
    return x * 5


print(myft(2))

print("asd".endswith("d"))

a ="a.b.c";

print(a.split("."))



x = ['a'] + ['b']

print(x)

x = ["We", "are", "learning"]

x.append("python") # the .append() method adds a single variable to a list.
x.extend(["programming"])  # the extend() method adds a list 

print(x) # ["We", "are", "learning", "python", "programming"]


fruits = ["Pineapple", "Banana", "Apple", "Melon"]
fruits.insert(0, "Orange")  # insert the value "Orange" at the index 0 (1st position).
print(fruits)

for x in range(5):
	print(x)
     
for i in range(10):
	print(i)
	if i > 5 :
		break
	
for x, y in enumerate(fruits):
    print(x, len(y))

for i in range(len(fruits)):
    print(fruits[i])
    if fruits[i] == "Banana":
          break
    
for i, x in enumerate(fruits):
      if fruits[i] == "Banana":
            print(i)

# using enumerate function  wich names the index
for index, value in enumerate(fruits):
    if index == 2:
        print(value) 

for i in range(11):
      if i >= 1:
        if i % 3 == 0:
            print('Fizz')
        else:
            print(i)
b = 1
while b <= 10:
     print(b)
     b += 1


import random

print(random.randint(1, 10))
                     


# write program generates random numbers between 1 and 10 until the number generated is 5

while True:
    num = random.randint(1, 10)
    if num == 5:
        break
    print(num)


x = ['a','b','c']

# sort iterable x   

x.sort()

sorted



a = 10
b = 20

c = a == b

print(c)



def testusername(username) -> bool:
    if len(username) < 5:
       return(False)
    else:
       return(True)
           
# test age is 18
def testage(age) -> bool:
    if age < 18:
       return(False)
    
#age = int(input("enter your age: "))
#username = input("enter your username: ")




for x in range(5):
	print(x)
    

try:
    result = 10 / 0
except ZeroDivisionError:
    # Handling the ZeroDivisionError and printing an error message
    print("Error: Cannot divide by zero")
# This line will be executed regardless of whether an exception occurred
print("outside of try and except block")