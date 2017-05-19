# -*- coding: utf-8 -*-

from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from model import *
import json
import logging

app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///D:\\bigdata\\work\\dddoc\\python_web\\flask_demo\\AllInOnePlatform\\test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:r00t@localhost/med_gwc'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/', methods=['GET', 'POST'])
def index():
	#if request.method == 'GET':
		#return 'index page'
	#data = yhxy("YHBM", "YHMC", "SZY", "SSY", "PJY", "MB", "SJZT", "2010-10-10", "SHLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "1", "EMPI", "DOCTOR_EMPI", 0)
	#db.session.add(data)
	#db.session.commit()

	#data = yhxy01("YHBM", "YHMC", "XY", "MB", "SJZT", "2010-10-10", "SHLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "EMPI", "DOCTOR_EMPI", 0)
	#db.session.add(data)
	#db.session.commit()

	data = yhxt("YHBM", "YHMC", "XT", "SJZT", "2010-10-10", "SHLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "EMPI", "DOCTOR_EMPI", 0)
	db.session.add(data)
	db.session.commit()

	# data = yhxz("YHBM", "YHMC", "CHOL", "HDL", "TG", "LDL", "SJZT", "2010-10-10", "SHLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "1", "EMPI", "DOCTOR_EMPI", 0)
	# db.session.add(data)
	# db.session.commit()

	# data = yhtw("YHBM", "YHMC", "WD", "SJZT", "2010-10-10", "SJLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "EMPI", "DOCTOR_EMPI", 0)
	# db.session.add(data)
	# db.session.commit()

	#data = yhtz("YHBM", "YHMC", "TZ", "SG", "2010-12-12", "SHLY", "SJZT", "SJLY", 0)
	#db.session.add(data)
	#db.session.commit()
	return 'index page'


@app.route('/platform/api/register', methods=['GET', 'POST'])
def register():
	pass

@app.route('/platform/api/uploaddoctor', methods=['GET', 'POST'])
def uploaddoctor():
	pass

@app.route('/platform/api/uploadresident', methods=['GET', 'POST'])
def uploadresident():
	pass

@app.route('/platform/api/uploadecg', methods=['GET', 'POST'])
def uploadecg():
	pass

@app.route('/platform/api/uploadbloodpresure', methods=['GET', 'POST'])
def uploadbloodpresure():
	pass

@app.route('/platform/api/uploadbloodsugar', methods=['GET', 'POST'])
def uploadbloodsugar():
	pass

@app.route('/platform/api/uploadbloodoxygen', methods=['GET', 'POST'])
def uploadbloodoxygen():
	pass

@app.route('/platform/api/uploadtemperature', methods=['GET', 'POST'])
def uploadtemperature():
	pass

@app.route('/platform/api/uploadhemoglobin', methods=['GET', 'POST'])
def uploadhemoglobin():
	pass

@app.route('/platform/api/uploadurine', methods=['GET', 'POST'])
def uploadurine():
	pass

@app.route('/platform/api/uploaduricacid', methods=['GET', 'POST'])
def uploaduricacid():
	pass

@app.route('/platform/api/uploadbmi', methods=['GET', 'POST'])
def uploadbmi():
	pass

@app.route('/platform/api/uploadfetalheart', methods=['GET', 'POST'])
def uploadfetalheart():
	pass

@app.route('/platform/api/uploadhealthreport', methods=['GET', 'POST'])
def uploadhealthreport():
	pass



@app.route('/test/<name>')
def test(name):
	return 'hello %s' % name

@app.route('/db')
def db2():
	return 'db save ok'

def generate_response():
	retsult = {}
	sysHead = {}
	sysHead['version'] = '1.0'
	retsult['sysHead'] = sysHead

	ret = {}
	ret['retCode'] = '000000'
	ret['retMsg'] = 'successful'
	retsult['ret'] = ret

	data = {}
	data['aaa'] = '你好'
	Body = {}
	Body['data'] = data
	retsult['Body'] = Body

	return json.dumps(retsult, ensure_ascii=False)

@app.route('/upload', methods=['POST'])
def upload():
	s = request.form.get('json')
	json_data = json.loads((s))
	ret = {}
	sysHead = {}
	sysHead['version'] = '1.0'
	ret['sysHead'] = sysHead
	ret['aaa'] = 'qweadf'
	ttt = json.dumps(ret)
	return generate_response()
	#return str(json_data['aaa'])

@app.route('/doc')
def doc():
	return 'doc'

if __name__ == '__main__':
	app.run(debug=True)


