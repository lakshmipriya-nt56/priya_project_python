from flask import request, Blueprint, jsonify, redirect, url_for, render_template, flash
from core.model.students import Students

app = Blueprint('students', __name__)


#displaying the form 
@app.route('/first_page', methods = ["POST","GET"])
def First_page():
    s=Students()
    sel_all = s.getall()
    return render_template('first_page.html', dis = sel_all)

#collecting the form data and sending to Insert method through POST method
@app.route('/insert', methods = ["POST","GET"])
def Insert():
    print('reached insert method in studentcontroller')
    if request.method == "POST":
        data = { 
                    'Name' : request.form["name"],
                    'Email' : request.form["email"],
                    'Phone' : request.form["phone"] 
                }

        #creating object for class Studata
        s = Students()

        #once the values are fetched from the form 
        s.insert(data)

        flash('Data Inserted successfully')


        return redirect (url_for('students.First_page'))
    else:
        return redirect (url_for('students.First_page'))

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
        s=Students()
        s.update(user_id, data)
        print(user_id)

        flash('Data Updated successfully')


        return redirect (url_for('students.First_page'))
    else:
        return redirect (url_for('students.First_page'))

@app.route('/delete/<id>', methods = ["POST", "GET"])
def Delete(id):
    user_id = id
    s=Students()
    s.delete(user_id)


    flash('Data Deleted Successfully')

    return redirect (url_for('students.First_page'))

@app.route('/search', methods = ["POST", "GET"])
def Search():
    print('reached /search route')
    if request.method == "POST":
        print('hi')
        content = request.form["search"]
        print(content)
        s=Students()
        result=s.fetchall(content)
        print(result)
        return render_template("first_page.html", dis = result,content=content)
    # return redirect (url_for('First_page'))