from sqlalchemy import create_engine, MetaData,select, Table, Integer, String, Column, insert, update
from sqlalchemy.sql import and_, or_
from core import app

engine = create_engine(app.config['DATABASE_URI'])

#creating a studata class for the above table and passing all variables 
class Students():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.students = Table("students", self.meta, autoload=True, autoload_with=engine)
        except Exception as e:
            print(e)
    
    def insert(self, data):
        print('inside model insert')
        result = engine.execute(self.students.insert(), data)
        
    def getall(self):
        stud = self.students.select()
        all_data = engine.execute(stud)
        return all_data

    def update(self, id, data):
        row_up = self.students.update()
        stmt = row_up.where(
            and_(self.students.c.ID.in_([id]))
        )
        result = engine.execute(stmt,data)

    def delete(self,id):
        row_del = self.students.delete()
        stmt = row_del.where(
            and_(self.students.c.ID.in_([id]))
        )
        result = engine.execute(stmt)
    
    def fetchall(self, content):
        print('inside method fetchall')
        stmt = select([self.students]).where(self.students.c.Name.ilike("%" + content + "%"))
        result = engine.execute(stmt)
        results = [dict(r) for r in result] if result else None
        print(results)
        return results

# select([sometable]).where(sometable.c.column.like("%foobar%"))
#like(category_param_value + "%")) - like parameter using variable