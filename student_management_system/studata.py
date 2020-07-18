from sqlalchemy import create_engine, select, MetaData, Table
from sqlalchemy.sql import and_, or_
from core import app

# Author Sridhar V1.0 
# Create @ 2020.Apr.02 4:43 PM
# Useage : users table model

engine = create_engine(app.config['DATABASE_URI'])

class Studata():	
	def __init__(self):
		try:
			self.meta = MetaData()
			self.studata = Table("studata", self.meta, autoload=True, autoload_with=engine)
		except Exception as e:
			print(e)

	# https://stackoverflow.com/questions/21206869/insert-and-update-with-core-sqlalchemy
	def getAll(self):
		stmt = self.users.select() 
		# stmt = select([self.users])
		# stmt = select([self.users.c.name,self.users.c.mobile, self.users.c.email, self.users.c.user_id])
		# stmt = "select * from users"
		# print(stmt)			
		result = engine.execute(stmt)
		temp = [dict(r) for r in result] if result else None
		# print(temp)			
		return temp		


	def get(self, user_id):
		stmt = self.users.select()
		stmt = stmt.where(
			and_(
				self.users.c.user_id.in_([user_id])
			)
		)
		result = engine.execute(stmt)
		temp = [dict(r) for r in result] if result else None
		return temp

	
	def create(self, data):
		result = engine.execute(self.users.insert(), data)
		print("result:-")
		print(result.inserted_primary_key[0])
		temp = [r for r in result.inserted_primary_key] if result.inserted_primary_key else None
		print(temp)
		return temp


	def insert(self, data):
		result = engine.execute(self.studata.insert(), data)
		print("result:-")
		print(result)
		return result	