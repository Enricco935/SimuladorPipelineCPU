from pipeline import Pipeline
from simulador import MaquinaSemPipeline, MaquinaComPipeline
from plot import salvar_tabela

estagios = []
tarefas = []

pipe = Pipeline(estagios, tarefas)

pipe.configurar_estagios()
pipe.preencher_tarefas()

pipeM = MaquinaSemPipeline(pipe)
pipeC = MaquinaComPipeline()

dadosConfig, colunasConfig = pipe.config()#retona dados e colunas pra criar a tabela
salvar_tabela(dadosConfig, colunasConfig, "configPipeline")

dadosS, colunasS = pipeM.rodar(pipe)
salvar_tabela(dadosS, colunasS, "maquinaSemPipeline")

dadosC, colunasC = pipeC.rodar(pipe)
salvar_tabela(dadosC, colunasC, "maquinaComPipeline")