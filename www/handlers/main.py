'''
url handlers
'''

__author__ = 'buyuxing'

import re, time, json, logging, hashlib, base64, asyncio

from MyWebFramework import get, post

from models import User, Blog, Comment, next_id

@get('/')
async def index(request):
	summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
	blogs = [
		Blog(id='1', title='Test Blog', summary=summary, createdAt=time.time()-120),
		Blog(id='2', title='Something New', summary=summary, createdAt=time.time()-3600),
		Blog(id='3', title='Learn Swift', summary=summary, createdAt=time.time()-7200)
		]

	dic = {
	'__template__': 'blogs.html',
	'blogs': blogs
	}

	if request.__user__ is not None:
		dic['__user__'] = request.__user__
	return dic

@get('/register')
async def register():
	return {
		'__template__': 'register.html'
	}

@get('/signin')
async def signin():
	return {
		'__template__': 'signin.html'
	}