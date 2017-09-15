import orm, asyncio

from models import User, Blog, Comment

async def test(loop):
	await orm.create_pool(loop,user = 'buyuxing', password='buyuxing', db='myblog')
	u = User(username = 'Test', email='test@example.com', pwd = '1asfafdf',img='about:blank')
	r = await u.save()
	return r

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.run_until_complete(test(loop))
	loop.run_forever()

