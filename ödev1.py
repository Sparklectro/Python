#odev :
# 3 karakter olsun
#her round da 1 kisi diger 2 kisiye saldiricak (ayni anda degil) rastgele(sirayla degil)
#kazananı ekrana bastir

from __future__ import print_function
MuhammedAli_can = 200
MuhammedAli_hasar = 15
Frazer_can = 150
Frazer_hasar = 25
Hakem_can = 180
Hakem_hasar = 30

def kavga(hasar,rakip_can):
    rakip_can = rakip_can - hasar
    return rakip_can

while Frazer_can>0 and MuhammedAli_can>0 and Hakem_can>0:
     MuhammedAli_can = kavga(Frazer_hasar,MuhammedAli_can)
     Frazer_can = kavga(MuhammedAli_hasar, Frazer_can)
     Hakem_can = kavga(Frazer_hasar,Hakem_can)

     print(MuhammedAli_can,Frazer_can,Hakem_can)


     class Karakter:
         can = 150
         hasar_min = 25
         hasar_max = 30

         def savas(self, rakip):
             rakip.can = rakip.can - random.randint(self.hasar_min, self.hasar_max)


     print()
     print()

     import random

     kar1 = Karakter()
     kar2 = Karakter()
     kar2.hasar_max = 35
     kar2.hasar_min = 30

     # kar1.hasar = 30 #atama yaparak iceriyi degistirebiliyoruz
     # print(kar1.hasar,kar1.can)

     while kar1.can > 0 and kar2.can > 0:
         kar1.savas(kar2)
         kar2.savas(kar1)
         print(kar1.can, kar2.can)

sonuç = 'Frazer Kazandı'
print(sonuç)

     # Frazer Muhammed Ali ile Hakem'e saldıran boksör.
      # Frazer kazandı.





