import pymysql

employeeList = [('LIN','FEI',20,'M',2000.00),
				('SUN','BO',35,'M',2500.00),
                ('LI','SHIQI',47,'M',17803.00)]

db = pymysql.connect('localhost','python_test','123456','mypython')

cursor = db.cursor()

for s in employeeList:
	sql = "INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME) \
			values('%s','%s','%d','%c','%f')" % (s[0],s[1],s[2],s[3],s[4])
	try:
		cursor.execute(sql)
	except:
		db.rollback()

db.commit()

db.close()