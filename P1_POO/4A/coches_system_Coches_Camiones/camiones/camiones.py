from coches import coches


class Camiones(coches.Coches):
    def __init__(self, color, marca, velocidad, potencia, asientos, modelo,eje,capacidadCarga):
        super().__init__(color, marca, velocidad, potencia, asientos, modelo)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    def acelerar(self):
        self._velocidad+=2

    def frenar(self):
        self._velocidad-=1

    def cargar(self,tipo_carga):
        print(f"El tipo de carga es: {tipo_carga}")
        
        

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

    @property
    def eje(self):
        return self.__eje
    
    @eje.setter
    def eje(self,eje):
        self.__eje=eje

    @property
    def capacidadCarga(self):
        return self.__capacidadCarga

    @capacidadCarga.setter
    def capacidadCarga(self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga






