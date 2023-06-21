from flask import Flask
from flask import render_template, request, session
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy

database_url = 'postgresql://postgres:postgres@localhost:5432/nhonduc'

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = database_url
app.config['WTF_CSRF_ENABLED'] = False

csrf = CSRFProtect(app)
db = SQLAlchemy(app)

