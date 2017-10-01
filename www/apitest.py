import requests
import hashlib

def test_register():
	pwd = hashlib.sha1('Tt123456'.encode('utf-8')).hexdigest()
	data = {
		'email':'281866683@qq.com', 
		'username':'buyuxing',
		'password':pwd
	}
	r = requests.post('http://127.0.0.1:8888/api/user/register',data = data)
	print(r.text)

def test_login():
	pwd = hashlib.sha1('Tt12345'.encode('utf-8')).hexdigest()
	data = { 
		'username':'buyuxing',
		'password':pwd
	}
	r = requests.post('http://127.0.0.1:8888/api/user/signin',data = data)
	print(r.text)

if __name__ == '__main__':
	test_login()