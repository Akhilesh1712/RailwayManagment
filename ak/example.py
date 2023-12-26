#firstly you have to create your database(means data) then connect it to this
import mysql.connector

conn = mysql.connector.connect(host='localhost', password='password', user='root')

if conn.is_connected():
	print("connection established...")
import pandas as pd
import mysql.connector 



conn= mysql.connector.connect(host='localhost',user='root',password='Password',database='Databasename')
if conn.is_connected():
    print('successfully connected')


    





def menu():




    print()
    print("************************************************************************************************************************************")
    print("                                        RAIWAY MANAGEMENT SYSTEM                                                                    ")
    print("1. Create Table Passengers")
    print("2. Add new Passenger Detail")
    print("3. Create Table traindetail")
    print("4. Add new in Train Detail")
    print("5. Show All from train detail")
    print("6. Show All from Passenger Table")
    print("7. Show PNR NO.")
    print("8. Rservation of Ticket")
    print("9. Cancellation of Reservation")

menu()




def create_passengers():
    c1=conn.cursor()
    c1.execute('create table if not exist passengers( pname varchar(30) not null, age varchar(25) not null, trainno varchar(27) unique, noofpas varchar(26) not null,cls varchar(35) not null, destination varchar(24) not null,amt varchar(28) not null,status varchar(28) not null,pnrno varchar(20) not null')
    print('table passengers created')



def add_passengers():
    c1=conn.cursor()
    L=[]
    pname=input("enter name:")
    L.append(pname)
    age=input("enter age:")
    L.append(age)
    trainno=input("Enter teain no:")
    L.append(trainno)
    noofpas=input("enter no of passengers:")
    L.append(noofpas)
    cls=input("enter class:")
    L.append(cls)
    destination=input("enter destination:")
    L.append(destination)
    amt=input("enter amount:")
    L.append(amt)
    status=input("enter status:")
    L.append(status)
    pnrno=input("enter pnrno:")
    L.append(pnrno)
    pas=(L)
    sql="insert into passengers(pname,age,trainno,noofpas,cls,destination,amt,status,pnrno)values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,pas)
    conn.commit()
    print('Record of Passenger inserted')
    df=pd.read_sql("select * from passengers",conn)
    print(df)





def create_traindetails():
    c1=conn.cursor()
    c1.execute('create table if not exists traindetails( tname varchar(30),tnum varchar(25),source varchar(26),destination varchar(29),fare varchar(20),ac1 varchar(26),ac2 varchar(26),alp varchar(28)')
    print('table traindetails created')


def add_traindetails():
    c1=conn.cursor()
    df=pd.read_sql("select * from traindetails",conn)
    print(df)
    L=[]
    tname=input("Enter the train name:")
    L.append(tname)
    tnum=input("Enter number of train:")
    L.append(tnum)
    source=input("enter source of train:")
    L.append(source)
    destination=input("enter your destination:")
    L.append(destination)
    fare=input("Enter the fare:")
    L.append(fare)
    ac1=input("Enter no of seats in ac1:")
    L.append(ac1)
    ac2=input("Enter  no of seats in ac2:")
    L.append(ac2)
    slp=input("Enter no of seats in slp:")
    L.append(slp)
    f=(L)
    sql="insert  into traindetails(tname,tnum,source,destination,fare,ac1,ac2,slp)values(%s,%s,%s,%s,%s,%s,%s,%s)"
    c1.execute(sql,f)
    conn.commit()
    print('Record inserted in the train detail')


def showtraindetails():
    print("ALL TRANS DETAIL")
    df=pd.read_sql("select * from train detail")
    print(df)



def showpassengers():
  print("All PASSENGERS DETAIL")
  df=pd.read_sql("select * from passengers",conn)
  print(df)


def disp_pnrno():
    print("PNR status")
    a=input("Enter trian no:")
    qry="select pname,status from passengers where trainno=%s;"%(a)
    df=pd.read_sql(qry,conn)
    print(df)


def ticketreservation():
    print("WE HAVE THE FOLLOWING SEATS FOR YOU")
    print("TNAME is 1 FOR MANALI EXPERSS FROM NEW DELHI")
    print()
    print("1. FIRST CLASS AC RS 6000 PER PERSON")
    print("2. SECOND CLASS AC RS 5000 PER PERSON")
    print("3. THIRD CLASS AC RS 4000 PER PERSON")
    print("4. SLEEPER RS 3000 PER PERSON")
    print()
    print("TNAME IS 2 FOR HHONOLLULU EXPRESS FROM NEW DELHI")
    print()
    print("1. FIRST CLASS AC RS 60000 PER PERSON")
    print("2. SECOND CLASS AC RS 50000 PER PERSON")
    print("3. THIRD CLASS AC RS 40000 PER PERSON")
    print("4. SLEEPER RS 30000 PER PERSON")


    tname=input("ENTER YOUR CHOICE OF TRAIN NAME--->")
    print(tname)
    x=int(input("ENTER THE CHOICE OF YOUR TICKET PLEASE---->"))
    n=int(input("HOW MANY TICKET YOU NEED:"))


    if (x==1):
        print("YOUR HAVE CHOOSEN FRIST CLASS AC ")
        s=6000*n
    elif(x==2):
        print("YOU HAVE CHOOSEN SECOND CLASS AC")
        s=5000*n
    elif(x==3):
        print("YOU HAVE CHOOSEN THIRD CLASS AC")
        s=4000*n
    elif(x==4):
        print("YOU HAVE CHOOSEN SLEEPER ")
        s=3000*n
    else:
        print("INVALID !!!!!!!!")
    print("YOUR TOTAL PRICE IS =",s,"\n")


    if (x==1):
        print("YOUR HAVE CHOOSEN FRIST CLASS AC ")
        s=60000*n
    elif(x==2):
        print("YOU HAVE CHOOSEN SECOND CLASS AC")
        s=50000*n
    elif(x==3):
        print("YOU HAVE CHOOSEN THIRD CLASS AC")
        s=40000*n
    elif(x==4):
        print("YOU HAVE CHOOSEN SLEEPER ")
        s=30000*n
    else:
        print("INVALID !!!!!!!!")
    print("YOUR TOTAL PRICE IS =",s,"\n")


def cancel():
    print("WANT TO CANCELL")
    df=pd.read_sql("select * from passengers",conn)
    print(df)
    mc=conn.cursor()
    mc.execute("update passengers set status='cancell' where pnrno='G23HF'")
    df=pd.read_sql("select * from passengers",conn)
    print(df)


opt=""
opt=int(input("ENTER YOUR CHOICE"))
if opt==1:
    create_passengers()
elif opt==2:
    add_passengers()
elif opt==3:
     create_traindetails()
elif opt==4:
    add_traindetails()             
elif opt==5:
    showtraindetails()
elif opt==6:
    showpassengers()
elif  opt==7:
    disp_pnrno()
elif opt==8:
    ticketreservation()
else:
    print("INVALID !!!!!!")                

