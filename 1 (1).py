class Forma:
    def area(self):
        raise NotImplementedError("Las subclases deben implementar este método")

class Circulo(Forma):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio * self.radio

class Cuadrado(Forma):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado

class Rectangulo(Forma):
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def area(self):
        return self.largo * self.ancho


formas = [Circulo(5), Cuadrado(4), Rectangulo(3, 6)]
for forma in formas:
    print(f"Área: {forma.area()}")
