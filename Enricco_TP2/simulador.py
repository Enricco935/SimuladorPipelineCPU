from pipeline import Pipeline

def recurso_em_uso(matriz, termo, coluna):

    for linha in matriz:
        i = coluna
        while i >= 0:

            if f"({termo})" in linha[i]:
                return linha[i], linha[0]

            if linha[i] != "ST":
                break

            i -= 1

    return None

def tentou_usar(linha):
    for estagio in linha:
        if "ST" != estagio:
            return estagio 

def printar_stall(ciclo, tarefa_usando, estagio_usando, recurso, tarefa_bloqueada, estagio_bloqueado):

    print(f"\nCiclo {ciclo}:")
    print(f"- {tarefa_usando} usa {estagio_usando}")
    print(f"- {tarefa_bloqueada} tentaria usar {estagio_bloqueado}")
    print(f"\nComo o recurso {recurso} já está ocupado:")
    print(f"- {tarefa_bloqueada} deve esperar;")
    print("- Stall inserido.")

def printar_estagios_ciclos(matriz):
    for coluna in range(1,len(matriz[0])):

        print(f"Ciclo {coluna}:")
        for linha in matriz:
            if linha[coluna] != " ":

                if "ST" in linha[coluna]:
                    print()
                print(f"{linha[0]} -> {linha[coluna]}")

class MaquinaSemPipeline:
    def calcular_tempos(self, pipeline):
        tempoTarefa = 0

        for estagio in pipeline.estagios:
            tempoTarefa += estagio.ciclosConsumidos
        
        tempoTotal = len(pipeline.tarefas) * tempoTarefa

        return tempoTarefa, tempoTotal
    
    def __init__(self, pipeline):
        self.tempoTarefa, self.tempoTotal = self.calcular_tempos(pipeline)

    def rodar(self, pipeline):
        
        ciclos = 0

        dados = []
        for i, tarefa in enumerate(pipeline.tarefas):
            dados.append([" "] * (self.tempoTotal+1)) 
            dados[i][0] = f"T{tarefa.id}({tarefa.tipo})"

            for estagio in tarefa.estagios:
                if 'A' in tarefa.tipo:
                    for k in range(1, 1 + estagio.ciclosConsumidos):
                        dados[i][ciclos+k] = f"{estagio.nome}({estagio.recursoUtilizadoA})"
                else:
                    for k in range(1, 1 + estagio.ciclosConsumidos):
                        dados[i][ciclos+k] = f"{estagio.nome}({estagio.recursoUtilizadoB})"

                ciclos += estagio.ciclosConsumidos

        colunas = ["Tarefa"]
        for i in range(1,len(dados[0])):
            colunas.append(f"{i}")

        return dados, colunas
   
class MaquinaComPipeline:
    def __init__(self):
        self.ciclos = 0
        self.operacoesCiclo = []

    def rodar(self, pipeline):

        progressoTarefa = 0
        dados = []
        inicio_ultima_tarefa = 1
        qtd_stalls = 0
        
        for i, tarefa in enumerate(pipeline.tarefas):
            progressoTarefa = inicio_ultima_tarefa #ignora a primeira coluna de labels
            dados.append([])#adiciona uma nova linha para a tarefa
            dados[i].append(f"T{tarefa.id}({tarefa.tipo})")# adiciona o texto na matriz
            
            
            for j in range(inicio_ultima_tarefa - 1):#preenche a parte esquerda ta matriz com vazio, a quantidade depende de onde essa tarefa é inserida
                dados[i].append(" ")

            for id_estagio, estagio in enumerate(tarefa.estagios):

                k = 0
                if 'A' in tarefa.tipo:#se a tarefa for do tipo A
                    while k < estagio.ciclosConsumidos:
                        for l in range(i+1):# percorre todas as linhas adicionando vazio 
                            if len(dados[l]) <= progressoTarefa:
                                dados[l].append(" ")

                        resultado = recurso_em_uso(dados, estagio.recursoUtilizadoB, progressoTarefa)
                        if not resultado:
                            if id_estagio == 0 and k == 0:#se for o primeiro ciclo do primeiro estagio
                                inicio_ultima_tarefa = progressoTarefa + 1
                            dados[i][progressoTarefa] = f"{estagio.nome}({estagio.recursoUtilizadoA})"
                            k += 1
                        else:
                            printar_stall(progressoTarefa, resultado[1], resultado[0], estagio.recursoUtilizadoA, dados[i][0], estagio.nome  )
                            dados[i][progressoTarefa] = "ST"
                            qtd_stalls += 1
                        progressoTarefa += 1

                else:
                    while k < estagio.ciclosConsumidos:
                        for l in range(i+1):
                            if len(dados[l]) <= progressoTarefa:
                                dados[l].append(" ")

                        resultado = recurso_em_uso(dados, estagio.recursoUtilizadoB, progressoTarefa)
                        if not resultado:
                            if id_estagio == 0 and k == 0: #se for o primeiro ciclo do primeiro estagio
                                inicio_ultima_tarefa = progressoTarefa + 1
                            dados[i][progressoTarefa] = f"{estagio.nome}({estagio.recursoUtilizadoB})"
                            k += 1
                        else:
                            printar_stall(progressoTarefa, resultado[1], resultado[0], estagio.recursoUtilizadoB, dados[i][0], estagio.nome  )
                            dados[i][progressoTarefa] = "ST"
                            qtd_stalls += 1
                        progressoTarefa += 1

        colunas = ["Tarefa"]
        for k in range(progressoTarefa):
            colunas.append(f"{k+1}")

        return dados, colunas, progressoTarefa-1, qtd_stalls
