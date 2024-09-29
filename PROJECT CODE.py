import mysql.connector as sql
mydb=sql.connect(host='localhost',user='root',passwd='rrithik@006')
mycursor=mydb.cursor()

#mycursor.execute('create database library')
mycursor.execute('use library')
'''mycursor.execute('create table users(username varchar(30),passwd varchar(30))')
mycursor.execute("insert into users values('Rithik','rithik785')")
mycursor.execute("insert into users values('Arun Vijay','arun134')")
mycursor.execute("insert into users values('Griffin joe','joe630')")
mydb.commit()
mycursor.execute("create table member(mid varchar(20) primary key,name varchar(50),email varchar(50),phone varchar(10))")
mycursor.execute("create table book(id varchar(20) primary key,title varchar(20),author varchar(20),publisher varchar(50),cost int)")
mycursor.execute("create table issue(mid varchar(20),bid varchar(20),dateofissue date)")
mycursor.execute("create table issuelog(mid varchar(20),bid varchar(20),dateofissue date,dateofreturn date)")
mydb.commit()'''

def login():
    print('-'*40)
    print('\t Library Management System')
    print('-'*40)
    print('\t Login')
    user=input('Enter User Name : ')
    passwd=input('Enter Password : ')
    qry="select * from users where username='{}'and passwd='{}' ".format(user,passwd)
    mycursor.execute(qry)
    myrecord=mycursor.fetchall()
    print('-'*50)
    if len(myrecord)==0:
        print('Invaild User name or password')
        print('-'*50)
        return False
    else:
        print('Access Granted ')
        print('-'*50)
        return True
 



def addmember():
    print('-'*50)
    print("\t ADDING  A NEW MEMBER")
    print('-'*50)
    mid=input("Enter Member Id : ")
    name=input("Enter Member Name : ")
    email=input("Enter Email : ")
    phone=input("Enter  Phone Number : ")
    qry="insert into member values('{}','{}', '{}','{}')".format(mid,name,email,phone)
    mycursor.execute(qry)
    mydb.commit()
    print("Member Added Successfully")

def showmember():
    qry='select * from member'
    mycursor.execute(qry)
    myrecord=mycursor.fetchall()
    print('-'*40)
    print("List of Members")
    print('-'*40)
    print("Id    Name       Email                                Phone")
    for i in myrecord:
        print(i[0],'    ',i[1],'    ',i[2],'    ',i[3])
        print('-'*40)

def delmember():
    print('-'*40)
    print('\t Deleting a Member')
    print('-'*40)
    mid=input('Enter Member Id : ')
    qry="delete from member where mid='{}' ".format(mid)
    mycursor.execute(qry)
    mydb.commit()
    print('Member Deleted Succesfully')

def addbook():
    print('-'*50)
    print('\t Adding A New Book')
    bid=input("Enter Book Id :")
    title=input("Enter Book Title :")
    author=input("Enter Author Name : ")
    publisher=input("Enter Publisher : ")
    cost=int(input("Enter Cost of the Book : "))
    qry="insert into book values('{}','{}','{}','{}',{})".format(bid,title,author,publisher,cost)
    mycursor.execute(qry)
    mydb.commit()
    print('Book Added Successfully')

def showbook():
    mycursor.execute('select * from book')
    myrecord=mycursor.fetchall()
    print('-'*50)
    print("\t    Book Details ")
    print('-'* 50)
    print("Id         Title       Author            Publisher       Cost  ")
    for i in myrecord:
        print(i[0],'      ',i[1],'      ',i[2],'        ',i[3],'        ',i[4])

def delbook():
    print('-'* 40)
    print('\t Deleting A Book')
    print('-'*40)
    bid=input('Enter Book Id : ')
    qry="delete from book where  id='{}' ".format(bid)
    mycursor.execute(qry)
    mydb.commit()
    print('Book Deleted Successfully')


def showissued():
    mycursor.execute('select * from issue')
    myrecord=mycursor.fetchall()
    print('        List Of Issued Book')
    print('-' * 40)
    print('Member  BookId      Issued Date')
    for i in myrecord:
        print(i[0],'         ',i[1],'        ',i[2])
    print('-'*40)


def showreturn():
    mycursor.execute('select * from issuelog')
    myrecord=mycursor.fecthall()
    print('        List of Returned Books')
    print('-'*40)
    print('Member    BookId     Issued Date      Return Date ')
    for i in myrecord:
        print(i[0],'   ',i[1],'       ',i[2],'       ',i[3])
    print('-'*40)

def issuebook():
    bid=input('Enter  the book id to be issued  : ')
    qry="select *from issue where bid='{}'  ".format(bid)
    mycursor.execute(qry)
    myrecord=mycursor.fetchall()
    if len(myrecord)==0:
        mid=input('Enter Member Id: ')
        doi=input('Enter the date of issue  : ')
        quy="insert into issue values('{}','{}','{}')".format(mid,bid,doi)
        mycursor.execute(quy)
        mydb.commit()
        print('-'*40)
        print('Book Issued Successfully')
        print('-'*40)
    else:
        print('-'*40)
        print('   Sorry!  The Book is not Available')
        print('-'*40)


def returnbook():
    bid=input('Enter the Book Id : ')
    mid=input('Enter the Member Id : ')
    qry="select dateofissue from issue where bid='{}' and mid='{}' ".format(bid,mid)
    mycursor.execute(qry)
    myrecord=mycursor.fetchall()
    if len(myrecord)==0:
        print('-'*40)
        print('This Book is not Issued to This Member')
        print('-'*40)
    else:
        dort=input('Enter the date of return : ')
        q="delete from issue where bid='{}' and mid='{}' ".format(bid,mid)
        mycursor.execute(q)
        mydb.commit()
        q="insert into issuelog values('{}','{}','{}','{}')".format(bid,mid,myrecord[0],dort)
        mycursor.execute(q)
        mydb.commit()
        print('Book Returned')

if login():
    while True:
        print('-'*50)
        print('\t Choose an Operation')
        print('-'*50)
        print("Press 1  - Add a New Member")
        print("Press 2 - Delete an existing Member")
        print("Press 3 - Show All Members")
        print("Press 4 - Add a New Book")
        print("Press 5 - Delete  an Existing Book")
        print("Press 6 - Show All Books")
        print("Press 7 - Issue a Book ")
        print("Press 8 - Return a Book ")
        print("Press 9 - Show Issued  Books ")
        print("Press 10 - Show Returned Books")
        print("Press 11 - Quit")
        ch=int(input('Enter Your Choice :'))
        if ch==1:
            addmember()
        elif ch==2:
            delmember()
        elif ch==3:
            showmember()
        elif ch==4:
            addbook()
        elif ch==5:
            delbook()
        elif ch==6:
            showbook()
        elif ch==7:
            issuebook()
        elif ch==8:
            returnbook()
        elif ch==9:
            showissued()
        elif ch==10:
            showreturn()
        elif ch ==11:
            break

















 
