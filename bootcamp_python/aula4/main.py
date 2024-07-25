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


