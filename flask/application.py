from flask import render_template, request, redirect
from flask import url_for, Flask, session, abort
from flask_wtf import Form

from flask_sqlalchemy import SQLAlchemy 
from flask_wtf.csrf  import CSRFProtect

chuoi_ketnoi = 'postgresql://postgres:123@localhost/dulieu'

app = Flask(__name__) # < du thua
app.secret_key = 's3cr3t'
app.config['SQLALCHEMY_DATABASE_URI'] = chuoi_ketnoi
app.config['WTF_CSRF_ENABLED'] = False
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
csrf = CSRFProtect(app)

app = Flask(__name__, static_folder='F:\\_______Sinhvien\\flask' )

from services import truyvandulieu


@app.route('/', methods = ['GET', 'POST']) # trang chu
def bando1():
  ketqua = "----------------"
  if request.method == 'POST':
    soto = request.form['soto_html']
    sothua = request.form['sothua_html']
    print ("Do dai cua so to va so thua la: " + str(len(soto)) + "  " + str(len(sothua)))
    if len(soto) > 0 and len(sothua) >0:
      # thuc hien truy van:
      ketqua = truyvandulieu(soto, sothua)
    
  return render_template('web1.htm', cautruyvan = ketqua)


if __name__ == '__main__':
  app.run(debug = True, port = 5050)




