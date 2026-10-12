#Programa principal desde la que se manda llamar los objetos de la clase de coches

from coches import Coches, Camiones, Camionetas

coche1=Coches("Blanco","VW",220,150,5,"2020")
coche2=Coches("Blanco","Nissan",180,120,5,"2021")

camion1=Camiones("Negro", "Dina", "2020", 180, 300, 12, 8, 2500)
camion2=Camiones("Azul", "Star", "2019", 150, 200, 14, 6, 2000)

camioneta1=Camionetas("Amarillo", "Renault", "2025", 240, 250, 8, "Delantera", True)
camioneta2=Camionetas("Blanca", "Nissan", "2020", 180, 150, 6, "Trasera", False)

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

