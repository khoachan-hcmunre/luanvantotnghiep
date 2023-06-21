from flask import render_template, request, redirect
from flask import url_for, Flask, session, abort
from flask_wtf import Form

from flask_sqlalchemy import SQLAlchemy 
from flask_wtf.csrf  import CSRFProtect
import psycopg2

chuoi_ketnoi = 'postgresql://postgres:postgres@localhost:5432/nhonduc'

app = Flask(__name__)
app.secret_key = 's3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = chuoi_ketnoi
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

app = Flask(__name__, static_folder='D:/webgis/bin/webapps/geoserver/WEBGIS/templates/static' )

from services import truyvandulieu

conn = psycopg2.connect(database="nhonduc", user="postgres", password="postgres", host="", port="5432")
print ("Opened database successfully")
# print('Data result from Nhon Duc' , result)
@app.route('/', methods = ['GET', 'POST']) # trang chu
def bando():
  ketqua = "----------------"
  if request.method == 'POST':
    soto = request.form['sotohtml']
    sothua = request.form['sothuahtml']
    print ("Do dai cua so to va so thua la: " + str(len(soto)) + "  " + str(len(sothua)))
    if len(soto) > 0 and len(sothua) >0:
      # thuc hien truy van:
      ketqua = truyvandulieu(conn , soto, sothua)
      print('Ket qua: ', ketqua)
    
  return render_template('index.html', danhsach = ketqua)


if __name__ == '__main__':
  app.run(debug = True, port = 5050)