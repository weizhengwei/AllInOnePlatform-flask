# -*- coding: utf-8 -*-
from platform import db
from datetime import datetime
import json

import sys
reload(sys)
sys.setdefaultencoding('utf8')


class yhxy(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	YHBM = db.Column(db.String(40))
	YHMC = db.Column(db.String(20))
	SZY = db.Column(db.String(20))
	SSY = db.Column(db.String(20))
	PJY = db.Column(db.String(20))
	MB = db.Column(db.String(20))
	JCRQ = db.Column(db.DateTime)
	SHLY = db.Column(db.String(30))
	RESULT = db.Column(db.String(20))
	PID = db.Column(db.String(32))
	MACHINE_ID = db.Column(db.String(20))
	isDelete = db.Column(db.Integer)
	ORG_CODE = db.Column(db.String(100))
	ORG_NAME = db.Column(db.String(100))
	YSBM = db.Column(db.String(20))
	YSMC = db.Column(db.String(20))
	state = db.Column(db.String(1))
	EMPI = db.Column(db.String(32))
	DOCTOR_EMPI = db.Column(db.String(32))
	processed = db.Column(db.Integer)

	def __init__(self, YHBM, YHMC, SZY, SSY, PJY, MB, SJZT, JCRQ, SHLY, RESULT, PID, MACHINE_ID, isDelete, ORG_CODE, ORG_NAME, YSBM, YSMC, state, EMPI, DOCTOR_EMPI, processed):
		self.YHBM = YHBM
		self.YHMC = YHMC
		self.SZY = SZY
		self.SSY = SSY
		self.PJY = PJY
		self.MB = MB
		self.SJZT = SJZT
		self.JCRQ = JCRQ
		self.SHLY = SHLY
		self.RESULT = RESULT
		self.PID = PID
		self.MACHINE_ID = MACHINE_ID
		self.isDelete = 0
		self.ORG_CODE = ORG_CODE
		self.ORG_NAME = ORG_NAME
		self.YSBM = YSBM
		self.YSMC = YSMC
		self.state = state
		self.EMPI = EMPI
		self.DOCTOR_EMPI = DOCTOR_EMPI
		self.processed = processed

class yhxy01(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	YHBM = db.Column(db.String(40))
	YHMC = db.Column(db.String(20))
	XY = db.Column(db.String(20))
	MB = db.Column(db.String(20))
	JCRQ = db.Column(db.DateTime)
	SHLY = db.Column(db.String(30))
	RESULT = db.Column(db.String(20))
	PID = db.Column(db.String(32))
	MACHINE_ID = db.Column(db.String(20))
	isDelete = db.Column(db.Integer)
	ORG_CODE = db.Column(db.String(100))
	ORG_NAME = db.Column(db.String(100))
	YSBM = db.Column(db.String(20))
	YSMC = db.Column(db.String(20))
	EMPI = db.Column(db.String(32))
	DOCTOR_EMPI = db.Column(db.String(32))
	processed = db.Column(db.Integer)

	def __init__(self, YHBM, YHMC, XY, MB, SJZT, JCRQ, SHLY, RESULT, PID, MACHINE_ID, isDelete, ORG_CODE, ORG_NAME, YSBM, YSMC, EMPI, DOCTOR_EMPI, processed):
		self.YHBM = YHBM
		self.YHMC = YHMC
		self.XY = XY
		self.MB = MB
		self.SJZT = SJZT
		self.JCRQ = JCRQ
		self.SHLY = SHLY
		self.RESULT = RESULT
		self.PID = PID
		self.MACHINE_ID = MACHINE_ID
		self.isDelete = 0
		self.ORG_CODE = ORG_CODE
		self.ORG_NAME = ORG_NAME
		self.YSBM = YSBM
		self.YSMC = YSMC
		self.EMPI = EMPI
		self.DOCTOR_EMPI = DOCTOR_EMPI
		self.processed = processed



class yhxt(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	YHBM = db.Column(db.String(40))
	YHMC = db.Column(db.String(20))
	XT = db.Column(db.String(20))
	JCRQ = db.Column(db.DateTime)
	SHLY = db.Column(db.String(30))
	RESULT = db.Column(db.String(20))
	PID = db.Column(db.String(32))
	MACHINE_ID = db.Column(db.String(20))
	isDelete = db.Column(db.Integer)
	ORG_CODE = db.Column(db.String(100))
	ORG_NAME = db.Column(db.String(100))
	YSBM = db.Column(db.String(20))
	YSMC = db.Column(db.String(20))
	EMPI = db.Column(db.String(32))
	DOCTOR_EMPI = db.Column(db.String(32))
	processed = db.Column(db.Integer)

	def __init__(self, YHBM, YHMC, XT, SJZT, JCRQ, SHLY, RESULT, PID, MACHINE_ID, isDelete, ORG_CODE, ORG_NAME, YSBM, YSMC, EMPI, DOCTOR_EMPI, processed):
		self.YHBM = YHBM
		self.YHMC = YHMC
		self.XT = XT
		self.SJZT = SJZT
		self.JCRQ = JCRQ
		self.SHLY = SHLY
		self.RESULT = RESULT
		self.PID = PID
		self.MACHINE_ID = MACHINE_ID
		self.isDelete = 0
		self.ORG_CODE = ORG_CODE
		self.ORG_NAME = ORG_NAME
		self.YSBM = YSBM
		self.YSMC = YSMC
		self.EMPI = EMPI
		self.DOCTOR_EMPI = DOCTOR_EMPI
		self.processed = processed



class yhxz(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	YHBM = db.Column(db.String(40))
	YHMC = db.Column(db.String(20))
	CHOL = db.Column(db.String(20))
	HDL = db.Column(db.String(20))
	TG = db.Column(db.String(20))
	LDL = db.Column(db.String(20))
	JCRQ = db.Column(db.DateTime)
	SHLY = db.Column(db.String(30))
	RESULT = db.Column(db.String(20))
	PID = db.Column(db.String(32))
	MACHINE_ID = db.Column(db.String(20))
	isDelete = db.Column(db.Integer)
	ORG_CODE = db.Column(db.String(100))
	ORG_NAME = db.Column(db.String(100))
	YSBM = db.Column(db.String(20))
	YSMC = db.Column(db.String(20))
	state = db.Column(db.String(1))
	EMPI = db.Column(db.String(32))
	DOCTOR_EMPI = db.Column(db.String(32))
	processed = db.Column(db.Integer)

	def __init__(self, YHBM, YHMC, CHOL, HDL, TG, LDL, SJZT, JCRQ, SHLY, RESULT, PID, MACHINE_ID, isDelete, ORG_CODE, ORG_NAME, YSBM, YSMC, state, EMPI, DOCTOR_EMPI, processed):
		self.YHBM = YHBM
		self.YHMC = YHMC
		self.CHOL = CHOL
		self.HDL = HDL
		self.TG = TG
		self.LDL = LDL
		self.SJZT = SJZT
		self.JCRQ = JCRQ
		self.SHLY = SHLY
		self.RESULT = RESULT
		self.PID = PID
		self.MACHINE_ID = MACHINE_ID
		self.isDelete = 0
		self.ORG_CODE = ORG_CODE
		self.ORG_NAME = ORG_NAME
		self.YSBM = YSBM
		self.YSMC = YSMC
		self.state = state
		self.EMPI = EMPI
		self.DOCTOR_EMPI = DOCTOR_EMPI
		self.processed = processed



class yhxhdb(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	YHBM = db.Column(db.String(60))
	YHMC = db.Column(db.String(60))
	HB = db.Column(db.String(60))
	HCL = db.Column(db.String(60))
	JCRQ = db.Column(db.DateTime)
	SHLY = db.Column(db.String(30))
	RESULT = db.Column(db.String(20))
	PID = db.Column(db.String(32))
	MACHINE_ID = db.Column(db.String(60))
	isDelete = db.Column(db.Integer)
	ORG_CODE = db.Column(db.String(300))
	ORG_NAME = db.Column(db.String(300))
	YSBM = db.Column(db.String(60))
	YSMC = db.Column(db.String(60))
	processed = db.Column(db.Integer)

	def __init__(self, YHBM, YHMC, HB, HCL, SJZT, JCRQ, SHLY, RESULT, PID, MACHINE_ID, isDelete, ORG_CODE, ORG_NAME, YSBM, YSMC):
		self.YHBM = YHBM
		self.YHMC = YHMC
		self.HB = HB
		self.HCL = HCL
		self.SJZT = SJZT
		self.JCRQ = JCRQ
		self.SHLY = SHLY
		self.RESULT = RESULT
		self.PID = PID
		self.MACHINE_ID = MACHINE_ID
		self.isDelete = 0
		self.ORG_CODE = ORG_CODE
		self.ORG_NAME = ORG_NAME
		self.YSBM = YSBM
		self.YSMC = YSMC



class yhtw(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	YHBM = db.Column(db.String(20))
	YHMC = db.Column(db.String(255))
	WD = db.Column(db.String(20))
	SJZT = db.Column(db.String(20))
	JCRQ = db.Column(db.DateTime)
	SJLY = db.Column(db.String(30))
	RESULT = db.Column(db.String(255))
	PID = db.Column(db.String(32))
	MACHINE_ID = db.Column(db.String(20))
	isDelete = db.Column(db.Integer)
	ORG_CODE = db.Column(db.String(100))
	ORG_NAME = db.Column(db.String(100))
	YSBM = db.Column(db.String(20))
	YSMC = db.Column(db.String(20))
	EMPI = db.Column(db.String(32))
	DOCTOR_EMPI = db.Column(db.String(32))
	processed = db.Column(db.Integer)

	def __init__(self, YHBM, YHMC, WD, SJZT, JCRQ, SJLY, RESULT, PID, MACHINE_ID, isDelete, ORG_CODE, ORG_NAME, YSBM, YSMC, EMPI, DOCTOR_EMPI, processed):
		self.YHBM = YHBM
		self.YHMC = YHMC
		self.WD = WD
		self.SJZT = SJZT
		self.JCRQ = JCRQ
		self.SJLY = SJLY
		self.RESULT = RESULT
		self.PID = PID
		self.MACHINE_ID = MACHINE_ID
		self.isDelete = 0
		self.ORG_CODE = ORG_CODE
		self.ORG_NAME = ORG_NAME
		self.YSBM = YSBM
		self.YSMC = YSMC
		self.EMPI = EMPI
		self.DOCTOR_EMPI = DOCTOR_EMPI
		self.processed = processed



class yhtz(db.Model):
	ID = db.Column(db.Integer, primary_key=True)
	YHBM = db.Column(db.String(20))
	YHMC = db.Column(db.String(255))
	TZ = db.Column(db.String(20))
	SG = db.Column(db.String(20))
	JCRQ = db.Column(db.DateTime)
	SHLY = db.Column(db.String(255))
	SJZT = db.Column(db.String(20))
	SJLY = db.Column(db.String(20))
	isDelete = db.Column(db.Integer)

	def __init__(self, YHBM, YHMC, TZ, SG, JCRQ, SHLY, SJZT, SJLY, isDelete):
		self.YHBM = YHBM
		self.YHMC = YHMC
		self.TZ = TZ
		self.SG = SG
		self.JCRQ = JCRQ
		self.SHLY = SHLY
		self.SJZT = SJZT
		self.SJLY = SJLY
		self.isDelete = 0

