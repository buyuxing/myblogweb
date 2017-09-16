import orm, asyncio

from models import User, Blog, Comment

async def test(loop):
	await orm.create_pool(loop,user = 'buyuxing', password='Tt123456', db='myblog')
	u = User(username = 'buyuxing', email='281866683@qq.com', pwd = 'Tt123456',img='about:blank', isAdmin= True)
	r = await u.save()
	return r

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test(loop))
	loop.run_forever()

