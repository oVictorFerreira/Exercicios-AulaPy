#Crie uma matriz que pergunta os elementos e a quantidade de linhas pro usuário
matriz = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c]= input(f"Digite o elemento que deseja adicionar na posição [{l}, {c}]: ")
print('-='*30)

for l in range(0, 3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]', end=" ")
    print()

#Soma dos valores pares

soma = 0
for l in range(len(matriz)):
    for c in range(len(matriz)):
        if c % 2 == 0:
            soma += c

print(soma)

print()

soma3 = 0

for l in range(len(matriz)):
    soma3 = soma3 + matriz[l][2]

print(soma3)

