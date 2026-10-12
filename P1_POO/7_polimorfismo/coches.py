"""  
 Programación Orinetada a Objetos POO o OOP

CLASES .- es como un molde a traves del cual se puede instanciar un objeto dentro de las clases se definen los atributos (propiedades / caracteristicas) y los métodos (funciones o acciones)

OBJETOS O INSTANCIAS .- son parte de una clase los objetos o instacias pertenecen a una clase, es decir para interacturar con la clase o clases y hacer uso de los atributos y metodos es necesario crear un objeto o objetos.

METODO CONSTRUCTOR.- Este metodo especial dentro de una clase y se utiliza para dar un valor a los atributos del objeto al crearlo, es el primer metodo que se ejecuta al crear el objeto y se manda llamar automaticamente al crearlo, es decir este metodo puede recibir parametros al momento de crear el objeto 

Cuando se crear un metodo constructor se utiliza la funcion _init_(), para que se llame automáticamente cada vez que se utiliza la clase para crear un nuevo objeto.

El self es un parámetro es una referencia a la instancia actual de la clase y se utiliza para acceder a variables que pertenecen a la clase.

No es necesario que tenga nombre self, puedes llamarlo como quieras, pero tiene que ser el primer parámetro de cualquier función de la clase. Es decir por regla se utiliza en la palabra self pero puede ser llamado con otro nombre por ejemplo: valor, abd, parametro, etc.

"""

#Ejemplo 1 Crear una clase (un molde para crear mas objetos)llamada Coches y apartir de la clase crear objetos o instancias (coche) con caracteristicas similares

print("\033c")
class Coches:
    def __init__(self,color,marca,velocidad,potencia,asientos,modelo):
        self.__color=color
        self.__marca=marca
        self.__velocidad=velocidad
        self.__potencia=potencia
        self.__asientos=asientos
        self.__modelo=modelo
        
    
    def acelerar(self):
        self.__velocidad+=1
    def frenar(self):
        self.__velocidad-=1
#Multiples objetos

    def getVelocidad(self):
        return self.__velocidad 
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad

    def getMarca(self):
        return self.__marca
    def setMarca(self,marca):
        self.__marca=marca

    def getColor(self):
        return self.__color
    def setColor(self,color):
        self._color=color

    def getPotencia(self):
        return self.__potencia
    def setPotencia(self,potencia):
        self._potencia=potencia

    def getAsientos(self):
        return self.__asientos
    def setAsientos(self,asientos):
        self.__asientos=asientos

    def getModelo(self):
        return self.__modelo
    def setModelo(self,modelo):
        self.__modelo=modelo
    

class Camiones(Coches):
    def __init__(self, color, marca, velocidad, potencia, asientos, modelo, capacidadCarga, eje):
        super().__init__(color, marca, velocidad, potencia, asientos, modelo)
        self.__capacidadCarga=capacidadCarga
        self.__eje=eje

    def cargar(self,tipoCarga):
        print(f"El tipo de carga del camion es: {tipoCarga}")

    def acelerar(self):
        self.__velocidad=+1
        print("Estoy acelerando en un camion")

    def frenar(self):
        self.__velocidad=+1

    def setEje(self,eje):
        self.__eje=eje
    
    def getEje(self):
        return self.__eje

    def setCapacidad_carga(self,capcidadCarga):
        self.__capacidadCarga=capcidadCarga
        
    def getCapacidad_carga(self):
        return self.__capacidadCarga

class Camionetas(Coches):
    def __init__(self, color, marca, velocidad, potencia, asientos, modelo, traccion, cerrada):
        super().__init__(color, marca, velocidad, potencia, asientos, modelo)
        self.__traccion=traccion
        self.__cerrada=cerrada

    def tranportar(self,num_pasajeros):
        print(f"El numero de pasajeros de la camioneta es: {num_pasajeros}")

    def cargar(self,tipoCarga):
        print(f"El tipo de carga del camion es: {tipoCarga}")
    
    def acelerar(self):
        self.__velocidad=+1
        print("Estoy acelerando en una camioneta")
    
    def frenar(self):
        self.__velocidad=+1

    def setTraccion(self,traccion):
        self.__traccion=traccion

    def getTraccion(self):
        return self.__traccion

    def setCerrada(self,cerrada):
        self.__cerrada=cerrada

    def getCerrada(self):
        return self.__cerrada



#ejemplo de anidacion en clase
class CamionesCarga(Camiones):
    def __init__(self, color, marca, velocidad, potencia, asientos, modelo, capacidadCarga, eje, tipoCarga):
        super().__init__(color, marca, velocidad, potencia, asientos, modelo, capacidadCarga, eje)
        self._tipoCarga=tipoCarga
