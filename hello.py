print("Welcome to Python Aamna!")

# //////// Boolean = true and false ///////
money:bool = True
print(money)
print(int(True))

# ///////Boolean as numbers ////
# true = 1 
# false = 0

print(False + 10)

#  Boolean from Expressions

print(5 == 7) 
print(6 == 6)    

# None (Special Value)
# Python me None ka matlab "koi value nahi" ya "nothing" hota hai.

x = None
print(x)        # Output: None
print(type(x))  # Output: <class 'NoneType'>

# None in Functions
def greet():
    print("Hello!")

result = greet()  
print(result)   # Output: None (kyunki function kuch return nahi kar raha)

# None vs False
# None aur False dono Falsy values hain, lekin ye ek dusre ke barabar nahi hain.

print(None == False)  # Output: False
print(bool(None))     # Output: False (kyunki None bhi falsy value hai)

# 🔸 1. Control Flow Keywords (Decisions & Loops)
# These keywords help in decision-making and loops.
# ✅ if, elif, else → For conditions
# ✅ for, while → For loops
# ✅ break, continue → To control loops

x = 10
if x > 5:
    print("x is greater than 5") 
else:
    print("x is 5 or less")

# 🔸 2. Function & Class Keywords
# Used to define functions and classes.
# ✅ def → Define a function
# ✅ return → Return a value from a function
# ✅ lambda → Create an anonymous function
# ✅ class → Define a class

def invite(name):
    return "Hello, " + name

print(invite("Aleeza"))


# 🔸 3. Exception Handling Keywords (Error Handling)
# Used to handle errors.
# ✅ try, except, finally → Handle exceptions
# ✅ raise → Raise an exception
# ✅ assert → Debugging tool to check conditions

try:
    x = 10 / 6
except ZeroDivisionError:
    print("Your answer is")  

print("Your answer is", x)  # This will print: Your answer is 2.0

# and The and keyword is a logical operator used to check if both conditions are True.

name:str = 'Amna'
age:int = 16
if len(name) > 0 and age > 18:
    print('User is eligible to sign up.')
else:
    print('User is not eligible')

# 🔹 Python Data Types
# Python has built-in data types used to store different kinds of data.

# 🔸 1. Numeric Data Types
# Used for numbers.
# ✅ int (Integer) → Whole numbers
# ✅ float (Floating point) → Decimal numbers
# ✅ complex (Complex numbers) → Used in math

age = 25  # int
price = 99.99  # float
z = 2 + 3j  # complex
print(z,age,price)

# 🔸 Sequence Data Types
# Used for ordered collections.
# ✅ str (String) → Text data
# ✅ list → Ordered, changeable collection
# ✅ tuple → Ordered, unchangeable collection
# ✅ range → Generates sequences

name = "Amna"  # String
fruits = ["Apple", "Banana", "Cherry"]  # List
numbers = (1, 2, 4)  # Tuple
print(numbers)
print(fruits)

# 🔸 Set Data Types
# Used for unordered, unique collections.
# ✅ set → Collection of unique values
# ✅ frozenset → Immutable set

unique_numbers = {1, 2, 3, 3, 4 , 4, 6} # remove duplicates
print(unique_numbers)

# 🔸  Mapping Data Type
# Used for key-value pairs.
# ✅ dict → Dictionary (key-value pairs)

# Example:
student1 = {"name": "Amna", "age": 20}  # Dictionary
student2 = {"name":"Rida" ,"school": "Al-Hamd School"}

print(student2)

