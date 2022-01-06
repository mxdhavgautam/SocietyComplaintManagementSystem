import mysql.connector
from mysql.connector import errorcode
import os

def clrscrn():
    os.system("cls")

while True:
    mycon=mysql.connector.connect(host = 'localhost', user = 'xyz', password = '1234', database = 'comp_sys')
    MyCur=mycon.cursor()
    print('\n')
    print("Society Complaint Management System".center(120, '='))
    print('\n')
    print('1. Lodge Complaints'.center(120))
    print('2. View Pending Complaints'.center(120))
    print('3. View Resolved Complaints'.center(120))
    print('4. Update Complaint Status'.center(120))
    print('5. Delete Entry from Database'.center(120))
    print('6. View All'.center(120))
    print('7. Exit'.center(120))
    print('\n')
    print("=".center(120, '='))
    print('\n')
    choice1 = int(input("Enter the serial *number* of your choice : ".center(75)))
    if choice1 == 1:
        try:
            clrscrn()
            print("******ALL INFORMATION YOU ENTER WILL BE SAVED IN A TEXT FILE comp-log.txt AS A LOG OF ALL DATA******".center(120))
            print('\n')
            cno=int(input("Enter Complaint No:"))
            description=input("Describe Your Issue:")
            address=input("Enter Address:")
            status="Pending"
            Query=("Insert into complaints values(%s,%s,%s,%s);")
            Record=(cno,description,address,status)
            MyCur.execute(Query,Record)
            mycon.commit()
            print("Your complaint has been registered.")
            f=open('comp-log.txt', 'a+')
            fcno=str(cno)
            f.write('\n')
            f.write(fcno)
            f.write('\t')
            f.write('\t')
            f.write('\t')
            f.write(description)
            f.write('\t')
            f.write('\t')
            f.write(address)
            f.write('\t')
            f.write('\n')
            f.close()
            input("Press enter to go back to the Main Menu>>>")
            print('\n')
            clrscrn()
        except mysql.connector.Error as error:
            print('\n')
            print("Operation Failed: {}".format(error).center(120))
            print('\n')
            print('If the error shown above is a Duplicate Key Error, please use a different Complaint Number. This one has already been taken. Type 5 and click enter in the Main Menu to see a list of all complaints and choose a complaint number which is not already in use :)'.center(120))
            print('\n')
            input("Press enter to go back to the Main Menu>>>".center(120))
            print('\n')
            clrscrn()
    elif choice1 == 2:
        try:
            clrscrn()
            print('\n')                  
            MyCur.execute("SELECT * FROM complaints WHERE status='Pending';")
            myresult=MyCur.fetchall()
            print("CNo.,  Description of Complaint,  Address,  State".center(120))
            print('\n')
            for x in myresult:
                print(x)
            else:
                print('\n')
                print('---Bottom of List---'.center(120))
            print('\n')
            input("Press enter to go back to the Main Menu>>>")
            print('\n')
            clrscrn()
        except mysql.connector.Error as error:
            print('\n')
            print("Operation Failed: {}".format(error))
    elif choice1 == 3:
        try:
            clrscrn()
            print('\n')                    
            MyCur.execute("SELECT * FROM complaints WHERE status='Resolved';")
            myresult=MyCur.fetchall()
            print("CNo.,  Description of Complaint,  Address,  State".center(120))
            print('\n')
            for x in myresult:
                print(x)
            else:
                print('\n')
                print("---Bottom of List---".center(120))
            print('\n')
            input("Press enter to go back to the Main Menu>>>")
            print('\n')
            clrscrn()
        except mysql.connector.Error as error:
            print('\n')
            print("Operation Failed: {}".format(error))
    elif choice1 == 4:
        try:
            clrscrn()
            print('\n')
            choice2=input("Has your complaint been successfully resolved? (y/n):")
            if choice2 == 'y':
                print('\n')
                cno=int(input("Enter Complaint No for the complaint to be removed from pending:"))
                stat='Resolved'
                Query=("UPDATE complaints SET status=%s WHERE cno=%s;")
                Record=(stat,cno)
                MyCur.execute(Query,Record)
                mycon.commit()
                print("Updated Successfully.")
                print('\n')
                input("Press enter to go back to the Main Menu>>>")
                print('\n')
                clrscrn()
            elif choice2 == 'Y':
                print('\n')
                cno=int(input("Enter Complaint No for the complaint to be removed from pending:"))
                stat='Resolved'
                Query=("UPDATE complaints SET status=%s WHERE cno=%s;")
                Record=(stat,cno)
                MyCur.execute(Query,Record)
                mycon.commit()
                print("Updated Successfully.")
                print('\n')
                input("Press enter to go back to the Main Menu>>>")
                print('\n')
                clrscrn()
            elif choice2 == 'n':
                print('\n')
                print("PLEASE UPDATE RECORDS ONLY AFTER YOUR ISSUE HAS BEEN RESOLVED.")
                print('\n')
                input("Press enter to go back to the Main Menu>>>")
                print('\n')
                clrscrn()
            elif choice2 == 'N':
                print('\n')
                print("PLEASE UPDATE RECORDS ONLY AFTER YOUR ISSUE HAS BEEN RESOLVED.")
                print('\n')
                input("Press enter to go back to the Main Menu>>>")
                print('\n')
                clrscrn()
            else:
                print('\n')
                print("Incorrect Input, Try Again")
                print('\n')
                input("Press enter to go back to the Main Menu>>>")
                print('\n')
                clrscrn()
        except mysql.connector.Error as error:
            print('\n')
            print("Operation Failed: {}".format(error))
            
    elif choice1 == 5:
        try:
            clrscrn()
            print('\n')
            cno=int(input("Enter Complaint No for the complaint you want to delete:"))
            Query=("DELETE FROM complaints WHERE cno = %s ")
            MyCur.execute(Query, (cno,))
            mycon.commit()
            print("Deleted Successfully.")
            print('\n')
            input("Press enter to go back to the Main Menu>>>")
            print('\n')
            clrscrn()
        except mysql.connector.Error as error:
            print('\n')
            print("Operation Failed: {}".format(error))
    elif choice1 == 6:
        try:
            clrscrn()
            print('\n')                  
            MyCur.execute("SELECT * FROM complaints;")
            myresult=MyCur.fetchall()
            print("CNo.,  Description of Complaint,  Address,  State".center(120))
            print('\n')
            for x in myresult:
                print(x)
            else:
                print('\n')
                print('---Bottom of List---'.center(120))
            print('\n')
            input("Press enter to go back to the Main Menu>>>")
            print('\n')
            clrscrn()
        except mysql.connector.Error as error:
            print('\n')
            print("Operation Failed: {}".format(error))
    elif choice1 == 7:
        print("Good Bye")
        break
    else:
        print("INVALID CHOICE. PLEASE TRY AGAIN.")
    MyCur.close()
    mycon.close()
        
