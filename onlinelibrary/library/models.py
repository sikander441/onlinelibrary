from django.db import models
from django.db import connection
# Create your models here.



class UserManager(models.Manager):
    def get_name(self,user_name):
        cursor=connection.cursor()
        cursor.execute("""
            SELECT Name_of_user from library_User WHERE User_name=%s
            """,[user_name])
        a=cursor.fetchall()
        a=a[0]
        a=a[0]
        return a
    def get_phone(self,user_name):
        cursor=connection.cursor()
        cursor.execute("""
            SELECT Phone_number from library_User WHERE User_name=%s
            """,[user_name])
        a=cursor.fetchall()
        a=a[0]
        a=a[0]
        return a
    def get_email(self,user_name):
        cursor=connection.cursor()
        cursor.execute("""
            SELECT email_address from library_User WHERE User_name=%s
            """,[user_name])
        a=cursor.fetchall()
        a=a[0]
        a=a[0]
        return a
    def add_user1(self,name,user_name,email,phone,password):
        a=[user_name,name,phone,email,password]
        cursor=connection.cursor()
        cursor.execute("""
            INSERT INTO library_User VALUES (%s,%s,%s,%s,%s)
            """,a)
        return

    def logout(self):
        cursor=connection.cursor()
        cursor.execute("""
            DELETE  FROM library_Curr_user """)

        return
    def check_user(self,user_name,password):
        a=[user_name,password]
        cursor=connection.cursor()
        cursor.execute("""
            SELECT * FROM  library_User WHERE User_name=%s and Password= %s
            """,a)
        b=cursor.fetchall()
        if (len(b)==0):
            return 0

        cursor.execute("""
            SELECT * FROM library_Curr_user """)
        c=cursor.fetchall()
        if(len(c)>0):
            return -1
        cursor.execute("""
            INSERT INTO library_Curr_user values (%s)
            """,[user_name])
        return 1

class Curr_userManager(models.Manager):
    def get_user_name(self):
        cursor=connection.cursor()
        cursor.execute(""" SELECT * FROM  library_Curr_user;
        """)
        c=cursor.fetchall()
        if (len(c)==0):
            return " "
        c=c[0]
        c=c[0]
        return c
class Book_recordManager(models.Manager):
    def get_books(self,user_n,type_b):
        a=[type_b,user_n]
        cursor=connection.cursor()
        cursor.execute("""
            SELECT Book_name from library_Book_record WHERE Type=%s AND Lender_id=%s
            """,a)
        b=cursor.fetchall()
        c=[]
        for i in b:
            c.append(i[0])
        return c

    def delete(self,user_name,book):
        a=[user_name,book]
        cursor=connection.cursor()
        cursor.execute("""
            DELETE from library_Book_record WHERE Lender_id=%s AND Book_name=%s
            """,a)
        return


class Books_technicalManager(models.Manager):
    def get_books(self,name):
        cursor=connection.cursor()

        name=name.lower()
        name='%'+name+'%'
        cursor.execute("""
            SELECT Book_name from library_Books_technical WHERE Book_name=%s
            """,[name])
        a=cursor.fetchall()
        c=[]
        for i in a:
            b=i[0]
            c.append(b)
        return c
    def add(self,name,department,subject,author):
        cursor=connection.cursor()
        name=name.lower()
        department=department.lower()
        cursor.execute("""
            SELECT * from library_Books_technical WHERE Book_name=%s
            """,[name])
        b=cursor.fetchall()
        cursor.execute("""
            SELECT User_name from library_Curr_user
            """)
        n=cursor.fetchall()
        n=n[0]
        n=n[0]
        flag=0
        if(len(b)==0):
            a=[name,author,department,subject]
            cursor.execute("""
                        INSERT INTO library_Books_technical(Book_name,Author_name,Department,Subject,No_of_copies) VALUES (%s,%s,%s,%s,1)
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

    def update_no_of_books(self,book):
        cursor=connection.cursor()
        cursor.execute("""
            UPDATE library_Books_technical SET No_of_copies=No_of_copies-1 WHERE Book_name=%s
            """,[book])
        return


class Books_non_technicalManager(models.Manager):
    def get_books(self,name):
        cursor=connection.cursor()

        name=name.lower()
        name='%'+name+'%'
        cursor.execute("""
            SELECT Book_name from library_Books_non_technical WHERE Book_name=%s
            """,[name])
        a=cursor.fetchall()
        c=[]
        for i in a:
            b=i[0]
            c.append(b)
        return c


    def add(self,name,department,subject,author):
        cursor=connection.cursor()
        name=name.lower()
        department=department.lower()
        cursor.execute("""
            SELECT * from library_Books_non_technical WHERE Book_name=%s
            """,[name])
        b=cursor.fetchall()
        cursor.execute("""
            SELECT User_name from library_Curr_user
            """)
        n=cursor.fetchall()
        n=n[0]
        n=n[0]
        flag=0
        if(len(b)==0):
            a=[name,author,department,subject]
            cursor.execute("""
                        INSERT INTO library_Books_non_technical(Book_name,Author_name,Department,Subject,No_of_copies) VALUES (%s,%s,%s,%s,1)
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

    def update_no_of_books(self,book):
        cursor=connection.cursor()
        cursor.execute("""
            UPDATE library_Books_non_technical SET No_of_copies=No_of_copies-1 WHERE Book_name=%s
            """,[book])
        return

class SearchManager(models.Manager):
    def add(self,Book,department,types,user):
        cursor=connection.cursor()
        a=[Book,department,types,user]
        cursor.execute("""INSERT INTO library_search(Book_name,Department,Type,User_name) VALUES (%s,%s,%s,%s)""",a)
        return

class User(models.Model):
    User_name=models.CharField(max_length=200,primary_key=True)
    Name_of_user=models.CharField(max_length=200)
    Phone_number=models.CharField(max_length=15)
    email_address=models.CharField(max_length=200)
    Password=models.CharField(max_length=100,null=False,blank=False)
    objects=UserManager()
    def __str__(self):
        return self.User_name

class Books_technical(models.Model):
    Book_name=models.CharField(max_length=200)
    Author_name=models.CharField(max_length=200)
    Department=models.CharField(max_length=200)
    Subject=models.CharField(max_length=200)
    No_of_copies=models.IntegerField(default=0)
    objects=Books_technicalManager()
    def __str__(self):
        return self.Book_name

class Books_non_technical(models.Model):
    Book_name=models.CharField(max_length=200)
    Author_name=models.CharField(max_length=200)
    Department=models.CharField(max_length=200)
    Subject=models.CharField(max_length=200)
    No_of_copies=models.IntegerField(default=0)
    objects=Books_non_technicalManager()
    def __str__(self):
        return self.Book_name

class Book_record(models.Model):
    Book_name=models.CharField(max_length=200)
    Type=models.CharField(max_length=200)
    Lender=models.ForeignKey(User, on_delete=models.CASCADE)
    objects=Book_recordManager()
    def __str__(self):
        return self.Book_name

class Curr_user(models.Model):
    User_name=models.CharField(max_length=200,primary_key=True)
    objects=Curr_userManager()
    def __str__(self):
        return self.User_name
class Search(models.Model):
    Book_name=models.CharField(max_length=200)
    Department=models.CharField(max_length=200)
    Type=models.CharField(max_length=200)
    User_name=models.CharField(max_length=200)
    objects=SearchManager()
