from tabulate import tabulate 
username=input("Enter your username:")              #
name = username.split()
print('Hello',name[0])                                          #
while True:
    ch=input('''What do you want to do today? 
1. Check latest circulars or notification
2. Assignments
3. Check Test Results''')
    if ch =='1':
       mydata = [

    ["18.06.2022","Computer Sci. ","Students kindly submit your CS project on or before 30th of June 2020."],["10.06.2022","Chemistry   ","Make a report on drinking water as your Chemistry Holiday Homework"],
["25.05.2022","Class 12     ","Summer vacations for class XII are from 1st June to 30th June 2022."]
]
       head=[" Date       ","  Title      ","                      Circular/Notification"]
       print(tabulate(mydata, headers=head))
       
       input("Press enter to go back")
    elif ch=='2':
       print("ASSIGNMENTS")
       Ass =['Solutions','MySQL','Trigonometry','Electrostatics']               #
       for i in Ass:
           print(i)
           continue
       Assd=input("Assignment Completed ?")
       if Assd=="Yes":
            sub=input("Enter the title of your assignment")
            for j in Ass:
                if j==sub:
                    Ass.remove(sub)
                    print('REMAINING ASSIGNMENTS')
                    for k in Ass:
                        print(k)
            else:
                Assn=input("New Assignment ?")
                if Assn=='Yes':
                    suba=input('Enter title of the assignment')
                    Ass=Ass+[suba]                                                                      #
                    print('ASSIGNMENT ADDED')
                    for l in Ass:
                        print(l)
                    input("Press enter to go back")
                else:               
                    input("Press enter to go back")
                
    elif ch=='3':
        test={'Solid State':'7/10','RT-Python':'18/25'}
        print('TITLE     MARKS')
        for m in test.keys():
            for n in test.values():
                print( m, n)
        input("Press enter to go back")
