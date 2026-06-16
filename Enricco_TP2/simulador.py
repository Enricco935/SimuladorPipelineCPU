from pipeline import Pipeline

def recurso_em_uso(matriz, termo, coluna):

    for linha in matriz:

        if coluna >= len(linha):
            continue

        i = coluna

        while i >= 0:

            if f"({termo})" in linha[i]:
                return True

            if linha[i] != "ST":
                break

            i -= 1

    return False

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

        for i, tarefa in enumerate(pipeline.tarefas):
            progressoTarefa = i + 1 #ignora a primeira coluna de labels
            dados.append([])
            dados[i].append(f"T{tarefa.id}({tarefa.tipo})")
            
            
            for j in range(i):
                dados[i].append(" ")

            for estagio in tarefa.estagios:

                k = 0
                if 'A' in tarefa.tipo:
                    while k < estagio.ciclosConsumidos:
                        for l in range(i+1):
                            if len(dados[l]) <= progressoTarefa:
                                dados[l].append(" ")

                        if not recurso_em_uso(dados, estagio.recursoUtilizadoA, progressoTarefa):
                            dados[i][progressoTarefa] = f"{estagio.nome}({estagio.recursoUtilizadoA})"
                            k += 1
                        else:
                            dados[i][progressoTarefa] = "ST"
                        progressoTarefa += 1
                else:
                    while k < estagio.ciclosConsumidos:
                        for l in range(i+1):
                            if len(dados[l]) <= progressoTarefa:
                                dados[l].append(" ")

                        if not recurso_em_uso(dados, estagio.recursoUtilizadoB, progressoTarefa):
                            dados[i][progressoTarefa] = f"{estagio.nome}({estagio.recursoUtilizadoB})"
                            k += 1
                        else:
                            dados[i][progressoTarefa] = "ST"
                        progressoTarefa += 1

        colunas = ["Tarefa"]
        for k in range(progressoTarefa):
            colunas.append(f"{k+1}")

        return dados, colunas
