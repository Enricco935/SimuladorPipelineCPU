from pipeline import Pipeline, printar_relatorio
from simulador import MaquinaSemPipeline, MaquinaComPipeline, printar_estagios_ciclos
from plot import salvar_tabela
import sys


if len(sys.argv) != 2:
    print("Uso: python main.py <saida>")
    sys.exit(1)
arquivo_saida = sys.argv[1]


estagios = []
tarefas = []

pipe = Pipeline(estagios, tarefas)#Cria um objeto o tipo da pipeline 

pipe.configurar_estagios()#Preenche os estagios 
pipe.preencher_tarefas()#Preenche as tarefas 

pipeM = MaquinaSemPipeline(pipe)#Cria um objeto da classe Sem Pipeline 
pipeC = MaquinaComPipeline()#Cria um objeto da classe Com Pipeline 

dadosConfig, colunasConfig = pipe.config()#retona dados e colunas pra criar a tabela de configuração digitada
salvar_tabela(dadosConfig, colunasConfig, f"{arquivo_saida}(configPipeline)")

dadosS, colunasS = pipeM.rodar(pipe)#Roda as tarefas sem pipeline 
salvar_tabela(dadosS, colunasS, f"{arquivo_saida}(maquinaSemPipeline)")#Cria a tabela da maquina sem pipeline 

dadosC, colunasC, tempoC, qtd_stalls = pipeC.rodar(pipe)
salvar_tabela(dadosC, colunasC, f"{arquivo_saida}(maquinaComPipeline)")

printar_relatorio(pipe.tarefas, len(pipe.tarefas), pipeM.tempoTotal, tempoC, qtd_stalls, len(pipe.estagios), f"{arquivo_saida}(relatorio)")

