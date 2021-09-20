import MySQLdb as mysql
import time
db = mysql.connect(host = "localhost",user="root",passwd="123",db="INFORMATION_SCHEMA")
cur = db.cursor()

while True:
	cur.execute('SHOW STATUS')
	res = cur.fetchall()
	print(res)
	for i in res:
		print(i)
		print("____________________________________________________________________________")
	time.sleep(1)
db.close()
