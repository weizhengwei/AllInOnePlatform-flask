from flask import Flask
from flask import request
from flask import jsonify
from flaskext.mysql import MySQL

import real_uploadresident

app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'r00t'
app.config['MYSQL_DATABASE_DB'] = 'weixin'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql = MySQL()
mysql.init_app(app)


#cursor = mysql.get_db().sursor()


@app.route('/ttt', methods=['POST', 'GET'])
def index2():
	conn = mysql.connect()
	try:
		with conn.cursor() as cursor:
			#conn = mysql.connect()
			#cursor = conn.cursor()
			s = "INSERT INTO USER(username, email) VALUES('werxcv', '234');";
			#cursor.execute("insert user(username, email) values('test', 'test');")
			cursor.execute(s)
			conn.commit()
	finally:
		conn.close()
		return s
	return s

@app.route('/', methods=['POST', 'GET'])
def index():
	ua = request.headers.get('User-Agent')
	return '<p>you ua is %s</>' % ua

@app.route('/test')
def test():
	return 'test page'

@app.route('/doc')
def doc():
	return 'doc page'

@app.route('/file', methods=['POST'])
def file():
	f = request.files['file']
	fname = (f.filename)
	f.save(fname)
	return fname

@app.route('/morefile', methods=['POST'])
def morefile():
	f1 = request.files['file1']
	f2 = request.files['file2']
	fname1 = f1.filename
	fname2 = f2.filename
	return fname2

@app.route('/json', methods=['POST'])
def json():
	s = request.get_json()
	return jsonify(s)


@app.route('/platform/uploadTemperatureData', methods = ['GET', 'POST'])
def uploadTemperatureData():
	if request.method == 'GET':
		return "uploadTemperatureData"
	elif request.method == 'POST':
		s = request.get_json()

		return jsonify(s)


if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 10086, debug=True)