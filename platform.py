# -*- coding: utf-8 -*-
from model import *
from flask import request, jsonify, render_template
import json
import logging

url_prifix = '/platform/api'
error_msg = 'the data you post is not json'
return_msg = 'upload data ok'

#logFormatStr = '[%(asctime)s] p%(process)s {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s'
logFormatStr = '[%(asctime)s] %(lineno)d} %(levelname)s - %(message)s'
logging.basicConfig(format = logFormatStr, filename='error.log', level=logging.DEBUG)


@app.route('/', methods=['GET', 'POST'])
def index():
	return render_template('index.html')

@app.route('/out', methods=['GET', 'POST'])
def out():
	if request.method == 'GET':
		header = str(request.headers)
		return header + str(request.args)
	if request.method == 'POST':
		body = request.get_data()
		header = str(request.headers)
		return header + body

@app.route('/test', methods=['GET', 'POST'])
def test():
	#if request.method == 'GET':
		#return 'index page'
	# data = bloodpresure("YHBM", "YHMC", "SZY", "SSY", "PJY", "MB", "SJZT", "2010-10-10", "SHLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "1", "EMPI", "DOCTOR_EMPI", 0)
	# db.session.add(data)
	# db.session.commit()

	# data = bloodoxygen("YHBM", "YHMC", "XY", "MB", "SJZT", "2010-10-10", "SHLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "EMPI", "DOCTOR_EMPI", 0)
	# db.session.add(data)
	# db.session.commit()

	# data = bloodsugar("YHBM", "YHMC", "XT", "SJZT", "2010-10-10", "SHLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "EMPI", "DOCTOR_EMPI", 0)
	# db.session.add(data)
	# db.session.commit()

	# data = bloodlipids("YHBM", "YHMC", "CHOL", "HDL", "TG", "LDL", "SJZT", "2010-10-10", "SHLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "1", "EMPI", "DOCTOR_EMPI", 0)
	# db.session.add(data)
	# db.session.commit()

	# data = bodytemperature("YHBM", "YHMC", "WD", "SJZT", "2010-10-10", "SJLY", "RESULT", "PID", "MACHINE_ID",  0, "ORG_CODE", "ORG_NAME", "YSBM", "YSMC", "EMPI", "DOCTOR_EMPI", 0)
	# db.session.add(data)
	# db.session.commit()

	# data = bodyfat("YHBM", "YHMC", "TZ", "SG", "2010-12-12", "SHLY", "SJZT", "SJLY", 0)
	# db.session.add(data)
	# db.session.commit()
	return 'index page'


@app.route(url_prifix + '/register', methods=['GET', 'POST'])
def register():
	if request.method == 'GET':
		return 'register'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploaddoctor', methods=['GET', 'POST'])
def uploaddoctor():
	if request.method == 'GET':
		return 'uploaddoctor'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadresident', methods=['GET', 'POST'])
def uploadresident():
	if request.method == 'GET':
		return 'uploadresident'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadbloodpresure', methods=['GET', 'POST'])
def uploadbloodpresure():
	if request.method == 'GET':
		return 'uploadbloodpresure'
	if request.method == 'POST':
		data = request.get_data().decode('utf-8')
		if data == None:
			return error_msg
		logging.debug('this is post data uploadbloodpresure')
		logging.debug(data)
		data = json.loads(data)
		realdata = data.get('data')
		for item in realdata:
			bloodpresuredata = bloodpresure(item.get("IDCARD"), item.get("ResidentName"), item.get("SBP"), 
					item.get("DBP"), item.get("MBP"), item.get("pulse"), "1", item.get("examDate"), 
					data.get("dataSource"), item.get("Mode"), item.get("PID"),data.get("mechineID"), 
					0, data.get("orgCode"), data.get("orgName"), item.get("examDoctorIDCARD"), item.get("examDoctorName"), "1", 
					item.get("residentEMPI"), item.get("examDoctorEMPI"), 0)
			db.session.add(bloodpresuredata)
		db.session.commit()
		return "upload ok"

@app.route(url_prifix + '/uploadbloodsugar', methods=['GET', 'POST'])
def uploadbloodsugar():
	if request.method == 'GET':
		return 'uploadbloodsugar'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadbloodoxygen', methods=['GET', 'POST'])
def uploadbloodoxygen():
	if request.method == 'GET':
		return 'uploadbloodoxygen'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadtemperature', methods=['GET', 'POST'])
def uploadtemperature():
	if request.method == 'GET':
		return 'uploadtemperature'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadhemoglobin', methods=['GET', 'POST'])
def uploadhemoglobin():
	if request.method == 'GET':
		return 'uploadhemoglobin'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/bloodlipids', methods=['GET', 'POST'])
def bloodlipids():
	if request.method == 'GET':
		return 'bloodlipids'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadurine', methods=['GET', 'POST'])
def uploadurine():
	if request.method == 'GET':
		return 'uploadurine'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploaduricacid', methods=['GET', 'POST'])
def uploaduricacid():
	if request.method == 'GET':
		return 'uploaduricacid'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadbmi', methods=['GET', 'POST'])
def uploadbmi():
	if request.method == 'GET':
		return 'uploadbmi'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadecg', methods=['GET', 'POST'])
def uploadecg():
	if request.method == 'GET':
		return 'uploadecg'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadfetalheart', methods=['GET', 'POST'])
def uploadfetalheart():
	if request.method == 'GET':
		return 'uploadfetalheart'
	if request.method == 'POST':
		pass

@app.route(url_prifix + '/uploadhealthreport', methods=['GET', 'POST'])
def uploadhealthreport():
	if request.method == 'GET':
		return 'uploadhealthreport'
	if request.method == 'POST':
		pass


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

@app.route(url_prifix + '/upload', methods=['POST'])
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


