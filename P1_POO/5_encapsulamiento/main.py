#Programa principal desde la que se manda llamar los objetos de la clase de coches
from coches import Coches

coche1=Coches("Blanco","VW",220,150,5,"2020")
coche2=Coches("Blanco","Nissan",180,120,5,"2021")

print(coche1.getVelocidad())
for i in range(1,101):
    coche1.acelerar()


print(coche1.getVelocidad())

coche1.setVelocidad(400)
print(coche1.getVelocidad())

print("\033c")
print(coche1.getColor())
print(coche1.getMarca())
print(coche1.getVelocidad())
print(coche1.getPotencia())
print(coche1.getAsientos())
print(coche1.getModelo())

