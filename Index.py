from flask import render_template, request, redirect, url_for, Flask, session, abort, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import Form
from flask import jsonify
import os, gc
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email, Length, EqualTo
from flask_wtf.csrf  import CsrfProtect
from wtforms.ext.sqlalchemy.orm import model_form
from sqlalchemy import Column, Integer, String
from models import User
import sqlalchemy as sa
import sys
import services
reload(sys)
sys.setdefaultencoding("utf-8")
from config import app
from database import db_session
app = Flask (__name__)
app = Flask(__name__, static_folder='D:\\\Do_An_Tot_Nghiep_Uyen\\Code_DoAn_DaoTrucUyen\\templates\\static' )
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456789@localhost:5433/webgis'
db = SQLAlchemy(app)
@app.route('/', methods = ['GET', 'POST'])
def index():
	return render_template('index.html')
@app.route("/search", methods=['POST'])
def search():
    phuongxa = request.form['phuongxa']
    dientich = request.form['dientich']
    khoanggia = request.form['khoanggia']
    result = []
    sql_str = "-----"
    list_phongtro = [] 	

    if phuongxa and dientich and khoanggia :
        phuongxa = str(phuongxa)
        dientich = str(dientich)
        khoanggia = str(khoanggia)
        
        sql_str, list_phongtro = services.search(phuongxa,  dientich, khoanggia)                
    return render_template('index.html', sql_str = sql_str , result=result, list_phongtro=list_phongtro)
@app.route('/hello', methods = ['GET', 'POST'])
def hello():
	return 'Xin chao!'

@app.route('/login', methods=['GET', 'POST'])
def login():
	return render_template('login.html')

@app.route('/loginkhac', methods=['GET', 'POST'])
def loginkhac():
    """Login Form"""
    if request.method == 'GET':
        return render_template('index.html')
    else:
        tendangnhap = request.form['tendangnhap']
        matkhau = request.form['matkhau']
        try:
            data = User.query.filter_by(Username=tendangnhap, Password=matkhau).first()
            """data = User.query.all()"""
            print'1'
            if data is not None:
                print'2'
                return render_template('True.html')
            else:
                print'3'
                return render_template('False.html')
        except:
            print'4'
            print "Unexpected error:", sys.exc_info()[0]
            return render_template('index.html')



if __name__ == "__main__":
	app.run()
	
	
	
