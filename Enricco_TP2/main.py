from pipeline import Pipeline, printar_relatorio
from simulador import MaquinaSemPipeline, MaquinaComPipeline, printar_estagios_ciclos
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

dadosC, colunasC, tempoC, qtd_stalls = pipeC.rodar(pipe)
salvar_tabela(dadosC, colunasC, "maquinaComPipeline")

printar_relatorio(pipe.tarefas, len(pipe.tarefas), pipeM.tempoTotal, tempoC, qtd_stalls, len(pipe.estagios), )
#printar_estagios_ciclos(dadosC)