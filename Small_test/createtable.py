import pymysql

db = pymysql.connect('localhost','python_test','123456','mypython')

cursor = db.cursor()

cursor.execute('DROP TABLE IF EXISTS EMPLOYEE')

sql = """CREATE TABLE EMPLOYEE (
		 FIRST_NAME CHAR(20) NOT NULL,
		 LAST_NAME CHAR(20),
		 AGE INT,
		 SEX CHAR(1),
		 INCOME FLOAT)"""

cursor.execute(sql)

db.close()
