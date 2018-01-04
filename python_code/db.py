import pymysql

db = pymysql.connect("localhost","root","root","ost")
cursor = db.cursor()
# cursor.execute("SELECT VERSION()")
# data = cursor.fetchone()
# print ("Database version : %s " % data)

sql = "SELECT * FROM ost_submission"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      seat = row[2]
      name = row[3]
      filepath = row[4]
      # Now print fetched result
      print ("seat = %s,name = %s,filepath = %s" % \
             (seat, name, filepath))
except:
   print ("Error: unable to fetch data")

db.close()


# To Create DB

#CREATE DB

# Drop table if it already exist using execute() method.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # Create table as per requirement
# sql = """CREATE TABLE EMPLOYEE (
#    FIRST_NAME  CHAR(20) NOT NULL,
#    LAST_NAME  CHAR(20),
#    AGE INT,
#    SEX CHAR(1),
#    INCOME FLOAT )"""
#
# cursor.execute(sql)


# Insert Database
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
   LAST_NAME, AGE, SEX, INCOME)
   VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()
