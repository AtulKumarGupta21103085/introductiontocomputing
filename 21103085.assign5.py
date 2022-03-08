# Question.1:
# make a GUI based GST tax finder calculator
print("Q.1:")
from tkinter import*
#Function for finding gst rate
def find_gst():
    org_cost=int(org_priceField.get())
    net_cost=int(net_priceField.get())
    gst_rate=((net_cost - org_cost) * 100) / org_cost
    print("the original cost is: ",org_cost)
    print("the net cost is : ",net_cost)
    print("the gst rate is : ",gst_rate)
    gst_rateField.insert(12, str(gst_rate) + "%")

#function for clearing all the enteries
def clear_all():
    org_priceField.delete(0,END)
    net_priceField.delete(0,END)
    gst_rateField.delete(0,END)

#driver code
win=Tk()
win.configure(background='light blue')
win.geometry('500x500')
win.title("GST RATE FINDER")
lbl_1=Label(win,text='ENTER ORIGINAL PRICE',bg='red',relief='ridge',padx=3,pady=3,bd=3,font=('calibre',14,'bold','underline'))
lbl_1.grid(row=1,column=1,padx=10,pady=10)
lbl_2=Label(win,text="ENTER NET PRICE",bg='red',relief='ridge',padx=3,pady=3,bd=3,font=('calibre',14,'bold','underline'))
lbl_2.grid(row=2,column=1,padx=10,pady=10)
but_1=Button(win,text="Calculate",padx=3,pady=3,bg='light grey',relief='sunken',bd=3,font=('calibre',14),command=find_gst,activebackground='red')
but_1.grid(row=3,column=2,padx=10,pady=10)
lbl_3=Label(win,text="GST RATE IS",bg='red',relief='ridge',padx=3,pady=3,bd=3,font=('calibre',14,'bold','underline'))
lbl_3.grid(row=4,column=1,padx=10,pady=10)
but_2=Button(win,text="Clear",padx=3,pady=3,bg='light grey',relief='sunken',bd=3,font=('calibre',14),command=clear_all,activebackground='red')
but_2.grid(row=5,column=2,padx=10,pady=10)
org_priceField=Entry(win)
org_priceField.grid(row=1,column=2,padx=10,pady=10)
net_priceField=Entry(win)
net_priceField.grid(row=2,column=2,padx=10,pady=10)
gst_rateField=Entry(win)
gst_rateField.grid(row=4,column=2,padx=10,pady=10)
win.mainloop()
print("\n")


# Question.2:
# Create a GUI based calender application using Tkinter module
print("Q.2:")

from tkinter import *
# importing calendar module
import calendar
# Function for showing the calendar of the given year
def showCal() :

	# Create a GUI window
	new_gui = Tk()

	# Set the background colour of GUI window
	new_gui.configure(background = "white")

	# set the name of tkinter GUI window
	new_gui.title("CALENDAR")

	# Set the configuration of GUI window
	new_gui.geometry("500x500")

	# get method returns current text as string
	fetch_year = int(year_field.get())

	# calendar method of calendar module return
	# the calendar of the given year .
	cal_content = calendar.calendar(fetch_year)

	# Create a label for showing the content of the calendar
	cal_year = Label(new_gui, text = cal_content, font = "Consolas 10 bold")

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure.
	cal_year.grid(row = 5, column = 1, padx = 20)

	# start the GUI
	new_gui.mainloop()


# Driver Code
if __name__ == "__main__" :

	# Create a GUI window
	gui = Tk()

	# Set the background colour of GUI window
	gui.config(background = "light blue")

	# set the name of tkinter GUI window
	gui.title("CALENDAR")

	# Set the configuration of GUI window
	gui.geometry("500x500")

	# Create a CALENDAR : label with specified font and size
	cal = Label(gui, text = "CALENDAR", bg = "dark red",font = ("times", 40, 'bold'),padx=5,pady=5)


	# Create a Enter Year : label
	year = Label(gui, text = "ENTER YEAR", bg = "light green",font = ("times", 28, 'bold'),padx=5,pady=5)

	# Create a text entry box for filling or typing the information.
	year_field = Entry(gui)

	# Create a Show Calendar Button and attached to showCal function
	Show = Button(gui, text = "Show Calendar", fg = "Black",bg = "Red", command = showCal)

	# Create a Exit Button and attached to exit function
	Exit = Button(gui, text = "Exit", fg = "Black", bg = "Red", command = exit)

	# grid method is used for placing
	# the widgets at respective positions
	# in table like structure.
	cal.grid(row = 1, column = 1,padx=140,pady=10)

	year.grid(row = 2, column = 1,padx=140,pady=0)

	year_field.grid(row = 3, column = 1,pady=5)

	Show.grid(row = 4, column = 1)

	Exit.grid(row = 6, column = 1)

	# start the GUI
	gui.mainloop()
print("\n")


# Question.3:
# Python program to create a simple GUI
# calculator using Tkinter
print("Q.3:")
# import everything from tkinter module
from tkinter import *

# globally declare the expression variable
expression = ""


# Function to update expression
# in the text entry box
def press(num):
    # point out the global expression variable
    global expression

    # concatenation of string
    expression = expression + str(num)

    # update the expression by using set method
    equation.set(expression)


# Function to evaluate the final expression
def equalpress():
    # Try and except statement is used
    # for handling the errors like zero
    # division error etc.

    # Put that code inside the try block
    # which may generate the error
    try:

        global expression

        # eval function evaluate the expression
        # and str function convert the result
        # into string
        total = str(eval(expression))

        equation.set(total)

        # initialize the expression variable
        # by empty string
        expression = ""

    # if error is generate then handle
    # by the except block
    except:

        equation.set(" error ")
        expression = ""


# Function to clear the contents
# of text entry box
def clear():
    global expression
    expression = ""
    equation.set("")


# Driver code
if __name__ == "__main__":
    # create a GUI window
    gui = Tk()

    # set the background colour of GUI window
    gui.configure(background="light green")

    # set the title of GUI window
    gui.title("Simple Calculator")

    # set the configuration of GUI window
    gui.geometry("270x150")

    # StringVar() is the variable class
    # we create an instance of this class
    equation = StringVar()

    # create the text entry box for
    # showing the expression .
    expression_field = Entry(gui, textvariable=equation)

    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .
    expression_field.grid(columnspan=4, ipadx=70)

    # create a Buttons and place at a particular
    # location inside the root window .
    # when user press the button, the command or
    # function affiliated to that button is executed .
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                     command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)

    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                     command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)

    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                     command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)

    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                     command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)

    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                     command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)

    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                     command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)

    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                     command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)

    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                     command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)

    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                     command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)

    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                     command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)

    plus = Button(gui, text=' + ', fg='black', bg='red',
                  command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)

    minus = Button(gui, text=' - ', fg='black', bg='red',
                   command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)

    multiply = Button(gui, text=' * ', fg='black', bg='red',
                      command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)

    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)

    equal = Button(gui, text=' = ', fg='black', bg='red',
                   command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)

    clear = Button(gui, text='Clear', fg='black', bg='red',
                   command=clear, height=1, width=7)
    clear.grid(row=5, column='1')

    Decimal = Button(gui, text='.', fg='black', bg='red',
                     command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)
    # start the GUI
    gui.mainloop()
print("\n")


# Question.4:
print("Q.4:")
# Defining Quicksort Function
def QuickSort(array,low,high):
    if(low>=high): #If a single element or no element is there return
        return
    pivot=low #Creating a Variable with value of start
    count=low #Creating a Variable with value of start
    for i in range(low+1,high): #Counting number of terms less than or equal to pivot point
        if(array[i]<=array[pivot]):
            count+=1
    temp=array[pivot] #Substituting the value at pivot point with value at start
    array[pivot]=array[count]
    array[count]=temp
    pivot=count #replacing the previous value of pivot point with count
    i=low #defining two variable one from start and another from end
    j=high-1
    while(i<pivot and j>pivot):
        if(array[i]>array[pivot] and array[j]<=array[pivot]):
            temp = array[i] #Creating a while loop to shift number less than or equal to pivot on its left and greater than that on its right
            array[i] = array[j]
            array[j] = temp
            i+=1
            j-=1
        elif(array[j]>array[pivot]):
            j-=1
        elif(array[i]<=array[pivot]):
            i+=1
    QuickSort(array,low,pivot) #sorting left part of pivot
    QuickSort(array,pivot+1,high) #sorting right part of pivot

def Mergesort(array,start,end):
    size=end-start #size is defined
    if(size<=1): #if size of list is less than or equal to 1 return
        return
    else:
        mid=(start+end)//2  #defined a mid which is having value equal to (start+end)/2 floor division

        Mergesort(array,start,mid) #Calling the function for the left half part
        Mergesort(array,mid,end) #Calling the function for the right half part
        result=[0]*size #created a new list of the size equal to the size of input list
        i=start #Starting variable defined
        j=mid #another variable with value of mid is defined
        count=0
        # While loop is created for sorting the elements across the array if the starting index is less than mid and ending index is less than end index
        while(i<mid and j<end):
            if(array[i]<=array[j]):
                result[count]=array[i]
                i+=1
            elif(array[i]>=array[j]):
                result[count]=array[j]
                j+=1
            count+=1
        if(i==mid and j<end):#If the starting point is equal to mid but the end point is not equal to end of list
            while(j<end):
                result[count]=array[j]
                j+=1
                count+=1
        if (j == end and i < mid): #If the starting point is not equal to mid but the ending index is at end of the list
            while (i < mid):
                result[count] = array[i]
                i+=1
                count+=1

        for i in range(size): #Replacing the elements of the original list with the new list
            array[i+start]=result[i]
list1=list(map(int,input("Enter The Numbers:\n").split()))
print("List Entered By User:",list1) #Printing the input list
Mergesort(list1,0,len(list1)) #Using Merge Sort to sort the list
print("Sorted List Using Merge Sort:",list1)
QuickSort(list1,0,len(list1)) #Using Quick Sort to sort the list
print("Sorted List Using Quick Sort:",list1)
print("\n")


# Question.5:
# Using Merge Sort to Sort The list
print("Q.5:")
def Mergesort(array,start,end):
    size=end-start
    if(size<=1):
        return
    else:
        mid=(start+end)//2

        Mergesort(array,start,mid)
        Mergesort(array,mid,end)
        result=[0]*size
        i=start
        j=mid
        count=0
        while(i<mid and j<end):
            if(array[i]<=array[j]):
                result[count]=array[i]
                i+=1
            elif(array[i]>=array[j]):
                result[count]=array[j]
                j+=1
            count+=1
        if(i==mid and j<end):
            while(j<end):
                result[count]=array[j]
                j+=1
                count+=1
        if (j == end and i < mid):
            while (i < mid):
                result[count] = array[i]
                i+=1
                count+=1

        for i in range(size):
            array[i+start]=result[i]

#BinarySearch Function
def Binarysearch(list,number):
    start=0
    end=len(list)
    indicator=False
    while(start<=end):
        mid=(start+end)//2
        if(list[mid]==number):
            indicator=True
            break
        elif(list[mid]>number):
            end=mid-1
        elif(list[mid]<number):
            start=mid+1
    return indicator

#Taking Input of list from User and converting it into list directly
input_list=list(map(int,input("Enter The Numbers:\n").split()))
print("List Entered By User:",input_list)
#Sorting the list using Merge Sort
print("Part a")
Mergesort(input_list,0,len(input_list))
print("Sorted List:",input_list)
#Taking Input from user to check the number
number_check=int(input("Enter The Number You Want To Check:\n"))

#Printing the result, if the number present in the list entered by user using binary search
print("Part b")
print("If the Number is Present:",Binarysearch(input_list,number_check))
#Counting the number of times the number has appeared in list
print("Part c")
if(Binarysearch(input_list,number_check)==True):
     print("Number of times the number entered by user appeared:",input_list.count(number_check))
