

class Estagio:
    def __init__(self, nome, ciclosConsumidos, recursoUtilizadoA, recursoUtilizadoB):
        self.nome = nome
        self.ciclosConsumidos = ciclosConsumidos
        self.recursoUtilizadoA = recursoUtilizadoA
        self.recursoUtilizadoB = recursoUtilizadoB

    def __repr__(self):
        return f"Estagio(nome='{self.nome}', ciclos={self.ciclosConsumidos}, RecA='{self.recursoUtilizadoA}', RecB='{self.recursoUtilizadoB}')"
    