#%%
import csv

caminho_arquivo = r"C:\Users\Diego\Documents\Workspace\bootcamp-python\bootcamp_python\aula4\arquivo.csv"
arquivo_csv = []

with open(file=caminho_arquivo, mode= "r", encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for i in leitor_csv:
        arquivo_csv.append(i)

print(arquivo_csv)
#%%