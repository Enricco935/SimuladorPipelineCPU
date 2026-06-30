import matplotlib.pyplot as plt

import csv

def salvar_tabela(dados, colunas, arquivo):
    with open(f"{arquivo}.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Cabeçalho
        writer.writerow(colunas)

        # Dados
        writer.writerows(dados)