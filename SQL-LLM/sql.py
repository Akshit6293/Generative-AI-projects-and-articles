#!/usr/bin/env python
# coding: utf-8

# # SQL-LLM APP
# 

# In[2]:


import sqlite3

#connect to sqlite
connection = sqlite3.connect("student.db")

#create a cursor object to insert,record,create table,retrieve
cursor = connection.cursor()

table_info = """
create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25), 
SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

#let's insert records in the table

cursor.execute("""Insert Into STUDENT VALUES("Akshit", "Data Science", "A", 90) """)
cursor.execute("""Insert Into STUDENT VALUES("Dipanshu", "Data Science", "B", 100) """)
cursor.execute("""Insert Into STUDENT VALUES("Darius", "Data Science", "A", 86) """)
cursor.execute("""Insert Into STUDENT VALUES("Awni", "Devops", "A", 50) """)
cursor.execute("""Insert Into STUDENT VALUES("Salil", "Devops", "A", 75) """)
cursor.execute("""Insert Into STUDENT VALUES("Himanshu", "Devops", "A", 65) """)
cursor.execute("""Insert Into STUDENT VALUES("Kartik", "Devops", "A", 45) """)
cursor.execute("""Insert Into STUDENT VALUES("Paras", "Frontend", "A", 55) """)
cursor.execute("""Insert Into STUDENT VALUES("Aniket", "Frontend", "A", 95) """)
cursor.execute("""Insert Into STUDENT VALUES("Akanksha", "Frontend", "A", 25) """)


## Display all records
print("The inserted records are:")

data = cursor.execute(""" Select * from STUDENT """)
for rows in data:
    print(rows)
    
## close the connection
connection.commit()
connection.close()


# In[ ]:




