import mysql.connector

user="root"
password=""
port=3306
database="python_ship_reservation_system"

def select(q):
	cnx=mysql.connector.connect(user=user,password=password,host="localhost",database=database,port=port)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	result=cur.fetchall()
	cur.close()
	cnx.close()
	return result

def insert(q):
	cnx=mysql.connector.connect(user=user,password=password,host="localhost",database=database,port=port)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.lastrowid
	cur.close()
	cnx.close()
	return result

def update(q):
	cnx=mysql.connector.connect(user=user,password=password,host="localhost",database=database,port=port)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.rowcount
	cur.close()
	cnx.close()
	return result

def delete(q):
	cnx=mysql.connector.connect(user=user,password=password,host="localhost",database=database,port=port)
	cur=cnx.cursor(dictionary=True)
	cur.execute(q)
	cnx.commit()
	result=cur.rowcount
	cur.close()
	cnx.close()
	return result