from tkinter import *

def openwindow1():
    global menu
    global E1
    menu =Toplevel(login)
    menu.geometry("500x500")
    menu.title("Menu")
    
    L3= Label(menu, text="Hello, Tkinter!",font=('Arial',25))
    L3.pack()
    L4=Label(menu, text='What do you want to do today',font=('Algeria',22))
    L4.pack()
    btn2=Button(menu,text="Circular/Notifications", font=("Arial", 14),command=openwindow2)
    btn2.pack(side=TOP)
    btn3=Button(menu, text="Assignment",font=("Arial", 14), command = openwindow3)
    btn3.pack()
    btn4=Button(menu, text="Test Results",font=("Arial", 14), command = openwindow4)
    btn4.pack()
    btn9=Button(menu,text="Close", font="15",justify=CENTER, command =lambda: openwindow1.destroy()) # Problem with command destroy
    btn9.pack()
def openwindow2():
    global circular
    circular=Toplevel(menu)
    circular.geometry("300x50")
    circular.title("Circulars")

    L5=Label(circular,text="Latest Circulars / Notifications",font=("Arial",16),justify = CENTER)
    L5.pack()

    class Table:                            #Table not complete
	
        def __init__(self,root):
		
		# code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
				
                        self.e = Entry(root, width=20, fg='blue',
			font=('Arial',16,'bold'))
				
                        self.e.grid(row=i, column=j)
                        self.e.insert(END, lst[i][j])

# take the data
    lst = [('Date','Title','Circular/Notification'),
	('18.06.2022','COMPUTER SCIENCE','Students kindly submit your CS project on or before 30th of June 2020 on google classroom.'),
	('10.06.2022','CHEMISTRY','Make a report on drinking water as your Chemistry Holiday Homework.'),
	('25.05.2020','CLASS XII','All the Students as well as their Parents kindly note that you have PTM on 5th of June 2020 from 8:30am to 11:30 am. All the subject teachers will be present.')]

# find total number of rows and
# columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

# create root window
    root = Tk()
    t = Table(root)
    root.mainloop()

    btn5=Button(circular,text="Close",justify=CENTER, command=circular.destroy())       #Not working----Optional
    btn5.pack()

def openwindow3():
    ass = Tk()
    ass.title("Assignments")
    ass.geometry("300x200")

    L6 = Label(ass, text ='GeeksForGeeks', font = "50")
    L6.pack()

    Checkbutton1 = IntVar()
    Checkbutton2 = IntVar()
    Checkbutton3 = IntVar()

    Btn5 = Checkbutton(ass, text = "Solutions",
					variable = Checkbutton1,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)

    Btn6 = Checkbutton(ass, text = "Trigonometry",
					variable = Checkbutton2,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)

    Btn7 = Checkbutton(ass, text = "Capacitance",
					variable = Checkbutton3,
					onvalue = 1,
					offvalue = 0,
					height = 2,
					width = 10)
	
    Btn5.pack()
    Btn6.pack()
    Btn7.pack()

    Btn8=Button(ass,text="Submit",justify=CENTER, command=ass.destroy())    #Problem with the command
    Btn8.pack()

    mainloop()

def openwindow4():
    global TESTS
    TESTS=Toplevel(menu)
    TESTS.geometry("325x50")
    TESTS.title("Test Report")
    L7=Label(TESTS,text="Review your Test Marks", font=("Comic Sans MS",20),justify=CENTER)
    L7.pack()
    
    class Table:
	
        def __init__(t,test):
		
		# code for creating table
            for i in range(total_rows):
                for j in range(total_columns):
				
                    t.e = Entry(test, width=20, fg='Red',
				font=('Times New Roman',16,))
				
                    t.e.grid(row=i, column=j)
                    t.e.insert(END, lst[i][j])

# take the data
    lst = [('Serial No.','Title','Marks','Max. Marks'),
	(1,'Current Electricity',18,20),
	(2,'Python',19,20),
	(3,'Calculus',24,30),
	(4,'Alcohols,Amines & Acids',24,25)]

# find total number of rows and
# columns in list
    total_rows = len(lst)
    total_columns = len(lst[0])

# create root window
    test = Tk()
    a = Table(test)
    test.mainloop()


login=Tk()
login.geometry("300x300")
login.title("Login Page")
L1 = Label(login, text="User Name", font = 16,justify=LEFT)
L1.pack()
E1=Entry(login, bd =5,font=14,justify=CENTER)
E1.pack()
L2 = Label(login, text="Password", font=16,justify=LEFT)
L2.pack()
E2=Entry(login, bd =5,font =14,justify=CENTER)
E2.pack()
btn1=Button(login, text='Login',font=('Arial',16), bd=7, justify = CENTER,command = openwindow1)
btn1.pack()
username=E1.get()
name = username.split()

#DEKH LIYO  YAHA

login.mainloop()
menu.mainloop()
