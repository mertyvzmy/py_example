import datetime as dt

try:
 _birth_day = input("Doğduğunuz Günü Giriniz (gg.aa.yyyy) : ")
 _birth_day = (dt.datetime.strptime(_birth_day, "%d.%m.%Y"))
 _now = dt.datetime.now()
 _age = _now - _birth_day


 _hour = _age.days * 24
 _minute = _hour * 60
 _year = _age.days // 365
 _month = _age.days % 365 // 30
 _day = _age.days % 365 % 30
 _week = _age.days // 7

 print(_minute, " Dakika")
 print(_hour," Saat")
 print(_age.days," Gün")
 print(_week," Hafta")
 print(_year,"Yıl", _month, "Ay", _day,"Gündür Hayattasın")
except (ValueError):
    print("Lütfen Formata Uygun Şekilde Tarihi Giriniz.")