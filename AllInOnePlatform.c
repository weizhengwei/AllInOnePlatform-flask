(env) D:\bigdata\work\dddoc\python_web\flask_demo\AllInOnePlatform>pip install flask-mysql
Collecting flask-mysql
d:\bigdata\work\dddoc\python_web\flask_demo\allinoneplatform\env\lib\site-packages\pip\_vendor\requests\package
s\urllib3\util\ssl_.py:318: SNIMissingWarning: An HTTPS request has been made, but the SNI (Subject Name Indica
tion) extension to TLS is not available on this platform. This may cause the server to present an incorrect TLS
 certificate, which can cause validation failures. You can upgrade to a newer version of Python to solve this.
For more information, see https://urllib3.readthedocs.io/en/latest/security.html#snimissingwarning.
  SNIMissingWarning
d:\bigdata\work\dddoc\python_web\flask_demo\allinoneplatform\env\lib\site-packages\pip\_vendor\requests\package
s\urllib3\util\ssl_.py:122: InsecurePlatformWarning: A true SSLContext object is not available. This prevents u
rllib3 from configuring SSL appropriately and may cause certain SSL connections to fail. You can upgrade to a n
ewer version of Python to solve this. For more information, see https://urllib3.readthedocs.io/en/latest/securi
ty.html#insecureplatformwarning.
  InsecurePlatformWarning
  Downloading Flask_MySQL-1.4.0-py2.py3-none-any.whl
Collecting PyMySQL (from flask-mysql)
  Downloading PyMySQL-0.7.11-py2.py3-none-any.whl (78kB)
    100% |████████████████████████████████| 81kB 17kB/s
Requirement already satisfied: Flask in d:\bigdata\work\dddoc\python_web\flask_demo\allinoneplatform\env\lib\si
te-packages (from flask-mysql)
Requirement already satisfied: click>=2.0 in d:\bigdata\work\dddoc\python_web\flask_demo\allinoneplatform\env\l
ib\site-packages (from Flask->flask-mysql)
Requirement already satisfied: Jinja2>=2.4 in d:\bigdata\work\dddoc\python_web\flask_demo\allinoneplatform\env\
lib\site-packages (from Flask->flask-mysql)
Requirement already satisfied: Werkzeug>=0.7 in d:\bigdata\work\dddoc\python_web\flask_demo\allinoneplatform\en
v\lib\site-packages (from Flask->flask-mysql)
Requirement already satisfied: itsdangerous>=0.21 in d:\bigdata\work\dddoc\python_web\flask_demo\allinoneplatfo
rm\env\lib\site-packages (from Flask->flask-mysql)
Requirement already satisfied: MarkupSafe>=0.23 in d:\bigdata\work\dddoc\python_web\flask_demo\allinoneplatform
\env\lib\site-packages (from Jinja2>=2.4->Flask->flask-mysql)
Installing collected packages: PyMySQL, flask-mysql
Successfully installed PyMySQL-0.7.11 flask-mysql-1.4.0

---------------------------------------------------------------------

Initialize the extension :

from flaskext.mysql import MySQL
mysql = MySQL()
mysql.init_app(app)
Obtain a cursor :

cursor = mysql.get_db().cursor()



@app.route("/Authenticate")
def Authenticate():
    username = request.args.get('UserName')
    password = request.args.get('Password')
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT * from User where Username='" + username + "' and Password='" + password + "'")
    data = cursor.fetchone()
    if data is None:
     return "Username or Password is wrong"
    else:
     return "Logged in successfully"



 import pymysql

def connection():
    try:
        conn = pymysql.connect(host="localhost", port=3306, user="root", passwd="my_password",db="db_name",charset='utf8')
        c = conn.cursor()
        return conn, c
    except Exception as e:
        print (str(e))




@app.route('/test/') 
def test_page():
    try:
        c, conn = connection()
        return("okay")
    except Exception as e:
        return(str(e))



http://milo.leanote.com/post/Flask%E4%B8%AD%E4%BD%BF%E7%94%A8MySQL-2
http://codehandbook.org/python-web-application-flask-mysql/
https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972



@app.route('/', methods=['POST', 'GET'])
def index():
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


request.headers.get('token')

=================================================================================


curl -H "version:1.0" -H "token=10086" localhost:1086



接口：
header 
{
	version
	token
	language
	timeZone
}


多参仪：
区域
机构代码
注册

上传数据{
	医生-关联机构
	居民-关联医生
	心电-pdf文件，xml文件
	血压：收缩压，舒张压，平均压 blood pressure
	血氧：血氧，脉率 bloodoxygen
	血脂：
	血红蛋白：
	体温：37度
	尿常规:
	尿酸：
	BMI：
	胎监：pdf文件，xml文件，wav文件
	健康报告：
	头像
}

下载{
	特定机构
	医生：
	居民
	头像
}

/platform/uploadresient
/platform/uploaddoctor
/platform/uploadbloodpressure
/platform/uploadbloodoxygen
/platform/uploadfetalheart
/platform/uploadecg
/platform/uploadhealthreport
/platform/uploadbmi
/platform/uploadtempreture

/platform/tempreture



curl -F filename=master.zip http://jingweibbq.com:7777/upload

curl -i -X POST -H "Content-Type: multipart/form-data" -F "file=@test.pdf" http://localhost:10086/file

curl -H "Content-Type: multipart/form-data" -F "file=@test.pdf" http://localhost:10086/file

curl -F "file=@test.pdf" http://localhost:10086/file

curl -F "file=@生活大爆炸第一季 S01E01.mkv" http://localhost:10086/file


curl -F "file1=@test.pdf" -F "file2=@fname.pdf" http://localhost:10086/morefile

curl -F "file1=@test.pdf" -F "file2=@fname.pdf" -F "a=1&b=2" http://localhost:10086/morefile



http://stackoverflow.com/questions/12667797/using-curl-to-upload-post-data-with-files/12667839#12667839
https://segmentfault.com/a/1190000005642670








curl -H  "Content-Type:application/json"



@app.route('/messages', methods = ['POST'])
 def api_message():

    if request.headers['Content-Type'] == 'text/plain':
       return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        f = open(filename,'r')
        l = f.readlines()
        f.close()
        return len(l)


@app.route('/user/<name>')
def user(name):
	return 'hello, %s' % name





　当然，也可使用 url_for 构造，代码如  url_for("static",filename="css/demo.css") 



def root_dir():  # pragma: no cover
    return os.path.abspath(os.path.dirname(__file__))


-----------------------------------------------------
However, you can use send_from_directory to send files from a directory,
 which can be pretty convenient in some situations:

from flask import Flask, request, send_from_directory

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/js/<path:path>')
def send_js(path):
    return send_from_directory('js', path)

if __name__ == "__main__":
    app.run()
------------------------------------------


send_static_file example:

from flask import Flask, request
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/')
def root():
    return app.send_static_file('index.html')



from werkzeug.utils import secure_filename
elif request.method == 'POST':
f = request.files['file']
fname = secure_filename(f.filename) #获取一个安全的文件名，且仅仅支持ascii字符；
f.save(os.path.join(UPLOAD_FOLDER, fname))


@app.route('/')
def index():
return redirect(url_for('upload'), 302)





curl -d "@uploadTemperatureData.json" -H "Content-Type: application/json" localhost:10086/platform/uploadTemperatureData


apache-tomcat-7.0.59.zip 
apache-tomcat-7.0.59_imifs.zip     
bullesb-server-base-3.7.1.zip   




http://52.29.110.21:8080/medimifs/netease/getAccount.do
52.29.110.21:10086/medimifs/netease/getDoctorList.do






 curl -d "username=aaa&email=aaa@qq.com" localhost:5000/add 

 curl -d "username=bbb&email=bbb@qq.com" localhost:5000/add 


 curl -d "username=www&email=www@qq.com" localhost:5000/add 


curl -d '{"aaa":123}' -H 'Content-Type: application/json' localhost:5000/add2
居民
医生
数据：

心电
血压 X
血氧 X
血糖 X
血脂X
血红蛋白
体脂 
体温X
尿酸
尿常规
胎监
BMI


header
	"version":"1.0",
	"token":"token",
	"language":"zh-cn",
	"timeZone":"UTC+8",

curl -H "Content-Type:application/json" -H "version:1.0" -H "token:token" -H "timeZone:UTC+08:00" -d "{}"  localhost:5000/upload


curl -H "Content-Type:application/json" -H "version:1.0" -H "token:token" -H "timeZone:UTC+08:00" -d "{\"asdf\":123}"  localhost:5000/upload

curl -H "Content-Type:application/x-www-form-urlencoded" -H "version:1.0" -H "token:token" -H "timeZone:UTC+08:00" -d "json={\"asdf\":123}"  localhost:5000/upload



curl -H "Content-Type:application/x-www-form-urlencoded" -H "version:1.0" -H "token:token" -H "timeZone:UTC+08:00" -d "json={\"aaa\":123}"  localhost:5000/upload




The moral of the story is, if you have binary (non-alphanumeric) data (or a significantly sized payload) to
 transmit, use multipart/form-data. Otherwise, use application/x-www-form-urlencoded.

uploadBPData

json={
	"familyCode":"familyCode",
	"familyName":"familyName",
	"orgCode":"orgCode",
	"orgName":"orgName",
	"dataSource":"1",
	"mechineID":"mechineID",
	"data":[
		{
			"examDate":"2010-10-10",
			"residentEMPI":"residentEMPI",
			"residenName":"residentName",
			"examDoctorEMPI":"examDoctorEMPI",
			"examDoctorName:"examDoctorName",
			"auditDoctorEMPI":"auditDoctor",
			"SBP":100,
			"DBP":80,
			"MBP":90,
			"pluse":80,
			"conclusion":"jielunjianyi"
		}
	]
}

ret = {}
ret['sysHead'] = {}
ret['aaa'] = 'qweadf'
ttt = json.dumps(ret)


ret = {}
sysHead = {}
sysHead['version'] = '1.0'
ret['sysHead'] = sysHead

ret = {}
ret['retCode'] = '000000'
ret['retMsg'] = 'successful'
ret['ret'] = ret

data = {}
data['aaa'] = 100
Body = {}
Body['data'] = data
ret['Body'] = Body

ttt = json.dumps(ret)


{
	"sysHead":{
		"version":"1.0"
	},
	"ret":{
		"retCode":"000000",
		"retMsg":"upload data successfully"
	},
	"retStatus":"S",
	"Body":{
		"data":[
			{
				"examDate":"2010-10-10",
				"residentEMPI":"residentEMPI",
				"residenName":"residentName",
				"examDoctorEMPI":"examDoctorEMPI",
				"examDoctorName:"examDoctorName",
				"auditDoctorEMPI":"auditDoctor",
				"SBP":100,
				"DBP":80,
				"MBP":90,
				"pluse":80,
				"conclusion":"jielunjianyi"
			}
		]
	}
}

源代码文件第一行添加：#coding:utf-8，这样就可以避免了
也可以改为，在第一行增加：#-*- coding: UTF-8 -*- 。

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

import json, yaml
print json.dumps(['绳子','带子'], ensure_ascii=False, indent=2)
print yaml.dump(['绳子','带子'], allow_unicode=True)
json.dumps(something).decode("unicode-escape")


python3 双引号里的是unicode字符串，只要确保源代码文件是用unicode保存的就可以在双引号里直接用中文

python2 双引号里的是ASCII编码的字符串，unicode字符串用u"中文"来表示

d2269dc1d0198210e62bde8792ca5ec6
1. 在 python2 里面：对于 obj = [u'\u7ef3\u5b50', u'\u5e26\u5b50'] 这种情况， 使用：print(repr(obj).decode('unicode-escape'))
对于 obj = ['绳子','带子'] 这种情况，使用：print(repr(obj).decode('string-escape'))





curl -H "Content-Type: application/json" -d "@uploadHeighWeight.json" http://localhost:5000/post


curl  -H "Content-Type: application/json" -d "@heighweight.json" localhost:5000/dataplatform/api/uploadHeighWeight


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


from flask import abort

abort(404)
    