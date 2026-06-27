from pipeline import Pipeline
from simulador import MaquinaSemPipeline, MaquinaComPipeline
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

dadosC, colunasC = pipeC.rodar(pipe)#Roda as tarefas com pipeline 
salvar_tabela(dadosC, colunasC, "maquinaComPipeline")#Cria a tabela da maquina com pipeline