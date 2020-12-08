import pymysql
import csv
import itertools 

connection = pymysql.connect(host='127.0.01',
                            user = 'root',
                            password = '123',
                            db='project',
                            cursorclass=pymysql.cursors.DictCursor)
print(connection)

check = "DROP TABLE IF EXISTS Shootings" #for repeating code to fix errors
cursor = connection.cursor()
cursor.execute(check)
sql = """CREATE TABLE Shootings ( 
           id  integer NOT NULL,
           name  varchar(32),
           date  varchar(32),
           manner_of_death  varchar(50),
           armed  varchar(32),
           age integer,
           gender varchar(32),
           race varchar(32),
           city varchar(32),
           state varchar(32),
           mental_illness varchar(32),
           threat_level varchar(32),
           flee varchar(32),
           body_camera varchar(32),
           PRIMARY KEY (id));"""   #creating table and columns  with data types
cursor.execute(sql)
connection.commit()
sql2 = "show tables;"
cursor.execute(sql2)
result = cursor.fetchone()
print(result)

with open('shootings_wash_post.csv') as csv_file:    #opening csv
   csvfile = csv.reader(csv_file, delimiter=',')#using csv reader to separate values(in this case 'row') by a comma
   all_values = []  #creating a list of all values based on for loop below
   next(csvfile) #skips header row
   for row in csvfile:
       flag = True #each iteration of the for loop resets flag to true
       if not row[5]:   #if row is blank, omit
           flag = False
       if not row[6]:
           flag = False
       if not row[7]:
           flag = False
       if not row[3]:
           row[3]= 'other'
       if flag == True: #if the flag remains true when testing value(it meets the criteria), then it is added to the values list
           value = (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9],row[10],row[11],row[12],row[13])  #row[column number]
           all_values.append(value) #appending values to list
       
sql3 = ("INSERT INTO Shootings VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);")
cursor.executemany(sql3,all_values) #inserting values from list into table
connection.commit()
connection.close()



