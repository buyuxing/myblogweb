import requests
import hashlib

if __name__ == '__main__':
	pwd = hashlib.sha1('Tt123456'.encode('utf-8')).hexdigest()
	data = {
		'email':'281866683@qq.com', 
		'username':'buyuxing',
		'password':pwd
	}
	r = requests.post('http://127.0.0.1:8888/api/user/register',data = data)
	print(r)
	print(r.text)