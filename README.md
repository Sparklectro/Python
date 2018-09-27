# Python
Python Repository

Muhammad Ali-Frazer Box Match- Random Health Players

# There are 3 characters in this box match.
#For one round two players attack randomly to eachother and one of them , Frazer, wins by also attacking referee.
#Print who wins!!
#Turkish/English versions.

---TURKISH VERSION---

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

---ENGLISH VERSION---


from __future__ import print_function
MuhammedAli_health = 200
MuhammedAli_damage = 15
Frazer_health = 150
Frazer_damage= 25
Referee_health = 180
Referee_damage= 30

def box_match(damage,opponent_health):
    opponent_health = opponent_health - damage
    return opponent_health

while Frazer_health>0 and MuhammedAli_health>0 and Referee_Health>0:
     MuhammedAli_health = box_match(Frazer_damage,MuhammedAli_health)
     Frazer_health = box_match(MuhammedAli_damage, Frazer_health)
     Referee_health = box_match(Frazer_damage,Referee_health)


     print(MuhammedAli_health,Frazer_health,Hakem_health)


     class Character:
         health = 150
         damage_min = 25
         damage_max = 30

         def war(self, opponent):
             opponent.health = opponent.health - random.randint(self.damage_min, self.damage_max)


     print()
     print()

     import random

     char1 = Character()
     char2 = Character()
     char2.damage_max = 35
     char2.damage_min = 30

     # char1.damage = 30 
     #We can diffentiate by assigning inside parantheses.
     # print(char1.damage,char1.health)

     while char1.health > 0 and char2.health > 0:
         char1.war(char2)
         char2.war(char1)
         print(char1.health, char2.health)

result = 'Frazer Wins!'
print(result)

     # Frazer who attacks MuhammedAli and Referee.
      # Frazer Wins!
