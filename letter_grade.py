_vize = input("Vize : ")
_final = input("Final : ")

try:
 _vize_top = int(_vize)*(4/10)
 _final_top = int(_final)*(6/10)
 _sonuc = float(_vize_top + _final_top)


 if int(_final) <= 49 :
  print("Harf Notunuz : FF")
  print("Finalde 50'Den Düşük Aldığınız İçin Kaldınız" )
 elif _sonuc >= 90:
  print("Harf Notunuz : AA")
  print("Geçtiniz!")
 elif _sonuc >=85 :
  print("Harf Notunuz : BA")
  print("Geçtiniz!")
 elif _sonuc >=80 :
  print("Harf Notunuz : BB")
  print("Geçtiniz!")
 elif _sonuc >= 75:
  print("Harf Notunuz : CB")
  print("Geçtiniz!")
 elif _sonuc >= 70:
  print("Harf Notunuz : CC")
  print("Geçtiniz!")
 elif _sonuc >= 65:
  print("Harf Notunuz : DC")
  print("Geçtiniz!")
 elif _sonuc >= 60:
  print("Harf Notunuz : DD")
  print("Geçtiniz!")
 elif _sonuc <= 55:
  print("Harf Notunuz : FF")
  print("Kaldınız!")

 print("Ortalamanız : ", _sonuc)
except (ValueError):
  print("Bir Hata Oluştu")
  print("Lütfen Sayısal İfadeler Giriniz ve Not Alanlarını Boş Bırakmayınız...")