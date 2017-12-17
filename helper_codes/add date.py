from random import randint
import datetime
import pymysql.cursors
import pandas as pd
import sys
import random
sys.__stdout__ = sys.stdout
counter=0
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='balbir1012',
                             db='myproject',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor=connection.cursor()
for i in  range(26616,29617):
 startdate=datetime.date(2017,9,28)
 date=startdate+datetime.timedelta(randint(1,14))
 print(i)
 cursor.execute("""
            UPDATE library_searcH SET date_of_search=%s where id=%s
            """,[date,i])
connection.commit()
