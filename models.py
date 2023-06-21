from config import db
from sqlalchemy import Column, Integer, String


class User(db.Model):
	__tablename__ = 'User'
	ID = Column(Integer, primary_key=True)
	Username = Column(String (30))
	Password = Column(String (30))
	Phone = Column(Integer)



# class nhatro(db.Model):
#     __tablename__ = 'nhatro'  #ten bang csdl
#     gid = serial NOT NULL
#     stt = Column(numeric)
#     x = Column(double precision)
#     y = Column(double precision)
#     chutro = Column(character varying(254))
#     lienhe = Column(character varying(254))
#     diachi = Column(character varying(254))
#     phuongxa = Column(character varying(254))
#     quanhuyen = Column(character varying(254))
#     dientich = Column(double precision)
#     songuoi = Column(double precision)
#     nhavesinh = Column(character varying(254))
#     gia = Column(double precision)
#     tiencoc = Column(double precision)
#     dien_kwh = Column(double precision)
#     nuoc = Column(character varying(254))
#     wifi = Column(double precision)
#     nhadexe =  Column(character varying(254))
#     chiphikhac = Column(character varying(254))
#     gio = Column(character varying(254))
#     bep = Column(character varying(254))
#     sanphoi = Column(double precision)
#     noithat = Column(character varying(254))
#     mahoant =  Column(character varying(254))
#     anninh = Column(character varying(254))
#     mahoaan = Column(character varying(254))
#     tienichkha = Column(character varying(254))
#     ghichu = Column(Integer)
#     phuongxa2 = Column(Integer)
#     geom = geometry(Point,4326)
