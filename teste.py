# IF ELIF ELSE

# meta = 50000
# qtde_vendida = 400

# if qtde_vendida > meta:
#     print(f'Batemos a meta de vendas! Vendemos {qtde_vendida} produtos')
# else:
#     print(f'Não batemos a meta de vendas! Vendemos {qtde_vendida} produtos a meta é de {meta} ficamos {meta - qtde_vendida} abaixo')
# print('Fim da analise!')
##################################

# meta = 0.05
# taxa = 0
# rendiemnto = 0.10

# if rendiemnto > meta:
#     if rendiemnto > 0.20:
#         taxa = 0.04
#         print(f'A taxa de {taxa}')
#     else:
#         taxa = 0.02
#         print(f'A taxa de {taxa}')
# else:
#     taxa = 0
#     print(f'A taxa doi de {taxa}')
#######################################

# meta = 20000
# venda = 40000
# bonus = 0

# if venda >= meta * 2:
#         bonus = 0.07
#         valor_bonus = venda * bonus
#         venda_com_bonus = venda + valor_bonus
#         print(f'Parabens, você vendeu 2x mais que a meta! Venda {venda}, bonus {bonus * venda} Venda + bonus {venda_com_bonus}')
# elif venda >= meta:
#         bonus = 0.03
#         valor_bonus = venda * bonus
#         venda_com_bonus = venda + valor_bonus
#         print(f'Parabens, você atingiu a meta! Venda {venda}, bonus {bonus * venda} Venda + bonus {venda_com_bonus}')
# else:
#     print(f'não ganha bonus')
# print('FIM')
#############################

# produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]
# producao = [10, 15, 7, 22]

# for i in range(len(producao)):
#     print(f'{produtos[i]} - {producao[i]}')

# produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]


# for i in range(len(produtos)):
#     print(f'{i, produtos[i]}')

# for i in produtos:
#     print(i)
###################
# meta=  80
# producao = [10, 15, 7, 22,12,90,80,100]
# c = 0

# for i in producao:
#     if i > meta:
#         c += 1

# qtde_func = len(producao)
# result = c / qtde_func

# print(c)
# print(qtde_func)
# print(result)
####################
# produtos = ["Produto A", "Produto B", "Produto C", "Produto D"]
# producao = [10, 15, 7, 22]
# minimo = 12

# for i,qtde in enumerate(producao):
#     if qtde < minimo:
#         print(producao[i],produtos[i])
################
# qtde_pessoas = int(input('Quantas pessoas? '))
# list_quarto = []
# for i in range(qtde_pessoas):
#     nome = input('Informe seu nome:')
#     cpf = input('Informe seu CPF: ')
#     list_quarto.append((nome, cpf))
# print(list_quarto)
####################################
# Lista de vendedores e suas vendas
meta = 1100
lista = []
vendedores = [
    ["Vendedor 1", 1200.50],
    ["Vendedor 2", 850.00],
    ["Vendedor 3", 950.75],
    ["Vendedor 4", 1300.20],
    ["Vendedor 5", 1120.40],
    ["Vendedor 6", 780.90]
]

for vendedor in vendedores:
    if vendedor[1] >= meta:
        lista.append(vendedor)

for vendedor in lista:
    print(f"Vendedor: {vendedor[0]}, Vendas: R$ {vendedor[1]:.2f}")

