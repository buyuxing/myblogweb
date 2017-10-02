'''
blog接口
'''

__author__ = 'buyuxing'

import re, time, json, logging, hashlib, base64, asyncio

from MyWebFramework import get, post

from models import User, Blog, Comment, next_id

from apis import APIError, APIValueError, APIResourceNotFoundError

from aiohttp import web

from config import configs

@post('/api/blog/submit')
async def api_blog_submit(request, *, title, summary, content):
	if not title or not title.strip():
		raise APIValueError('title', '标题不能为空')
	if not summary or not summary.strip():
		raise APIValueError('summary', '摘要不能为空')
	if not content or not content.strip():
		raise APIValueError('content', '内容不能为空')
	user = request.__user__
	blog = Blog(
			id = next_id(),
			userId = user.id, 
			username = user.username, 
			img = user.img,
			title = title.strip(),
			summary = summary.strip(),
			content = content.strip()
		)
	await blog.save()
	return blog
