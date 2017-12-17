import pymysql.cursors
import pandas as pd
import sys
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
i=cursor.fetchall()
users=[]
for j in i:
   users.append(j['User_name'])
print(users)

def add_tech(name,department,subject,author):
        global counter
        cursor=connection.cursor()
        name=name.lower()
        department=department.lower()
        cursor.execute("""
            SELECT * from library_books_technical WHERE Book_name=%s
            """,[name])
        b=cursor.fetchall()
        n=users[counter%5]
        counter+=1
        flag=0
        if(len(b)==0):
            a=[name,author,department,subject]
            cursor.execute("""
                        INSERT INTO library_books_technical(Book_name,Author_name,Department,Subject,No_of_copies) VALUES (%s,%s,%s,%s,1)
                        """,a)
            m=[name,'tech',n]
            cursor.execute("""
                        INSERT INTO library_Book_record(Book_name,Type,Lender_id) VALUES (%s,%s,%s)""",m)
            flag=1
        if(flag==1):
            return
        cursor.execute("""
            UPDATE library_Books_technical SET No_of_copies=No_of_copies+1 WHERE Book_name=%s
            """,[name])
        m=[name,'tech',n]
        cursor.execute("""
                        INSERT INTO library_Book_record(Book_name,Type,Lender_id) VALUES (%s,%s,%s)
                        """,m)
        return
def add_non_tech(name,department,subject,author):
        global counter
        cursor=connection.cursor()
        name=name.lower()
        department=department.lower()
        cursor.execute("""
            SELECT * from library_books_non_technical WHERE Book_name=%s
            """,[name])
        b=cursor.fetchall()
        n=users[counter%5]
        counter+=1
        flag=0
        if(len(b)==0):
            a=[name,author,department,subject]
            cursor.execute("""
                        INSERT INTO library_books_non_technical(Book_name,Author_name,Department,Subject,No_of_copies) VALUES (%s,%s,%s,%s,1)
                        """,a)
            m=[name,'non',n]
            cursor.execute("""
                        INSERT INTO library_Book_record(Book_name,Type,Lender_id) VALUES (%s,%s,%s)""",m)
            flag=1
        if(flag==1):
            return
        cursor.execute("""
            UPDATE library_Books_non_technical SET No_of_copies=No_of_copies+1 WHERE Book_name=%s
            """,[name])
        m=[name,'non',n]
        cursor.execute("""
                        INSERT INTO library_Book_record(Book_name,Type,Lender_id) VALUES (%s,%s,%s)
                        """,m)
        return

dept=['computer','mechanical','electronics']
df = pd.read_excel('books_new.xlsx','books_new')
for i in range(0,185):
  if df.iat[i,2] == 'tech':
    add_tech(df.iat[i,0],dept[counter%3],df.iat[i,3],df.iat[i,1])
  elif df.iat[i,2]=='fiction':
      add_non_tech(df.iat[i,0],'fiction',df.iat[i,3],df.iat[i,1])
  elif df.iat[i,2]=='nonfiction':
       add_non_tech(df.iat[i,0],'non fiction',df.iat[i,3],df.iat[i,1])
  elif df.iat[i,2]=='science':
        add_tech(df.iat[i,0],dept[counter%3],df.iat[i,3],df.iat[i,1])
  else:
        add_non_tech(df.iat[i,0],'magazines',df.iat[i,3],df.iat[i,1])
connection.commit()

