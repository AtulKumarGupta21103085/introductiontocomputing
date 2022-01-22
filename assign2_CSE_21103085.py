# Question 1 :
intro = "Python is a case sensitive language"
# (a):
print("length of the string = ", len(intro))
# (b):
print("reverse the order = ", intro[::-1])
# (c):
print(intro[10:27])
# (d):
print(intro.replace("a case sensitive", "object oriented"))
# (e):
print(intro.find("a"))
# (f):
print(intro.replace(" ", ""))
print("\n")

# Question 2 :
name = "Atul Kumar Gupta"
sid = 21103085
department = "Computer Science"
cgpa = 9.9
intro = ("Hey,{} Here!\nMy SID is {}\nI am from {} department and my CGPA is {}")
print(intro.format(name, sid, department, cgpa))
print("\n")

# Question 3 :
a = 56
b = 10
# (a):
print("a&b = ", a & b)
# (b):
print("a|b = ", a | b)
# (c):
print("a^b = ", a ^ b)
# (d):
print("Left shift both a and b with 2 bits = ", a << 2, b << 2)
# (e):
print("Right shift a with 2 bits and b with 4 bits = ", a >> 2, b >> 4)
print("\n")

# Question 4 :
num1 = float(input("enter the first number = "))
num2 = float(input("enter the second number = "))
num3 = float(input("enter the third number = "))
if (num1 > num2) and (num1 > num3):
    greatest = num1
elif (num2 > num1) and (num2 > num3):
    greatest = num2
else:
    greatest = num3
print("the greatest number is = ", greatest)
print("\n")

# Question 5 :
intro = input("enter the string = ")
if (input("enter the word = ")) in intro:
    print("Yes")
else:
    print("No")
    print("\n")

# Question 6 :
x = int(input("enter the first side of a triangle = "))
y = int(input("enter the second side of a triangle = "))
z = int(input("enter the third side of a triangle = "))
if (x>y+z):
    print("No")
elif (y>x+z):
    print("No")
elif (z>x+y):
    print("No")
else:
    print("Yes")
