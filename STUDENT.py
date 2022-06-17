username=input("Enter your username:")              #
name = username.split()
print('Hello',name[0])                                          #
while True:
    ch=input('''What do you want to do today? 
1. Check latest circulars or notification
2. Assignments
3. Check Test Results''')
    if ch =='1':
        print('''[18.06.2020]
COMPUTER SCIENCE
Students kindly submit your CS project on or before 30th of June 2020 on google classroom.

[10.06.2020]
CHEMISTRY
Make a report on drinking water as your Chemistry Holiday Homework.

[25.05.2020]
CLASS XII
All the Students as well as their Parents kindly note that you have PTM on 5th of June 2020 from 8:30am to 11:30 am. All the subject teachers will be present.
''')
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
