Relatório do Trabalho: Simulador de Pipeline de CPU

Integrantes:
    Enricco Faria
    João Vitor da Silva Silvério

Descrição do trabalho:
Este trabalho implementa um simulador de pipeline de CPU que compara a execução de tarefas em três cenários:
- Pipeline ideal,
- Pipeline com hazard estrutural,
- Pipeline com sequência mista de tarefas.

O objetivo é demonstrar como a técnica de pipeline aumenta o desempenho ao sobrepor estágios de instruções e como hazards e uso misto de recursos afetam o tempo de execução.

Explicação da implementação:
O programa foi desenvolvido em Python e usa as seguintes etapas:
- Leitura e configuração dos estágios do pipeline e das tarefas.
- Simulação da execução em uma máquina sem pipeline, obedecendo a execução sequencial completa.
- Simulação da execução em uma máquina com pipeline, com gerenciamento de stalls e recursos.
- Geração de tabelas de saída e relatório de desempenho para comparar os dois modos de execução.

A implementação principal está em `main.py`, que chama `Pipeline` para configurar os estágios e tarefas, `MaquinaSemPipeline` para simular a execução sem pipeline e `MaquinaComPipeline` para simular o pipeline real. Também grava os resultados em arquivos de saída com prefixo definido pelo usuário.

Descrição dos testes:
Foram utilizados três testes principais com entradas já criadas:
- `pipelineIdeal.txt`: simulação de pipeline ideal sem conflitos de recurso.
- `pipelineHazardEstrutural.txt`: simulação com hazard estrutural, onde há conflito de recursos e stalls.
- `pipelineSequenciaMista.txt`: simulação com tarefas mistas que variam os recursos e tipos de instrução.

Cada teste foi executado usando redirecionamento da entrada padrão para o arquivo desejado e um nome de saída específico.

Análise dos resultados:
- Pipeline ideal obteve um ótimo desempenho, pois a execução pôde ser sobreposta sem interferências significativas.
- Pipeline com hazard estrutural apresentou stalls que aumentaram o tempo necessário para processar o pipeline.
- Sequência mista também obteve um ótimo resultado, pois a variação de recursos permitiu maior aproveitamento do pipeline e menor penalidade por stalls.

Discussão crítica sobre desempenho:
O desempenho do pipeline ideal demonstra a vantagem clara da técnica quando não há conflitos de recurso. No entanto, a presença de hazards estruturais mostra que o ganho de desempenho pode ser reduzido se as instruções competirem pelos mesmos recursos.

A sequência mista evidencia que, em cargas de trabalho diversificadas, o pipeline pode manter bom desempenho porque as diferentes tarefas usam recursos variados e reduzem o acúmulo de stalls. Ainda assim, o simulador destaca a importância de detectar e mitigar hazards para manter a eficiência do pipeline.

Como usar o programa:

1. Execução normal:
   python main.py <arquivo_saida>

   Exemplo:
   python main.py resultado

   O programa irá ler os dados de configuração e as tarefas via teclado/interação e gerar os arquivos:
   - resultado(configPipeline)
   - resultado(maquinaSemPipeline)
   - resultado(maquinaComPipeline)
   - resultado(relatorio)

2. Usar entradas já criadas:
   python main.py <arquivo_saida> < pipelineIdeal.txt
   python main.py <arquivo_saida> < pipelineHazardEstrutural.txt
   python main.py <arquivo_saida> < pipelineSequenciaMista.txt

   Esses comandos redirecionam a entrada padrão para os arquivos de exemplo já existentes.

Observações:
- O parâmetro <arquivo_saida> é o prefixo usado nos arquivos de saída.
- Os arquivos de entrada prontos já contêm a sequência de estágios e tarefas do simulador.
- O relatório final é salvo em um arquivo com o sufixo "(relatorio)".
