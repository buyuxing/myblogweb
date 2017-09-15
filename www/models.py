import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
	return '%015d%s000' % (int(time.time() * 1000),uuid.uuid4().hex)

class User(Model):
	"""docstring for User"""
	__table__ = 'BYXUser'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	email = StringField(ddl='varchar(50)')
	pwd = StringField(ddl='varchar(50)')
	isAdmin = BooleanField()
	username = StringField(ddl='varchar(50)')
	nickname = StringField(ddl='varchar(50)')
	img = StringField(ddl='varchar(50)')
	email = StringField(ddl='varchar(500)')
	createdAt = FloatField(default=time.time)

class Blog(Model):
	"""docstring for Blog"""
	__table__ = 'BYXBlog'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	userId = StringField(ddl='varchar(50)')
	username = StringField(ddl='varchar(50)')
	img = StringField(ddl='varchar(500)')
	title = StringField(ddl='varchar(50)')
	summary = StringField(ddl='varchar(200)')
	content = TextField()
	createdAt = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'BYXComment'
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blogId = StringField(ddl='varchar(50)')
    userId = StringField(ddl='varchar(50)')
    username = StringField(ddl='varchar(50)')
    img = StringField(ddl='varchar(500)')
    content = TextField()
    createdAt = FloatField(default=time.time)