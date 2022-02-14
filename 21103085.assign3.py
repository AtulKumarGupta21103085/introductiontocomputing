# Q.1 :
print("Q.1")
a = str(input("ENTER ANY STRING: "))
list = a.split()
dict = {}
if list.__len__() == 1:
    for i in list[0]:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)
else:
    for i in list:
        if i in dict:
            dict[i] += 1
        else:

            dict[i] = 1
    print(dict)
print("\n")
 
# Q.2 :
print("Q.2")
def Next_Date():
    list1 = [1, 3, 5, 7, 8]
    list2 = [4, 6, 9, 11]
    list3 = [2]
    list4 = [12]
    while (True) :
        day = int(input("Enter the day : "))
        if (1 <= day <= 31):
            break
        else:
            print("Enter a existed day")
    while (True):
        month = int(input("Enter the month : "))
        if (1 <= month <= 12):
            break
        else:
            print("Enter the existed month")
    while (True):
        year = int(input("Enter the year: "))
        if (1800 <= year <= 2025):
            break
        else:
            print("Enter year between 1800 to 2025 : ")
    if month in list1:
        if (day == 31):
            day = 1
            month = month + 1
            print(day, "/", month, "/", year)
        elif (day < 31):
            day += 1
            print(day, "/", month, "/", year)
        else:
            print(" Unfoundable date !")
            Next_Date()
    elif month in list2:
        if (day == 30):
            day = 1
            month = month + 1
            print(day, "/", month, "/", year)
        elif (day < 30):
            day += 1
            print(day, "/", month, "/", year)
        else:
            print(" Unfoundable date ! ")
            Next_Date()
    elif month in list3:
        if (year % 4 == 0):
            if (day == 29):
                day = 1
                month = month + 1
                print(day, "/", month, "/", year)
            elif (day < 29):
                day += 1
                print(day, "/", month, "/", year)
            else:
                print(" Unfoundable date ! ")
                Next_Date()
        else:
            if (day == 28):
                day = 1
                month += 1
                print(day, "/", month, "/", year)
            elif (day < 28):
                day += 1
                print(day, "/", month, "/", year)
            else:
                print(" Unfoundable date ! ")
                Next_Date()
    elif month in list4:
        if (day == 31):
            day = 1
            month = 1
            year += 1
            print(day, "/", month, "/", year)
        elif (day < 31):
            day += 1;
            print(day, "/", month, "/", year)
        else:
            print(" Unfoundable date ! ")
            Next_Date()
    else:
        print(" Unfoundable date ! ")
        Next_Date()
        
Next_Date()
print("\n")
 
# Q.3 :
print("Q.3")
first_list= input("Enter numbers (with spaces but not commas) :  ")
second_list = first_list.split()
print('list: ', first_list)
for i in range(len(second_list)):
    second_list[i] = int(second_list[i])
squarelist = [(second_list[i], second_list[i]**2) for i in range(len(second_list))]
print(squarelist)
print("\n")

# Q.4 :
print("Q.4")
def input_point():
    point = int(input("Enter Grade Points : "))
    if point > 10 or point < 4:
        print(" Unfoundable grades ! ")
        point = input_point()
    return point
grade=input_point()
if(grade==4):
    print("Your Grade is 'D' and Poor Performance")
elif(grade==5):
    print("Your Grade is 'C' and Below Average Performance")
elif(grade==6):
    print("Your Grade is 'C+' and Average Performance")
elif(grade==7):
    print("Your Grade is 'B' and Good Performance")
elif(grade==8):
    print("Your Grade is 'B+' and Very Good Performance")
elif(grade==9):
    print("Your Grade is 'A' and Excellent Performance")
else:
    print("Your Grade is 'A+' and Outstanding Performance")
print("\n")

# Q.5 :
print("Q.5")
x = 6
for i in range(x):
    for j in range(i):
        print(' ', end='')
    for j in range(2*(x-i)-1):
        print(chr(65 + j), end='')   #(A=65,B=66,C=67,D=68,E=69,F=70,G=71,H=72,I=73,J=74,K=75)
    print()
print("\n")

# Q.6 :
print("Q.6")
sid = int(input("Enter SID: "))    #Do not use similar SId
name = input("Enter Name: ")
students = {sid: name}
while True:
    option = input("enter another student(Y or N):").upper()
    if option == 'Y':
        sid = int(input("Enter SID: "))
        name = input("Enter Name: ")
        students[sid] = name
    elif option == 'N':
        break
    else:
        print('Invalid input!')
# a. Print students details stored in the dictionary :
print("a= ", students)
# b. Sort dictionary using student names :
print("b= ", {a: b for a, b in sorted(students.items(), key= lambda x: x[1])})
# c. Sort dictionary using SID :
print("c= ", {a: b for a, b in sorted(students.items())})
# d. Search a student details with SID  and print name of that student :
sid = int(input("Search Name with SID: "))
print("d= ", students[sid])
print("\n")

# Q.7 :
print("Q.7")
def recur_fibo(n):
    # fibonacci sequence
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
number_of_terms = int(input("Enter the number of terms in the series : "))
if number_of_terms <= 0:     # Check if  the no. is foundable
   print("Enter a positive integer")
else:
   print("Fibonacci sequence:")
   sum=0
   for i in range(number_of_terms):
       print(recur_fibo(i))
       sum=sum+recur_fibo(i)
avg=float(sum/number_of_terms)
print("Average of the resultant Fibonacci series = ",avg)

# Q.8 :
print("Q.8")
Set1 = {1, 2, 3, 4, 5}
Set2 = {2, 4, 6, 8}
Set3 = {1, 5, 9, 13, 17}
# a. Create a new set of all elements that are in Set1 and Set2 but not both :
Set_Union = Set1.union(Set2)
Set_Intersection = Set1.intersection(Set2)
Part_A_Set = Set_Union - Set_Intersection
print("a= ", Part_A_Set)
# b. Create a new set of all elements that are in only one of the three sets Set1, Set2 and Set3 :
Part_B_Set = Set1.union(Set2.union(Set3)) - Set1.intersection(Set2) - Set2.intersection(Set3) - Set3.intersection(Set1)
print("b= ", Part_B_Set)
# c. Create a new set of elements that are exactly two of the sets Set1, Set2 and Set3 :
Part_C_Set=((Set1.intersection(Set2)).union((Set1.intersection(Set3)).union(Set2.intersection(Set3))))-(Set1.intersection(Set2.intersection(Set3)))
print("c= ", Part_C_Set)
# d. Create a new set of all integers in the range 1 to 10 that are not in Set1 :
Part_D_Set = set()
for i in range(1, 11):
    if i not in Set1:
        Part_D_Set.add(i)
print("d= ", Part_D_Set)
# e. Create a new set of all integers in the range 1 to 10 that are not in Set1, Set2 and Set3 :
Part_E_Set = set()
for i in range(1, 11):
    if i not in Set1 and i not in Set2 and i not in Set3:
        Part_E_Set.add(i)
print("e= ", Part_E_Set)
