@asyncio.coroutine
def create_pool(loop,**kw):
	logging.info('create database connection pool...')
	global _pool
	_pool = yield from aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf-8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
		)


@asyncio.coroutine
def select(sql,args,size=None):
        log(sql,args)
        global _pool
        with (yield from _pool) as conn:
                cur = yield from conn.cursor(aiomysql.DictCursor)
                yield from cur.execute(sql.replace('?','%s'),args or ())
                if size:
                        rs = yield from cur.fetchmany(size)
                else:
                    rs = yield from cur.fetchall()
                yield from cur.close()
                logging.info('rows returned: %s' % len(rs))
                return rs


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
#查询所有User对象：
User = User.findAll()




class Model(dict,metaclass=ModelMetaclass):
         def __init__(self, **kw):
             super(Model, self).__init__(**kw)
         
         def _getattr_(self,key):
             try:
                return self[key]
              except KeyError:
                raise AttributeError(r"'Model' object has no attribute '%s' % key")


         def _setattr_(self,key,value):
                self[key] = value


         def getValue(self,key):
                return getattr(self,key,None) 


         def getValueOrDefault(self,key):
                value = getattr(self,key,None)
                if value is None:
                    field = self._mappings_[key]
                    if field.default is not None:
                        value =field.default() if callable(field.default) else field.default
                        logging.debug('using default value for %s: %s' % (key,str(value))) 
                        setattr(self,key,value)
                return value
                





class field(object):

        def __init__(self, name,column_type,primary_key,default):
            self.name = name
            self.column_type = column_type
            self.primary_key = primary_key
            self.default = default

        def _str_(self):
                return '<%s,%s:%s>' % (self._class_._name_,self.column_type,self.name)




class StringField(Field):

        def __init__(self, name=None,primary_key=False,default=None,ddl='varchar(100)'):
                super().__init__(name,ddl,primary_key,default)
                
                




class ModelMetaclass(type):

        def _new_(cls,name,basses,attrs):
                #排除Model类本身：
                if name == Model:
                        return type._new_(cls,name,basses,attrs)

                #获取table名称：
                tableName = attrs.get('_table_',None) or name
                logging.info('found model: %s (table:%s)' % (name,tableName))

                #获取所有的Field和主键名：
                mappings =dict()
                fields = [] 
                primary_key = None
                for k,v in attrs.items():
                               if isinstance(v,Field):
                                  logging.info('  found mapping: %s ==> %s' % (k,v))
                                  mappings[k] = v
                                  if v.primary_key:
                                        #找到主键
                                         if primaryKey:
                                                raise RuntimeError('Duplicate primary key for field: %s' % k)
                                         primaryKey = k
                                  else:
                                         fields.append(k) 
                 if not primaryKey:
                         raise RuntimeError('Primary key not found.')
                 for k in mappings.keys():
                         attrs.pop(k)  
                 escaped_fields = list(map(lambda f: '`%s`' % f,fields))
                 attrs['_mappings_'] = mappings #保存属性和列的映射关系
                 attrs['_table_'] = tableName
                 attrs['_pimary_key_'] = primaryKey #主键属性名
                 attrs['_fields_'] = fields #除主键外的属性名

                 #构造默认的selcet,insert,update和delete语句：
                 attrs['_selcet_'] = 'select `%s`, %s from `%s`' % (primaryKey,','.join(escaped_fields),tableName)
                 attrs['_insert_'] = 'insert into `%s` (%s,`%s`)  values (%s)' % (tableName,','join(escaped_fields),primaryKey,create_args_string(len(escaped_fields) +1))
                 attrs['_update_'] = 'update `%s` set %s where `%s` = ?' % (tableName,','.join(map(lambda f:'`%s` = ?' % (mappings.get(f).name or f),fields)),primaryKey) 
                 attrs['_delete_'] = 'delete from `%s` where `%s` = ?' %(tableName,primaryKey)
                 return type,_new_(cls,name,basses,attrs)






class Model(dict):

        ...

        @classmethod
        @asyncio.coroutine                                                           
        def find(cls, pk):
               ' find object by primary  key.'
               rs = yield from select('%s where `%s` = ?' % (cls._selcet_,cls._pimary_key_),[pk],1)
               if len(rs) == 0:
                      return None
               return cls(**rs[0])


        @asyncio.coroutine
        def save(self):
                args = list(map(self.getValueOrDefault,self._fields_))
                args.append(self.getValueOrDefault(self._pimary_key_))
                rows = yield from execute(self._insert_,args)
                if rows !=1:
                        logging.warn('failed to insert record: affected rows: %s' % rows)

              

                                                                                                                                                