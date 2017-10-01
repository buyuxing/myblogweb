'''
用户接口定义
'''

__author__ = 'buyuxing'

import re, time, json, logging, hashlib, base64, asyncio

from MyWebFramework import get, post

from models import User, Blog, Comment, next_id

from apis import APIError, APIValueError, APIResourceNotFoundError

from aiohttp import web

from config import configs

COOKIE_NAME = 'myblogsession'
_COOKIE_KEY = configs.session.secret

_RE_EMAIL = re.compile(r'^[a-z0-9\.\-\_]+\@[a-z0-9\-\_]+(\.[a-z0-9\-\_]+){1,4}$')
_RE_SHA1 = re.compile(r'^[0-9a-f]{40}$')


def user2cookie(user, max_age):
    '''
    Generate cookie str by user.
    '''
    # build cookie string by: id-expires-sha1
    expires = str(int(time.time() + max_age))
    s = '%s-%s-%s-%s' % (user.id, user.pwd, expires, _COOKIE_KEY)
    L = [user.id, expires, hashlib.sha1(s.encode('utf-8')).hexdigest()]
    return '-'.join(L)

async def cookie2user(cookie_str):
    '''
    Parse cookie and load user if cookie is valid.
    '''
    if not cookie_str:
        return None
    try:
        L = cookie_str.split('-')
        if len(L) != 3:
            return None
        uid, expires, sha1 = L
        if int(expires) < time.time():
            return None
        user = await User.find(uid)
        if user is None:
            return None
        s = '%s-%s-%s-%s' % (uid, user.passwd, expires, _COOKIE_KEY)
        if sha1 != hashlib.sha1(s.encode('utf-8')).hexdigest():
            logging.info('invalid sha1')
            return None
        user.passwd = '******'
        return user
    except Exception as e:
        logging.exception(e)
        return None


@post('/api/user/register')
async def api_user_register(*, email, username, password):
	if not username or not username.strip():
		raise APIValueError('username')
	if not email or not _RE_EMAIL.match(email):
		raise APIValueError('email')
	if not password or not _RE_SHA1.match(password): 
		raise APIValueError('password')
	users = await User.findAll('email = ?', [email])
	if len(users) > 0:
		raise APIError('register:failed','email','邮箱已注册')
	uid = next_id()
	sha1_pwd = '%s:%s' % (uid, password)
	user = User(
				id = uid,
				email = email,
				username = username.strip(), 
				pwd = hashlib.sha1(sha1_pwd.encode('utf-8')).hexdigest(), 
				img = 'http://www.gravatar.com/avatar/%s?d=mm&s=120' % hashlib.md5(email.encode('utf-8')).hexdigest()
				)
	await user.save()
	r = web.Response()
	r.set_cookie(COOKIE_NAME, user2cookie(user, 86400), max_age = 86400, httponly = True)
	user.password = '***'
	r.content_type = 'application/json'
	r.body = json.dumps(user, ensure_ascii=False).encode('utf-8')
	return r