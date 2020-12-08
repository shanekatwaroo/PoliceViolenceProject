import pymysql
import csv
import itertools 

connection = pymysql.connect(host='127.0.01',
                            user = 'root',
                            password = '123',
                            db='project',
                            cursorclass=pymysql.cursors.DictCursor)
print(connection)

check = "DROP TABLE IF EXISTS PovertyLevel" #for repeating code to fix errors
cursor = connection.cursor()
cursor.execute(check)
sql = """CREATE TABLE PovertyLevel (
           state varchar(32),
           city varchar(100),
           poverty_rate float);"""   #creating table and columns  with data types
cursor.execute(sql)
connection.commit()
sql2 = "show tables;"
cursor.execute(sql2)
result = cursor.fetchone()
print(result)

with open('PercentagePeopleBelowPovertyLevel.csv', encoding = 'latin1') as csv_file:    #opening csv
   csvfile = csv.reader(csv_file, delimiter=',')#using csv reader to separate values(in this case 'row') by a comma
   all_values = []  #creating a list of all values based on for loop below
   next(csvfile) #skips header row
   for row in csvfile:
       flag = True
       if row[2] == "-":
           flag = False
       if flag == True:
           value = (row[0],row[1],row[2])  #row[column number]
           all_values.append(value) #appending values to list
       
sql3 = ("INSERT INTO PovertyLevel VALUES(%s,%s,%s);")
cursor.executemany(sql3,all_values) #inserting values from list into table
connection.commit()
connection.close()




