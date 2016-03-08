@asyncio.coroutine
def execute(sql, args):
	log(sql)
	with (yield from _pool) as conn:
		try:
			cur = yield from conn.cursor()
			yield from cur.execute(sql.replace('?', '%s'),args)
			affected = cur.rowcount
			yield from cur.close()
		except BaseException as e:
			raise
        return affected

from orm import Model,StringField,IntegerField

class User(Model):
	_table_ ='users'

	id = IntegerField(primary_key=True)
	name = StringField()

#创建实例：
User = User(id=123,name='Michael')
#存入数据库：
User.insert()

        		        