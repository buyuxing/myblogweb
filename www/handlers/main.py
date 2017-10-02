'''
url handlers
'''

__author__ = 'buyuxing'

import re, time, json, logging, hashlib, base64, asyncio

from MyWebFramework import get, post

from models import User, Blog, Comment, next_id

@get('/')
async def index(request):
	blogs = await Blog.findAll()

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

@get('/manage/blog/create')
async def manage_blog_create():
	return {
		'__template__' : 'blogedit.html',
		'id' : '',
		'action' : '/api/blog/submit'
	}

@get('/blog/{id}')
async def blog(id, request):
	blog = await Blog.find(id)
	return {
		'__template__' : 'blog.html',
		'blog' : blog,
		'__user__' : request.__user__
	}