from tkinter import *

def newpg1():
    global Tmenu
    global E1
    Tmenu =Toplevel(log)
    Tmenu.geometry("500x500")
    Tmenu.title("Menu")

    L3= Label(Tmenu, text="Hello, Tkinter!",font=('Arial',25))
    L3.pack()
    L4=Label(Tmenu, text='What do you want to do today?',font=('Algeria',22))
    L4.pack()
    btn2=Button(Tmenu,text="Upload Circular/Notifications", font=("Arial", 14),command=newpg2)
    btn2.pack(side=TOP)
    btn3=Button(Tmenu, text="Upload Assignment",font=("Arial", 14), command = newpg3)
    btn3.pack()
    btn4=Button(Tmenu, text="Upload Test Results",font=("Arial", 14), command = newpg4)
    btn4.pack()
    btn9=Button(Tmenu,text="Close", font="15",justify=CENTER, command =lambda: newpg1.destroy()) # Problem with command destroy
    btn9.pack()
def newpg2():
    global Ucircular
    Ucircular=Toplevel(Tmenu)
    Ucircular.geometry("300x50")
    Ucircular.title("Upload Circulars")

    L5=Label(Ucircular,text="Latest Circulars / Notifications",font=("Arial",16),justify = CENTER)
    L5.pack()

    btn5=Button(Ucircular,text="Upload/Share Circular",justify=CENTER) 
    btn5.pack()
    
    

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

    btn6=Button(Ucircular,text="Close",justify=CENTER, command=Ucircular.destroy())       #Not working----Optional
    btn6.pack()

def newpg3():
    global Tass
    Tass=Toplevel(Tmenu)
    Tass.title("Upload Assignments")
    Tass.geometry("300x200")

    L6 = Label(Tass, text ='Upload Assignment', font = "50")
    L6.pack()

    Btn8=Button(Tass,text="Upload",justify=CENTER)    #Problem with the command
    Btn8.pack()

def newpg4():
    global Ttest
    Ttest=Toplevel(Tmenu)
    Ttest.geometry("325x50")
    Ttest.title("Upload Test Results")
    btn7=Button(Ttest,text="Upload Marks", font=("Comic Sans MS",15),justify=CENTER)
    btn7.pack()
    

log=Tk()
log.geometry("300x300")
log.title("Teacher Login")
L1 = Label(log, text="User Name", font = '16',justify=LEFT)
L1.pack()
E1=Entry(log, bd =5,font='14',justify=CENTER)
E1.pack()
L2 = Label(log, text="Password", font='16',justify=LEFT)
L2.pack()
E2=Entry(log, bd =5,font ='14',justify=CENTER)
E2.pack()
btn1=Button(log, text='Login',font=('Arial',16), bd=7, justify = CENTER,command = newpg1)
btn1.pack()
username=E1.get()
name = username.split()

#DEKH LIYO  YAHA

log.mainloop()
#Saare destroy waale hata diye sirf ek hi rkha hai coz program is not working then
