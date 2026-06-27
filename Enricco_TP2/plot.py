import matplotlib.pyplot as plt

def salvar_tabela(dados, colunas, arquivo):#Função que pega os dados e cria a tabela em formato png 
        fig, ax = plt.subplots(figsize=(30, 2))
        ax.axis("off")

        tabela = ax.table(
            cellText=dados,
            colLabels=colunas,
            loc="center",
            cellLoc="center"
        )

        tabela.auto_set_font_size(False)
        tabela.set_fontsize(10)
        tabela.scale(1, 2)

        plt.savefig(f"{arquivo}.png", bbox_inches="tight", dpi=300)