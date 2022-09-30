class estudiante():
    def __init__(self, nombre, grado, promedio):
        self.nombre = nombre
        self.grado = grado
        self.promedio = promedio
    def verEst(self):
        return self.nombre
    def verGrado(self):
        return self.grado
    def verPromedio(self):
        return self.promedio