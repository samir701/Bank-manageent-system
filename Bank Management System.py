import mysql.connector as a
con=a.connect(host="localhost",user="root",password="1234",database="bank_sys")

def openAcount():
    print("*************OPEN NEW ACCOUNT*************")
    Acc_no =int(input("Enter Account No.:- "))
    Name=input("Enter Name :- ")
    Dob=input("Enter Date of Birth :- ")
    Address=input("Enter Address :- ")
    Mob_no =int(input("Enter Mobile No.:- "))
    Balance=int(input("Enter Opening Balance :- "))
    sql1="insert into account values('{}','{}','{}','{}','{}','{}')".format(Acc_no, Name, Dob, Address, Mob_no, Balance)
    sql2="insert into amount values('{}','{}','{}')".format(Acc_no, Name, Balance)
    c=con.cursor()
    c.execute(sql1)
    c.execute(sql2)
    con.commit()
    print("Congratulaions Account Open Successfully")
    main()

def deposit():
    print("**************DEPOSIT AMOUNT**************")
    amount=int(input("Enter Amount :- "))
    Acc_no=input("Enter Account No :- ")
    a="select TotalBalance from amount where Acc_no={}".format(Acc_no)
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchone()
    b=myresult[0]
    tamount=b+amount
    sql="update amount set TotalBalance={} where Acc_no={}".format(tamount,Acc_no)
    c.execute(sql)
    con.commit()
    main()

def withdraw():
    print("**************WITHDRAW AMOUNT**************")
    amount=int(input("Enter Withdraw Amount :- "))
    Acc_no=input("Enter Account No :- ")
    a="select TotalBalance from amount where Acc_no={}".format(Acc_no)
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchone()
    b=myresult[0]
    tamount=b-amount
    sql="update amount set TotalBalance={} where Acc_no={}".format(tamount,Acc_no)
    c.execute(sql)
    con.commit()
    main()

def balance():
    print("**************BALANCE ENQUIRY**************")
    ac=input("\tEnter Account No :- ")
    a="select TotalBalance from amount where Acc_no={}".format(ac)
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchone()
    print("******************BALANCE*******************")
    print("\tCurrent Balance is RS",myresult[0])
    main()

def details():
    print("***********CHECK ACCOUNT DETAILS************")
    ac=input("\tEnter Account No :- ")
    a="select * from amount where Acc_no={}".format(ac)
    c=con.cursor()
    c.execute(a)
    myresult=c.fetchone()
    print("******************DETAILS*******************")
    
    for i in myresult:
        print(i,end="\t|\t")
        
    main()

def close():
    ac=input("\tEnter Account No :- ")
    sql1="delete from account where Acc_no={}".format(ac)
    sql2="delete from amount where Acc_no={}".format(ac)
    c=con.cursor()
    c.execute(sql2)
    c.execute(sql1)
    con.commit()
    print("\n......Account Deleted Successfully........\n")
    main()

def main():
    print("""\n
********************************************
<><><><><><><><>[  MAIN MENU ]<><><><><><><>
********************************************
            1.OPEN NEW ACCOUNT
            2.DEPOSIT AMOUNT
            3.WITHDRAW AMOUNT
            4.BALANCE ENQUIRY
            5.ACCOUNT DETAIL
            6.CLOSE ACCOUNT
********************************************
********************************************
    \n""")
    choice=input("Enter Your Choice >>> ")
    if(choice=='1'):
        openAcount()
    elif(choice=='2'):
        deposit()
    elif(choice=='3'):
        withdraw()
    elif(choice=='4'):
        balance()
    elif(choice=='5'):
        details()
    elif(choice=='6'):
        close()
    else:
        print("Invalid Choice........")
        main()
main()
