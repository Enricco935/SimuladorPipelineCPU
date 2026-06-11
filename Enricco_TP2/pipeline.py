from estagio import Estagio

class Pipeline:
    def __init__(self, estagios, tarefas):
        self.estagios = estagios
        self.tarefas = tarefas

    def configurar_estagios(self):
        
        qtd = int(input("Quantos estagios quer configurar? "))
        for i in range(qtd):
            print(f"=============== ESTAGIO {i+1} ===============")
            nomeEstagio = input("Nome do Estagio: ")
            ciclosConsumidos = int(input("Quantidade de Ciclos Consumidos: "))
            recursoUtilizado = input("Recurso Utilizado: ")

            self.estagios.append(Estagio(nomeEstagio, ciclosConsumidos, recursoUtilizado, recursoUtilizado))

        for i,estagio in enumerate(self.estagios):
            print(f"[ {i} ] {estagio.nome}")
        idx = int(input('Qual estagio usa dois recursos? (-1 para "Nenhum")'))
        if 0 <= idx < len(self.estagios):
            self.estagios[idx].recursoUtilizadoA = input("Recurso do tipo A: ")
            self.estagios[idx].recursoUtilizadoB = input("Recurso do tipo B: ")

    def preencher_tarefas(self):

        self.tarefas = list(input("Digite as tarefas: ").upper())

        for tarefa in self.tarefas:
            if tarefa not in ("A", "B"):
                raise ValueError("As tarefas devem ser apenas A ou B")

        if len(self.tarefas) > 8:
            del self.tarefas[8:]
            print(f"ATENCAO! Foram consideradas apenas 8 tarefas:\n\t{self.tarefas}")
            