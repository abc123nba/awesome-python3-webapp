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