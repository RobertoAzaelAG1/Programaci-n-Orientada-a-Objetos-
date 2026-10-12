class Figuras:
    def __init__(self,ejex, ejey, visible):
        self.ejex=ejex
        self.ejey=ejey
        self.visible=visible

    def estaVisible(self):
        return self.visible

    def mostrar(self):
        self.visible=True

    def ocultar(self):
        self.visible=False
    

    def mover(self,ejex, ejey):
        self.ejex+=ejex
        self.ejey+=ejey
        

    def calcularArea(self):
        return self.ejex+self.ejey

class Circulos(Figuras):
    def __init__(self, ejex, ejey, visible,radio):
        super().__init__(ejex, ejey, visible)
        self.__radio=radio

    def getRadio(self):
        return self.__radio

    def setRadio(self, radio):
        self.__radio=radio

    def ocultar(self):
        self.visible=False

    def mostrar(self):
        self.visible=True
        

    def calcularArea(self, radio):
        return 3.1416*radio**2

class Rectangulos(Figuras):
    def __init__(self, ejex, ejey, visible, alto, ancho):
        super().__init__(ejex, ejey, visible)
        self.__alto=alto
        self.__ancho=ancho

    def ocultar(self):
        self.visible=False

    def mostrar(self):
        self.visible=True

    def calcularArea(self):
        return self.__ancho*self.__alto

rectangulo1=Rectangulos(3,4,True,10,20)
circulo1=Circulos(3,3,True,6)


        