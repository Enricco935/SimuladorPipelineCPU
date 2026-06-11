
class Tarefa:
    def __init__(self, id, tipo):
        self.id = id
        self.tipo = tipo

    def __repr__(self):
        return f"T{self.id}({self.tipo})"