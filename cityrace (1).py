import pymysql
import csv
import itertools 

connection = pymysql.connect(host='127.0.01',
                            user = 'root',
                            password = '123',
                            db='project',
                            cursorclass=pymysql.cursors.DictCursor)
print(connection)

check = "DROP TABLE IF EXISTS ShareRace" #for repeating code to fix errors
cursor = connection.cursor()
cursor.execute(check)
sql = """CREATE TABLE ShareRace (
           state varchar(32),
           city varchar(100),
           share_white float,
           share_black float,
           share_native_american float,
           share_asian float,
           share_hispanic float);"""   #creating table and columns  with data types
cursor.execute(sql)
connection.commit()
sql2 = "show tables;"
cursor.execute(sql2)
result = cursor.fetchone()
print(result)

with open('ShareRaceByCity.csv') as csv_file:    #opening csv
   csvfile = csv.reader(csv_file, delimiter=',')#using csv reader to separate values(in this case 'row') by a comma
   all_values = []  #creating a list of all values based on for loop below
   next(csvfile) #skips header row
   for row in csvfile:
       flag = True
       if row[2] == "(X)":
           flag = False
       elif row[3] =="(X)":
           flag = False
       elif row[4] =="(X)":
           flag = False
       elif row[5] =="(X)":
           flag = False
       elif row[6] =="(X)":
           flag = False
       if flag == True:
           value = (row[0],row[1],row[2],row[3],row[4],row[5],row[6])  #row[column number]
           all_values.append(value) #appending values to list
       
sql3 = ("INSERT INTO ShareRace  VALUES(%s,%s,%s,%s,%s,%s,%s);")
cursor.executemany(sql3,all_values) #inserting values from list into table
connection.commit()
connection.close()



