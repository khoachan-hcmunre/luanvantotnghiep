### File services.py


def truyvandulieu(soto_text = "", sothua_text = ""):
  str = ""
  if len(soto_text) >0 and len(sothua_text)>0:
    str = "select * from thuadat where soto = " + soto_text + " and sothua = " + sothua_text
  return str





