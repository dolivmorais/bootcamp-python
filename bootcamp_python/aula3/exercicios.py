### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.
# preco = float(input('Digite um valor? '))
# qtde = int(input('Digite um valor: '))

# if preco > 0 and qtde > 0:
#     print("Dados válidos")
# else:
#     print("Dados inválidos")


### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# # como 'Baixa', 'Normal' ou 'Alta'. Considerando que:
# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'
# TEMPERATURA = 20
# if TEMPERATURA < 18:
#     print('Baixa')
# elif TEMPERATURA <= 18:
#     print('Normal')
# else:
#     print('Alta')



### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.
# log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}
# if log['level'] == 'ERROR':
#     print(log['message'])

### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.
# idade = 25  # Exemplo de valor, substitua com input do usuário se necessário
# email = "usuario@exemplo.com"  # Exemplo de valor, substitua com input do usuário se necessário

# if not 18 <= idade <= 65:
#     print("Idade fora do intervalo permitido")
# elif "@" not in email or ".com" not in email:
#     print("Email inválido")
# else:
#     print("Dados de usuário válidos")

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.
# transacao = {'valor': 12000, 'hora': 20}

# if transacao['valor'] > 10000 or transacao['hora'] < 9 or transacao['hora'] > 18:
#     print("Transação suspeita")
# else:
#     print("Transação normal")

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.
# texto = "a a raposa marrom salta sobre o cachorro preguiçoso"
# palavras = texto.split()
# contagem_palavras = {}

# for palavra in palavras:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1

# print(contagem_palavras)

### Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.
# numeros = [10, 20, 30, 40, 50]
# minimo = min(numeros)
# maximo = max(numeros)
# normalizados = [(x - minimo) / (maximo - minimo) for x in numeros]

# print(normalizados)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando
# usuarios = [
#     {"nome": "Alice", "email": "alice@example.com"},
#     {"nome": "Bob", "email": ""},
#     {"nome": "Carol", "email": "carol@example.com"}
# ]

# usuarios_validos = [usuario for usuario in usuarios if not usuario["email"]]

# print(usuarios_validos)

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.
# numeros = range(1, 11)
# pares = [x for x in numeros if x % 2 == 0]

# print(pares)

### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.
# vendas = [
#     {"categoria": "eletrônicos", "valor": 1200},
#     {"categoria": "livros", "valor": 200},
#     {"categoria": "eletrônicos", "valor": 800}
# ]

# total_por_categoria = {}
# for venda in vendas:
#     categoria = venda["categoria"]
#     valor = venda["valor"]
#     if categoria in total_por_categoria:
#         total_por_categoria[categoria] += valor
#     else:
#         total_por_categoria[categoria] = valor

# print(total_por_categoria)

### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.
# dados = []
# entrada = "sair"
# while entrada.lower() != "sair":
#     entrada = input("Digite um valor (ou 'sair' para terminar): ")
#     if entrada.lower() != "sair":

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.
# numero = int(input("Digite um número entre 1 e 10: "))
# while numero < 1 or numero > 10:
#     print("Número fora do intervalo!")
#     numero = int(input("Por favor, digite um número entre 1 e 10: "))

# print("Número válido!")

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.
# pagina_atual = 1
# paginas_totais = 5  # Simulação, na prática, isso viria da API

# while pagina_atual <= paginas_totais:
#     print(f"Processando página {pagina_atual} de {paginas_totais}")
#     # Aqui iria o código para processar os dados da página
#     pagina_atual += 1

# print("Todas as páginas foram processadas.")

### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.
# tentativas_maximas = 5
# tentativa = 1

# while tentativa <= tentativas_maximas:
#     print(f"Tentativa {tentativa} de {tentativas_maximas}")
#     # Simulação de uma tentativa de conexão
#     # Aqui iria o código para tentar conectar
#     if True:  # Suponha que a conexão foi bem-sucedida
#         print("Conexão bem-sucedida!")
#         break
#     tentativa += 1
# else:
#     print("Falha ao conectar após várias tentativas.")

### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada
# itens = [1, 2, 3, "parar", 4, 5]

# i = 0
# while i < len(itens):
#     if itens[i] == "parar":
#         print("Parada encontrada, encerrando o processamento.")
#         break
#     # Processa o item
#     print(f"Processando item: {itens[i]}")
#     i += 1

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

