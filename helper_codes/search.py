import pymysql.cursors
import pandas as pd
import sys
import random
from random import randint
import datetime
sys.__stdout__ = sys.stdout
counter=0
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='balbir1012',
                             db='myproject',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor=connection.cursor()
cursor.execute("""Select * from library_user; """) 
x=cursor.fetchall()
users=[]
for j in x:
   users.append(j['User_name'])
print(users)



cursor.execute("""select *from library_book_record """)
all_books=cursor.fetchall()
for _ in range(40000):
 i=random.randrange(1,3)
 name=all_books[i]['Book_name']
 uname=users[counter%5]
 counter+=1
 typ=all_books[i]['Type']
 if typ=='tech':
  cursor.execute("""
            SELECT Department from library_books_technical WHERE Book_name=%s
            """,[name])
  dept=cursor.fetchone()['Department']
 else: 
  cursor.execute("""
            SELECT Department from library_books_non_technical WHERE Book_name=%s
            """,[name])
  dept=cursor.fetchone()['Department']
 startdate=datetime.date(2015,9,15)
 date=startdate+datetime.timedelta(randint(1,720))

 a=[name,dept,typ,uname,date]

 cursor.execute("""INSERT INTO library_search(Book_name,Department,Type,User_name,date_of_search) VALUES (%s,%s,%s,%s,%s)
                        """,a)

connection.commit()


