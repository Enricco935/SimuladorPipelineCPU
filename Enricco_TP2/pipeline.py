from estagio import Estagio
from tarefa import Tarefa

def printar_relatorio(seq_tarefas, qtd_tarefas, tmp_sem_pipeline, tmp_com_pipeline, qtd_stalls, latencia):

    print("=" * 40)
    print("RELATÓRIO DA SIMULAÇÃO")
    print("=" * 40)

    print(f"Sequência de tarefas : {"".join(tarefa.tipo for tarefa in seq_tarefas)}")
    print(f"Quantidade de tarefas: {qtd_tarefas}")
    print(f"Tempo sem pipeline   : {tmp_sem_pipeline} ciclos")
    print(f"Tempo com pipeline   : {tmp_com_pipeline} ciclos")
    print(f"Quantidade de stalls : {qtd_stalls}")
    print(f"Latência             : {latencia:.2f} ")
    print(f"Vazão (Throughput)   : {latencia/tmp_com_pipeline:.2f} tarefas/ciclo")
    print(f"Speedup              : {tmp_sem_pipeline/tmp_com_pipeline:.2f}")

    print("=" * 40)

class Pipeline:
    def __init__(self, estagios, tarefas):
        self.estagios = estagios
        self.tarefas = tarefas

    def configurar_estagios(self):
        
        while True:#Pega a quantidade de estagios que tem a pipeline (entre 1 e 8)
            qtd = int(input("Quantos estagios quer configurar? "))
            if 0 < qtd < 9:
                break
            else:
                print("Quantidade de estágios deve estar entre 1 e 8!")

        for i in range(qtd):#Pega nome,recurso e qtd de ciclos desses estagios
            print(f"=============== ESTAGIO {i+1} ===============")
            nomeEstagio = input("Nome do Estagio: ").upper()
            ciclosConsumidos = int(input("Quantidade de Ciclos Consumidos: "))
            recursoUtilizado = input("Recurso Utilizado: ").upper()

            self.estagios.append(Estagio(nomeEstagio, ciclosConsumidos, recursoUtilizado, recursoUtilizado))

        for i,estagio in enumerate(self.estagios):
            print(f"[ {i} ] {estagio.nome}")

        idx = int(input('Qual estagio usa dois recursos? (-1 para "Nenhum")'))#Pega se algum dos estagios usa mais de um recurso dependendo do tipo
        if 0 <= idx < len(self.estagios):# verifica se o indice digitado é valido
            self.estagios[idx].recursoUtilizadoA = input("Recurso do tipo A: ")
            self.estagios[idx].recursoUtilizadoB = input("Recurso do tipo B: ")
        else: 
            print("Indice digitado inválido. Considerando que nenhum estágio usa dois recursos.")

    def preencher_tarefas(self):

        tarefas = list(input("Digite as tarefas: ").upper())#Pega as tarefas(instruções)

        for tarefa in tarefas:#Verifica se todas tarefas digitadas são A e B
            if tarefa not in ("A", "B"):
                raise ValueError("As tarefas devem ser apenas A ou B")

        if len(tarefas) > 8:
            del tarefas[8:] #deleta do indice 8 pra frente
            print(f"ATENCAO! Foram consideradas apenas as 8 primeiras tarefas:\n\t{tarefas}")

        for id, tarefa in enumerate(tarefas):
            self.tarefas.append(Tarefa(id+1, tarefa, self.estagios))
                      
    def config(self):#Dados para a tabela de configuração digitada
        colunas =["Estagio", "Duracao", "Recurso Tipo A", "Recurso Tipo B"]

        dados = []
        for i, estagio in enumerate(self.estagios):
            dados.append([])
            dados[i].append(f"{estagio.nome}")
            dados[i].append(f"{estagio.ciclosConsumidos}")
            dados[i].append(f"{estagio.recursoUtilizadoA}")
            dados[i].append(f"{estagio.recursoUtilizadoB}")

        return dados, colunas


