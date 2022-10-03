class Casa:

    def __init__(self, color):
        self.color = color
        self.consumo_luz = 0
        self.consumo_agua = 0

    def pintar(self, color):
        self.color = color

    def prender_luz(self):
        self.consumo_luz += 10

    def abrir_ducha(self):
        self.consumo_agua += 10

    def tocar(self):
        print("toc, toc")
        self.consumo_luz += 2

mi_casa = Casa("rojo")
print(mi_casa.color)
print(mi_casa.consumo_luz)

mi_casa.tocar()
mi_casa.prender_luz()

class Mansion(Casa):

    def prender_luz(self):
        self.consumo_luz += 10

    def abrir_ducha(self):
        self.consumo_agua += 10

    def tocar_timbre(self):
        print("toc, toc")
        self.consumo_luz += 2


mi_mansion = Mansion("blanco")
print(mi_mansion)