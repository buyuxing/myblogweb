'''
url handlers
'''

__author__ = 'buyuxing'

import re, time, json, logging, hashlib, base64, asyncio

from MyWebFramework import get, post

from models import User, Blog, Comment, next_id

@get('/api')
async def api(request):
	u = await User.findAll()
	return u
