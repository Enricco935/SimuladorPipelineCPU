from pipeline import Pipeline, printar_relatorio
from simulador import MaquinaSemPipeline, MaquinaComPipeline, printar_estagios_ciclos
from plot import salvar_tabela

estagios = []
tarefas = []

pipe = Pipeline(estagios, tarefas)#Cria um objeto o tipo da pipeline 

pipe.configurar_estagios()#Preenche os estagios 
pipe.preencher_tarefas()#Preenche as tarefas 

pipeM = MaquinaSemPipeline(pipe)#Cria um objeto da classe Sem Pipeline 
pipeC = MaquinaComPipeline()#Cria um objeto da classe Com Pipeline 

dadosConfig, colunasConfig = pipe.config()#retona dados e colunas pra criar a tabela de configuração digitada
salvar_tabela(dadosConfig, colunasConfig, "configPipeline")

dadosS, colunasS = pipeM.rodar(pipe)#Roda as tarefas sem pipeline 
salvar_tabela(dadosS, colunasS, "maquinaSemPipeline")#Cria a tabela da maquina sem pipeline 

dadosC, colunasC, tempoC, qtd_stalls = pipeC.rodar(pipe)
salvar_tabela(dadosC, colunasC, "maquinaComPipeline")

printar_relatorio(pipe.tarefas, len(pipe.tarefas), pipeM.tempoTotal, tempoC, qtd_stalls, len(pipe.estagios), )
#printar_estagios_ciclos(dadosC)
