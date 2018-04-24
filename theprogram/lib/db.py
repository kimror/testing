import mysql.connector


def connect():

	try:
		cnx = mysql.connector.connect(  user='test', password='intelligence',
						host='localhost',
						database='test')
	except mysql.connector.error.Error as err:
		if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
			print("Wrong username or password")
		elif err.errno == errorcode.ER_BAD_DB_ERROR:
			print("Database does not exist")
		else:
			print(err)
	else:
		return cnx

def disconnect(cnx):

	cnx.close()
##	print("Maybe disconnected")

def insert(external_id, title, description, link, published_date):

	cnx = connect()

	cursor = cnx.cursor()

	query = ("INSERT INTO rss_items (external_id, title, description, link, published_date) VALUES (%s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE external_id = '" + external_id + "'")

	data = (external_id, title, description, link, published_date)

	cursor.execute(query, data)

	cnx.commit()

	cursor.close()

	disconnect(cnx)

def insert2(external_id, title, text):

	cnx = connect()

	cursor = cnx.cursor()

	query = ("INSERT INTO articles (external_id, title, text) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE external_id = '" + external_id + "'")

	data = (external_id, title, text)

	cursor.execute(query, data)

	cnx.commit()

	cursor.close()

	disconnect(cnx)

def select():

	cnx = connect()

	cursor = cnx.cursor()

	query = ("select r.external_id as external_id from rss_items r left join articles a on r.external_id = a.external_id where a.external_id is null")

	cursor.execute(query)

	result = cursor.fetchall()

	cursor.close()

	disconnect(cnx)

	return result
