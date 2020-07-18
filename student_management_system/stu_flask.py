from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import create_engine, MetaData,select, Table, Integer, String, Column, insert, update
from sqlalchemy.sql import and_, or_


app = Flask(__name__)
app.secret_key = 'Student Management system'

db_url = 'mysql+mysqldb://urbanedg_train:P&,1(r7-+o2o@72.52.161.232:3306/urbanedg_training_project'
engine = create_engine(db_url)

#meta = MetaData() 

#creatinng table
#studata = Table('studata', meta,
                    #Column('ID', Integer, primary_key = True),
                    #Column('Name', String(100)),
                    #Column('Email', String(100)),
                    #Column('Phone', String(100))
                    #) 



#meta.create_all(engine)
#by now the connection to the database has been established



#displaying the form 
@app.route('/first_page')
def First_page():
    s=Studata()
    sel_all = s.getall()
    return render_template('first_page.html', dis = sel_all)


#collecting the form data and sending to Insert method through POST method
@app.route('/insert', methods = ["POST","GET"])
def Insert():
    
    if request.method == "POST":
        data = { 
                    'Name' : request.form["name"],
                    'Email' : request.form["email"],
                    'Phone' : request.form["phone"] 
                }

        #creating object for class Studata
        s = Studata()

        #once the values are fetched from the form 
        s.insert(data)

        flash('Data Inserted successfully')


        return redirect (url_for('First_page'))
    else:
        return redirect (url_for('First_page'))


@app.route('/update', methods=["POST", "GET"])
def Update():
    if request.method == "POST":
        user_id = request.form["id"]
        data = { 
                    'Name' : request.form["name"],
                    'Email' : request.form["email"],
                    'Phone' : request.form["phone"] 
                }
        #user_id = ID 
        s=Studata()
        s.update(user_id, data)
        print(user_id)

        flash('Data Updated successfully')


        return redirect (url_for('First_page'))
    else:
        return redirect (url_for('First_page'))


@app.route('/delete/<int:id>', methods = ["POST", "GET"])
def Delete(id):
    user_id = id
    s=Studata()
    s.delete(user_id)


    flash('Data Deleted Successfully')

    return redirect (url_for('First_page'))


@app.route('/search', methods = ["POST", "GET"])
def search():
    print('reached /search route')
    if request.method == "POST":
        print('hi')
        content = request.form["search"]
        # print(content)
        s=Studata()
        result=s.fetchall(content)
        print(result)
        return render_template("first_page.html", dis = result,content=content)
    # return redirect (url_for('First_page'))



#creating a studata class for the above table and passing all variables 
class Studata():
    def __init__(self):
        try:
            self.meta = MetaData()
            self.studata = Table("studata", self.meta, autoload=True, autoload_with=engine)
        except Exception as e:
            print(e)
    
    def insert(self, data):
        result = engine.execute(self.studata.insert(), data)
        
    def getall(self):
        stud = self.studata.select()
        all_data = engine.execute(stud)
        return all_data

    def update(self, id, data):
        row_up = self.studata.update()
        stmt = row_up.where(
            and_(self.studata.c.ID.in_([id]))
        )
        result = engine.execute(stmt,data)

    def delete(self,id):
        row_del = self.studata.delete()
        stmt = row_del.where(
            and_(self.studata.c.ID.in_([id]))
        )
        result = engine.execute(stmt)


        

    def fetchall(self, content):
        print('inside method fetchall')
        stmt = select([self.studata]).where(self.studata.c.Name.ilike(content
        ))
        result = engine.execute(stmt)
        results = [dict(r) for r in result] if result else None
        print(results)
        return results

# select([sometable]).where(sometable.c.column.like("%foobar%"))


if __name__ == '__main__':
    app.run()