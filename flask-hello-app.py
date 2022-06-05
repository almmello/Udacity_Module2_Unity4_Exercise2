from flask import Flask
from urllib.parse import quote  
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://almmello@localhost:5432/example'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return 'Hello World!'
