from flask import Flask 
app = Flask(__name__)


app.config.from_object('core.config.SECRET_KEY')
app.config.from_object('core.config.ProductionConfig')

config = app.config

#from core import routes
from core.controller.studentcontroller import app as students

app.register_blueprint(students, url_prefix='')