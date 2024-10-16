# first function
def frst_function():
    return 2+2

def to_celsisu(x):
    return(x-32) * 5/9

temperature_celsius = to_celsisu(150)
print(temperature_celsius)

print( 1 - True)


name = "Alice"

print(f"{name} is my name")


print("{} is my name".format(name))

list = ["a","b "]
tuple = ("a","b")
newlist = {"a":1,"b":2}
newlist2 = {1,2,3}

print(len(name))
print("type{}{}{}{}".format( type(list),type(tuple),type(newlist),type(newlist2)))


hello = "Hello World, my friend"
newstrip = hello.strip(",")
print(newstrip)


#Exercise 1¶
#Given the string s = "Hello, World", extract the substring "Hello".
s = "Hello, World"
print(s[0:5])

#Exercise 2
#Given the string s = "Hello, World", extract the substring "World".
s = "Hello, World"
print(s[-5:])

#Exercise 3
#How many times does the letter l appear in the string s = "Hello, World"?
print(s.count("l"))
#Exercise 4
#Replace the substring "World" with "Alice" in the string s = "Hello, World".
print(s.replace("World","Alice"))

#Exercise 5
#Convert the string s = "Hello, World" to uppercase
s = "Hello, World"
print(s.upper())


def my_function(fname, lname):
    full_name = fname + " " + lname
    print(full_name)


full_name = my_function("Joao", "Santos")

print(full_name)
print(type(full_name))


a = True
b = 1 == 2
if a:
    print("True")
else:
    print("False")


#if ( b is True)
#    print("a is true")

x1 = "a"
x2 = ["a","b"]



b= x1  in x2  # check for inclusion
print(b)
print(x2[:1])
#s + t   # can be concatenated and multiplied (*)
#s[:i]   # can be accessed and sliced
#s.index(d)  # they have the .index() method
#s.count(d)  # and the .count() method    


xa = "I am going on hilliday to France"
print(xa.split())


t = (1, 2, 3 , 4, 5)
t2 = t[-2:]

print(type(t2))

newlis =  [1,2,3,4,5]
newlis.append(6)
newlis2 = [1,2,3,4,5]
newlis.extend(newlis2)
print(newlis)



# remove element from lis newlis    
newlis.pop(1)
print(newlis)   



#fruits = ["Pineapple", "Banana", "Apple", "Melon"]
#fruits.insert(0, "Orange")  # insert the value "Orange" at the index 0 (1st position).
#print(fruits)

#print(sorted(fruits))


fruits_cal = {"banana":3,"apple":1,"melon":2}
print(fruits_cal.items())
fruits_cal_list = sorted(fruits_cal.items(), key=lambda x: x[1])

print(fruits_cal_list)



a = ["cow", "dog", "cat", "dog", "gerbil", "manatee", "gecko", "marmoset"]

for x in range(len(a)):
    print(a[x])


i1 = 0
for x1,x2 in enumerate(a):
    i1 += 1
    if x2 == "gerbil":
        print(x1,x2)


for z in range(1,11):
    if z % 3 == 0:
        print("Fritz")
    else:
        print(z)      


import random
zx = 0
while zx != 5:
    zx = random.randint(1,10)
    print(zx)


names = ['John', 'Doe', 'Jane', 'Smith', 'Tom']

for z2 in range(len(names)):
    if  ("a" in names[z2] or "e" in names[z2]) or ("o" in names[z2]) and ("m" in names[z2]):
        print(names[z2])
        


x = {
	"John": 12,
	}
        
print( x.get("John2",0))





fruits_cal = {"banana":3,"apple":1,"melon":2}

for x in fruits_cal:
    print(x,fruits_cal[x])



sentences = [
    "I am a student",
    "I am a teacher",
    "I am a programmer"
]


# Diction Compreensive

wordcount2 = dict()
print(wordcount2)
for c in sentences:
    words = c.split()
    wordcount2= {w: wordcount2.get(w, 0) + 1 for w in words}
print(wordcount2)



# recursivo

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5))


