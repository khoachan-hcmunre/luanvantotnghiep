### File services.py


def truyvandulieu(chuoi_ketnoi, soHieuToBa = "", soThuTuThu = ""):
  cur = chuoi_ketnoi.cursor()
  str = ""
  if len(soHieuToBa) >0 and len(soThuTuThu)>0:
    str = "select *, st_x((st_centroid(geom))) as x, st_y((st_centroid(geom))) as y  from Thuadat "
    str = str + "where sohieutoba =" + soHieuToBa + " and sothututhu  =" + (soThuTuThu) + " "
    print("Truy van = " + str)
    cur.execute(str)
    rows = cur.fetchall()
    danhsach = []
    for row in rows:
      thuadat = convertRowData(row)
      danhsach.append(thuadat)
    #cur.commit()
    #cur.close()
    print(len(danhsach))
    print(danhsach)
  return danhsach 

def convertRowData(row):
   return {"maxa": row[4],"loaidat": row[5],"dientich": row[2],"sohieutoba": row[7], "sothututhu": row[8], "diachichit": row[3], "hoten": row[4], "x": row[13],"y": row[14]}