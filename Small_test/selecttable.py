import pymysql

db = pymysql.connect('localhost','python_test','123456','mypython')

cursor = db.cursor()

sql = "SELECT FIRST_NAME,LAST_NAME,AGE,SEX,INCOME FROM EMPLOYEE WHERE INCOME > %f" %(2200.15)

try:
	cursor.execute(sql)
	results = cursor.fetchall()
	for row in results:
		fname = row[0]
		lname = row[1]
		age = row[2]
		sex = row[3]
		income = row[4]
		print('%s %s %d %c %.2f' %(fname,lname,age,sex,income))
except:
	print('here is an exception')

db.close()