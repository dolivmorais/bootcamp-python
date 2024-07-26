# typint, lista e dicionario

idade: int = 0
altura: float = 1.78
nome: str = "AAA"
is_estudande: bool = True

# lista
#%%
produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]
valores = [10.0, 15.5, 7.3, 22.8]

for i, item in enumerate(valores):
    print(f'{produtos[i]} {valores[i]}')
#%%
texto = 'texto@gmail.com'
novo_texto = texto.replace('o',"")
print(novo_texto)
#%%
produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]
valores = [10.0, 15.5, 7.3, 22.8]

produto = input('Informe o nome do produto: ')
if produto in produtos:
    i = produtos.index(produto)
    qtde = valores[i]
    print(produtos[i], qtde)
else:
    print('Não existe')
print(i)
#%%
produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]
valores = [10.0, 15.5, 7.3, 22.8]
maior = max(valores)
menor = min(valores)

i = valores.index(maior)

print(f'{produtos[i]} {valores[i]}')

#%%
produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]
novos_produtos = ["Produto X", "Produto Z"]

#produtos.extend(novos_produtos)
todos_produtos = produtos + novos_produtos

print(todos_produtos)
#%%
todos_produtos.sort(reverse=True)
print(todos_produtos)
# %%
#%%
## dicionario

produtos = {
    1: "Arroz",
    2: "Feijão",
    3: "Macarrão",
    4: "Azeite",
    5: "Sal",
    6: "Açúcar",
    7: "Café",
    8: "Leite",
    9: "Farinha",
    10: "Óleo"
}

valores_produtos = {
    "Arroz": 5.99,
    "Feijão": 4.49,
    "Macarrão": 3.29,
    "Azeite": 12.99,
    "Sal": 1.99,
    "Açúcar": 3.99,
    "Café": 8.49,
    "Leite": 4.19,
    "Farinha": 2.89,
    "Óleo": 7.49
}
#qtde_prod = valores_produtos['Açúcar']

if "Óleo" in valores_produtos:
    print(valores_produtos['Óleo'])
else:
    print('Item não existe')

if valores_produtos.get("frango"):
    print(valores_produtos['frango'])
else:
    print('Item não existe')

#%%
lucro_1tri = {
    "Janeiro": 15000,
    "Fevereiro": 12000,
    "Março": 18000
}

lucro_2tri = {
    "Abril": 20000,
    "Maio": 22000,
    "Junho": 25000
}


lucro_1tri.update(lucro_2tri)

print(lucro_1tri)

# %%
lucro_1tri
valor_total = 0

for chave in lucro_1tri:
    if lucro_1tri[chave] >= 20000:
        valor_total += lucro_1tri[chave]
        print(f'{chave} {lucro_1tri[chave]}')
print(f'total: {valor_total}')
# %%
media = 250

niveis_co2 = {
    "AC": [212, 215, 254, 255],
    "AL": [198, 202, 207, 210],
    "AM": [180, 185, 192, 200],
    "AP": [175, 178, 182, 190],
    "BA": [220, 225, 230, 240],
    "CE": [210, 215, 220, 230],
    "DF": [250, 255, 260, 270],
    "ES": [190, 195, 200, 210],
    "GO": [200, 205, 210, 220],
    "MA": [185, 190, 195, 200],
    "MT": [260, 265, 270, 280],
    "MS": [245, 250, 255, 265],
    "MG": [230, 235, 240, 250],
    "PA": [275, 280, 285, 295],
    "PB": [215, 220, 225, 235],
    "PR": [225, 230, 235, 245],
    "PE": [205, 210, 215, 225],
    "PI": [195, 200, 205, 215],
    "RJ": [240, 245, 250, 260],
    "RN": [210, 215, 220, 230],
    "RS": [235, 240, 245, 255],
    "RO": [255, 260, 265, 275],
    "RR": [175, 180, 185, 195],
    "SC": [245, 250, 255, 265],
    "SP": [270, 275, 280, 290],
    "SE": [200, 205, 210, 220],
    "TO": [185, 190, 195, 205]
}
print("Estados acima da média na emmisão de CO2")
for chave in niveis_co2:
    qtde_medicao =len(niveis_co2[chave])
    soma_co2 = sum(niveis_co2[chave])
    media_real = soma_co2 / qtde_medicao
    if media_real > media:
        print(f'{chave} {media_real}')
# %%
valores_produtos = {
    "Arroz": 5.99,
    "Feijão": 4.49,
    "Macarrão": 3.29,
    "Azeite": 12.99,
    "Sal": 1.99,
    "Açúcar": 3.99,
    "Café": 8.49,
    "Leite": 4.19,
    "Farinha": 2.89,
    "Óleo": 7.49
}

#itens_dic = valores_produtos.items()
for prod, qtd in valores_produtos.items():
    if qtd > 7:
        print(prod, qtd)
# %%
chaves = valores_produtos.keys()
valores = valores_produtos.values()

print(valores)
print(valores)

lista_chaves = list(chaves)
lista_chaves.sort()

for i in lista_chaves:
    print(i)
# %%

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
lista_de_numeros = [10.0, 15.5, 7.3, 22.8,-4564.45]

for i in range(len(lista_de_numeros)):
    for j in range(i +1, len(lista_de_numeros)):
        if lista_de_numeros[i] > lista_de_numeros[j]:
            lista_de_numeros[i], lista_de_numeros[j] = lista_de_numeros[j], lista_de_numeros[i]
print(lista_de_numeros)