print("\033c")


class Coches:
    def __init__(self, color, marca, velocidad, potencia, asientos, modelo):
        self._color = color
        self._marca = marca
        self._velocidad = velocidad
        self._potencia = potencia
        self._asientos = asientos
        self._modelo = modelo

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def velocidad(self):
        return self._velocidad

    @velocidad.setter
    def velocidad(self, velocidad):
        self._velocidad = velocidad

    @property
    def potencia(self):
        return self._potencia

    @potencia.setter
    def potencia(self, potencia):
        self._potencia = potencia

    @property
    def asientos(self):
        return self._asientos

    @asientos.setter
    def asientos(self, asientos):
        self._asientos = asientos

    @property
    def modelo(self):
        return self._modelo

    @modelo.setter
    def modelo(self, modelo):
        self._modelo = modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1


class Camiones(Coches):
    def __init__(self, color, marca, velocidad, potencia, asientos, modelo, capacidadCarga, eje):
        super().__init__(color, marca, velocidad, potencia, asientos, modelo)
        self._capacidadCarga = capacidadCarga
        self._eje = eje

    @property
    def capacidadCarga(self):
        return self._capacidadCarga

    @capacidadCarga.setter
    def capacidadCarga(self, capacidadCarga):
        self._capacidadCarga = capacidadCarga

    @property
    def eje(self):
        return self._eje

    @eje.setter
    def eje(self, eje):
        self._eje = eje

    def cargar(self, tipoCarga):
        print(f"El tipo de carga del camion es: {tipoCarga}")

    def acelerar(self):
        self.velocidad += 1
        print("Estoy acelerando en un camion")

    def frenar(self):
        self.velocidad -= 1


class Camionetas(Coches):
    def __init__(self, color, marca, velocidad, potencia, asientos, modelo, traccion, cerrada):
        super().__init__(color, marca, velocidad, potencia, asientos, modelo)
        self._traccion = traccion
        self._cerrada = cerrada

    @property
    def traccion(self):
        return self._traccion

    @traccion.setter
    def traccion(self, traccion):
        self._traccion = traccion

    @property
    def cerrada(self):
        return self._cerrada

    @cerrada.setter
    def cerrada(self, cerrada):
        self._cerrada = cerrada

    def transportar(self, num_pasajeros):
        print(f"El numero de pasajeros de la camioneta es: {num_pasajeros}")

    def cargar(self, tipoCarga):
        print(f"El tipo de carga de la camioneta es: {tipoCarga}")

    def acelerar(self):
        self.velocidad += 1
        print("Estoy acelerando en una camioneta")

    def frenar(self):
        self.velocidad -= 1
