#Exercício 1: Crie uma função que recebe várias strings e as junta em uma única string separada por espaço.

#Funções que recebem um número indeterminado de parâmetro
def juntastring(*frase): #* é para representar todos os elementos da variavel frase
    texto = ''
    for i in range(len(frase)): # Percorre os índices dos elementos em 'frase'
        if i < len(frase)-1: # Se o índice for menor que o último índice..
            texto = texto + frase[i] + ' ' #Adiciona a string + um espaço
        else: # Se for o último elemento...
            texto = texto + frase[i] #adiciona a ultima string sem espaço
    return texto #Return deve estar na identação fora do for para passar todos os elementos.

x = juntastring('1','2','3','4','5','56')
print(x)

#Exercício: Crie uma função chamada média que aceita um número variável de argumentos e retorna a média.

def media(*valores):
    calculo = 0
    for i in valores:
        calculo = i + calculo
        media = calculo / len(valores)
    return media

print(media(10,2))

# Exercício: Crie um programa que simule um banco, usando variáveis globais saldo e transacoes. Implemente as funções
# depositar(valor), sacar(valor) e extrato()

saldo = 0
transferencia = []

def depositar(valor):
    global saldo
    global extrato

    saldo += valor
    transferencia.append(valor)

def sacar(valor):
    global saldo
    global extrato

    saldo -= valor
    transferencia.append(-valor)

def extratob():
    print(f'O seu extrato bancáro é:')
    for i in transferencia:
        print(f'{i}', end='\n')

while True:
    op = input("Selecione se deseja Depositar (D), Sacar (S), visualizar o extrato (E) ou sair (0): ")

    if op == 'D' or op == 'd':
        valor = int(input('Digite o valor que será depositado: '))
        depositar(valor)
        print(f"O valor depositado foi de R$ {valor:.2f}")
        print(f'O novo valor em conta é de R$ {saldo:.2f}')

    elif op == 'S' or op == 's':
        valor = int(input('Digite o valor que será sacado: '))
        sacar(valor)
        print(f"O valor sacado foi de R$ {valor:.2f}")
        print(f'O novo valor em conta é de R$ {saldo:.2f}')

    elif op == 'E' or op == 'e':
        print(extratob())
        print(f"Saldo disponível em R$ {saldo:.2f}")

    elif op == "0":
        print("Obrigado por utilizar o FIAPBANK")
        break
    else:
        print("Operação inválida")

#Exercício - Crie um programa que usa uma variável global para armazenar um carrinho de compras. Implemente as funções:
#adicionar_produto(produto), remover_produto(produto), e ver_carrinho().

carrinho = []

def adicionar(item):
    global carrinho
    carrinho.append(item)
    return f"O item adicionado foi: {item}"


def retirar(item):
    global carrinho
    if item in carrinho:
        indice = carrinho.index(item)  # Encontra o índice do item
        carrinho.pop(indice)  # Remove pelo índice
        print(f"O item '{item}' foi removido do carrinho.")
    else:
        print(f"O item '{item}' não está no carrinho.")

while True:
    op = input("Selecione se deseja Adicionar (A), Retirar (R), Visualizar o carrinho  (V) ou sair (0): ")

    if op == 'A' or op == 'a':
        item = input('Item a ser adicionado: ')
        adicionar(item)
        print(f"O item adicionado foi: {item}")

    elif op == 'R' or op == 'r':
        indice = int(input('Qual será o item a ser retirado digide o numero dele na ordem do carinho: '))
        retirar(indice)

    elif op == 'V' or op == 'v':
        print(carrinho)
        print(f"Seu carrinho atualmente possui: {len(carrinho)}")

    elif op == "0":
        print("Obrigado por utilizar o Fiapee")
        break
    else:
        print("Operação inválida")