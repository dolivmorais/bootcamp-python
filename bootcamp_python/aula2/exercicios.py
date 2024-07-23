#Exercício 1: Soma de Dois Números Inteiros
num1 = 8  # Exemplo de entrada
num2 = 12  # Exemplo de entrada
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)

# Exercício 2: Resto da Divisão por 
# num = int(input("Digite um número: "))
num = 18  # Exemplo de entrada
resultado_resto = num % 5
print("O resto da divisão por 5 é:", resultado_resto)

# Exercício 3: Multiplicação de Dois Números
# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))
num1 = 5  # Exemplo de entrada
num2 = 7  # Exemplo de entrada
resultado_multiplicacao = num1 * num2
print("O resultado da multiplicação é:", resultado_multiplicacao)

# Exercício 4: Divisão Inteira do Primeiro pelo Segundo Número
# num1 = int(input("Digite o primeiro número inteiro: "))
# num2 = int(input("Digite o segundo número inteiro: "))
num1 = 20  # Exemplo de entrada
num2 = 3  # Exemplo de entrada
resultado_divisao_inteira = num1 // num2
print("O resultado da divisão inteira é:", resultado_divisao_inteira)

# Exercício 5: Quadrado de um Número
# num = int(input("Digite um número: "))
num = 6  # Exemplo de entrada
resultado_quadrado = num ** 2
print("O quadrado do número é:", resultado_quadrado)

# Exercício 6: Adição de Dois Números Flutuantes
# num1 = float(input("Digite o primeiro número flutuante: "))
# num2 = float(input("Digite o segundo número flutuante: "))
num1 = 2.5  # Exemplo de entrada
num2 = 4.5  # Exemplo de entrada
resultado_soma = num1 + num2
print("A soma é:", resultado_soma)

# Exercício 7: Média de Dois Números Flutuantes
# num1 = float(input("Digite o primeiro número flutuante: "))
# num2 = float(input("Digite o segundo número flutuante: "))
num1 = 3.5  # Exemplo de entrada
num2 = 7.5  # Exemplo de entrada
media = (num1 + num2) / 2
print("A média é:", media)

# Exercício 8: Potência de um Número
# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
base = 2.0  # Exemplo de entrada
expoente = 3.0  # Exemplo de entrada
potencia = base ** expoente
print("O resultado da potência é:", potencia)

# Exercício 9: Conversão de Celsius para Fahrenheit
# celsius = float(input("Digite a temperatura em Celsius: "))
celsius = 30.0  # Exemplo de entrada
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")

# Exercício 10: Área de um Círculo
# raio = float(input("Digite o raio do círculo: "))
raio = 5.0  # Exemplo de entrada
area = 3.14159 * raio ** 2
print("A área do círculo é:", area)


# Exercício 11: Converter String para Maiúsculas
# texto = input("Digite um texto: ")
texto = "Olá, mundo!"  # Exemplo de entrada
texto_maiusculas = texto.upper()
print("Texto em maiúsculas:", texto_maiusculas)

# Exercício 12: Imprimir Nome Completo em Minúsculas
# nome_completo = input("Digite seu nome completo: ")
nome_completo = "Fulano de Tal"  # Exemplo de entrada
nome_minusculas = nome_completo.lower()
print("Nome em minúsculas:", nome_minusculas)

# frase = input("Digite uma frase: ")
frase = "  Olá, mundo!  "  # Exemplo de entrada
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final:", frase_sem_espacos)

# Exercício 14: Separar Dia, Mês e Ano de uma Data
# data = input("Digite uma data no formato dd/mm/aaaa: ")
data = "01/01/2024"  # Exemplo de entrada
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)

# Exercício 15: Concatenar Duas Strings
# parte1 = input("Digite a primeira parte do texto: ")
# parte2 = input("Digite a segunda parte do texto: ")
parte1 = "Olá,"  # Exemplo de entrada
parte2 = " mundo!"  # Exemplo de entrada
texto_concatenado = parte1 + parte2
print("Texto concatenado:", texto_concatenado)

# Exercício 16. Operador and (E lógico)
# Exemplo de entrada
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

# Exercício 17. Operador or (OU lógico)
# Exemplo de entrada
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)

# Exercício 18. Operador not (NÃO lógico)
# Exemplo de entrada
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

# Exercício 19. Operador == (Igualdade)
# Exemplo de entrada
num1 = 5
num2 = 6
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)

# Exercício 20. Operador != (Diferença)
# Exemplo de entrada
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)

'''
Escreva um programa que converta a temperatura de Celsius para Fahrenheit. O programa deve solicitar ao usuário a temperatura em Celsius e, 
utilizando try-except, garantir que a entrada seja numérica, tratando qualquer ValueError. Imprima o resultado em Fahrenheit ou uma mensagem 
de erro se a entrada não for válida.
'''
# try:
#     celsius = float(input("Digite a temperatura em Celsius: "))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C é igual a {fahrenheit}°F.")
# except ValueError:
#     print("Por favor, digite um número válido para a temperatura.")
'''
Crie um programa que verifica se uma palavra ou frase é um palíndromo (lê-se igualmente de trás para frente, desconsiderando espaços e pontuações).
Utilize try-except para garantir que a entrada seja uma string. Dica: Utilize a função isinstance() para verificar o tipo da entrada.
'''
# entrada = input("Digite uma palavra ou frase: ")
# if isinstance(entrada, str):
#     formatado = entrada.replace(" ", "").lower()
#     if formatado == formatado[::-1]:
#         print("É um palíndromo.")
#     else:
#         print("Não é um palíndromo.")
# else:
#     print("Entrada inválida. Por favor, digite uma palavra ou frase.")

'''
Desenvolva uma calculadora simples que aceite duas entradas numéricas e um operador (+, -, *, /) do usuário. Use try-except para lidar com divisões 
por zero e entradas não numéricas. Utilize if-elif-else para realizar a operação matemática baseada no operador fornecido. Imprima o resultado ou 
uma mensagem de erro apropriada.
'''
# n1 = float(input("Digite o primeiro número: "))
# n2 = float(input("Digite o segundo número: "))
# op = input("Digite a operação (+, -, *, /): ")
# try:
#     if op == "+":
#         print(n1 + n2)
#     elif op == "-":
#         print(n1 - n2)
#     elif op == "*":
#         print(n1 * n2)
#     elif op == "/" and n2 != 0:
#         print(n1 / n2)
#     else:
#         print("Operação inválida.")
# except ZeroDivisionError:
#     print("Não pode dividir por zero.")
# except ValueError:
#     print("Entrada inválida. Por favor, digite um número.")
'''
Escreva um programa que solicite ao usuário para digitar um número. Utilize try-except para assegurar que a entrada seja numérica e utilize 
if-elif-else para classificar o número como "positivo", "negativo" ou "zero". Adicionalmente, identifique se o número 
é "par" ou "ímpar"
'''
# try:
#     numero = int(input("Digite um número: "))
#     if numero > 0:
#         print("Positivo")
#     elif numero < 0:
#         print("Negativo")
#     else:
#         print("Zero")
#     if numero % 2 == 0:
#         print("Par")
#     else:
#         print("Ímpar")
# except ValueError:
#     print("Por favor, digite um número inteiro válido.")

'''
Crie um script que solicite ao usuário uma lista de números separados por vírgula. O programa deve converter a string de entrada em uma lista de 
números inteiros. Utilize try-except para tratar a conversão de cada número e validar que cada elemento da lista convertida é um inteiro. 
Se a conversão falhar ou um elemento não for um inteiro, imprima uma mensagem de erro. Se a conversão for bem-sucedida para todos os elementos, 
imprima a lista de inteiros.
'''
entrada_lista = input("Digite uma lista de números separados por vírgula: ")
numeros_str = entrada_lista.split(",")
numeros_int = []
try:
    for num in numeros_str:
        numeros_int.append(int(num.strip()))
    print("Lista de inteiros:", numeros_int)
except ValueError:
    print("Erro: certifique-se de que todos os elementos são números inteiros válidos.")