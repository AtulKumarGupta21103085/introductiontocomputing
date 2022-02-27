# Question.1:
# recursive python function to solve the problem of tower fo Hanoi with three disks:
print("Question.1(output):")
def TowerOfHanoi(n,source,destination,middle):
    if(n==0):
        return
    TowerOfHanoi(n-1,source,middle,destination)
    print("Move disk {} from {} to {}".format(n,source,destination))
    TowerOfHanoi(n-1,middle,destination,source)

# A,B, C are the name of rods and n are disks
n=3
TowerOfHanoi(n,"A","C","B")
print("\n")



# Question.2:
# Print the Pascal's Triangle for n number of rows given by the user both recursive and iterative procedures
print("Question.2(output):")
print("Using Iterative Procedures")

#for n number of rows
n = int(input("Enter the number the rows: "))

for i in range(1, n + 1):
    for j in range(0, n - i + 1):
        print(' ', end='')

    C = 1                                 # first element is always 1
    for j in range(1, i + 1):
        print(' ', C, sep='', end='')

        C = C * (i - j) // j              # using Binomial Coefficient
    print()

print("Using Recursive Procedures")
def fact(n):
    res = 1
    for c in range(1, n + 1):
        res = res * c
    return res

rows = int(input("Enter the number of rows : "))
for i in range(0, rows):
    for j in range(1, rows - i):
        print("  ", end="")
    for k in range(0, i + 1):
        coff = int(fact(i) / (fact(k) * fact(i - k)))
        print("  ", coff, end="")
    print()
print("\n")




# Question. 3:
print("Question.3(output):")
int1, int2 = map(int, input("Enter the two number: ").split())    #NOTE:enter the two number with space key
quotient = int1 // int2
remainder = int1 % int2

print("a:")       #check whether it (function/values) is valuable or not
print(callable(quotient))
print(callable(remainder))

print("b:")       #check wheather all the values are non zeros or not
if quotient == 0:
    print("Quotient is zero!")
if remainder == 0:
    print("Remainder is zero!")
if quotient != 0 and remainder != 0:
    print("All values are non zero")

print("c:")      #add values (4,5,6) to the result and filter out the values which are greater than 4
SomeValues= [quotient + 4, remainder + 4, quotient + 5, remainder + 5, quotient + 6, remainder + 6]
result=[]
for i in range (len(SomeValues)):
    if SomeValues[i] > 4:
        result.append(SomeValues[i])
print(f"filter out the values which are greater than 4: {result}")

print("d:")       #convert the above result into set datatype
resulto=set(result)
print(resulto)

print("e:")       #make that set immutable
# frozenset : The frozenset() is an inbuilt function in Python which takes an iterable object as input and makes them immutable
immutableSet = frozenset(resulto)
print(immutableSet)

print("f:")       #evaluate the maximum value from set and find out its hash value
print(hash(max(immutableSet)))
print("\n")




# Question.4:
# create a class named student, use the __init__()function to assign values for name and roll number
# Also call __del__() function to destroy object that is created
print("Question.4(output):")

class Student:
    def __init__(self, student, roll_no):
        self.name=student
        self.roll_no=roll_no
    def __del__(self):
        print("Object destroy that is created!")

A1 = Student("Atul Kumar Gupta", 21103085)
print(f"Name:{A1.name} and SID:{A1.roll_no}")
del A1
print("\n")




# Question.5:
# write a program to store details of three employees : name and salary using class

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
A = Employee("Mehak", 40000)
B = Employee("Ashok", 50000)
C = Employee("Viren", 60000)

print("5.a:")                 # updating the salary of Mehak to 70000
A.salary = 70000
print(f"The updated salary of {A.name} is {A.salary} ")

print("5.b:")                 # delete the record of employee Viren
print("Delete the record of employee Viren", end='')
del C
print("\n")


# Question.6:
# create a new meaningful word using the exact same letters and to form a word then their friendship is a fake
print("Question.6(output):")
def anagram(word):
    if len(word) == 1:
        return [word];
    partial_words = anagram(word[1:])
    char = word[0]
    result = []
    for perm in partial_words:
        for i in range(len(perm)+1):
            result.append(perm[:i]+char+perm[i:])
    return result
George_word= input("Please give a word: ")
Possible_words = anagram(George_word)
Barbie_word = input("Give a word: ")
print("Possible Words-", Possible_words)
print("If Barbie's word lies in the list,then their friendship is real.")

if Barbie_word in Possible_words:
    print("Friendship is real.")
else:
    print("Friendship is fake.")
print("\n")


