from pipeline import Pipeline


estagios = []
tarefas = []
pipe = Pipeline(estagios, tarefas)
pipe.configurar_estagios()
pipe.preencher_tarefas()

print(pipe.estagios)
