#Exercício:

#1. Criação de um dicionário
#Crie um dicionário com três pares chave-valor. As chaves devem ser os nomes de três frutas e os valores,
#suas respectivas cores.

dict3 = {
    "Manga":"Amarela",
    "Morango":"Vermelho",
    "Uva":"Roxa"
}

#2. Acesso a um valor
#Usando o dicionário criado no exercício anterior, acesse e imprima a cor de uma das frutas.

print(dict3.get("Manga"))

#3. Adicionar um novo par chave-valor
#Adicione um novo par chave-valor ao dicionário, representando outra fruta e sua cor.

dict3["Limao"]="Verde"
print(dict3)
#4. Atualizar um valor
#Modifique a cor de uma das frutas no dicionário. Substitua o valor atual por uma nova cor.

dict3["Uva"]="Verde"
print(dict3)

#5. Remover um item
#Remova uma fruta do dicionário utilizando o metodo pop().

dict3.pop("Morango")
print(dict3)

#6. Iterar sobre as chaves
#Itere sobre o dicionário e imprima apenas as chaves (nomes das frutas).
for fruta in dict3.keys():
    print(f"Fruta:", fruta)

#7. Iterar sobre os valores
#Itere sobre o dicionário e imprima apenas os valores (cores das frutas).

for cor in dict3.values():
    print(f"Cor:", cor)

#8. Verificar a existência de uma chave
#Verifique se a fruta "banana" está presente no dicionário e imprima uma mensagem com base no resultado.

#print(dict3["Banana"] if "Banana" in dict3 else "Não existe")

a = dict3.get("Banana")

if a in dict3.keys():
    print(f"A: {a}")
else:
    print(f"Não existe")


#9. Combinar dois dicionários
#Crie um segundo dicionário com outras frutas e cores. Combine os dois dicionários em um só.

dicionario = {
    "Banana":"Amarela",
    "Goiaba": "Rosa",
    "Pera": "Verde"
}

dict3.update(dicionario)

print(dict3)

#10. Contar a quantidade de itens
#Usando o metodo adequado, imprima o número total de itens no dicionário (pares chave-valor)

print(len(dict3.keys())+ len(dict3.values()))

#Exercício: Escreva uma função que receba uma frase
#como parâmetro e retorne um dicionário, onde cada
#chave seja um caractere e seu valor seja o número de
#vezes que o caractere aparece na frase lida.

def carac(frase):
    contador = {} #contador é o que armazena cada uma das letras em um dicionario

    for letra in frase: #Na frase o index percorre as letras
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    return contador

print(carac("Banana é gostosa"))

#Escreva uma função que recebe uma lista de compras e
#um dicionário contendo o preço de cada produto disponível em uma
#determinada loja, e retorna o valor total dos itens da lista que estejam
#disponíveis nesta loja. Por exemplo, para os dados:

lista_de_compras = ['biscoito', 'chocolate', 'farinha']

supermercado = {
'amaciante':4.99,
'arroz':10.90,
'biscoito':1.69,
'cafe':6.98,
'chocolate':3.79,
'farinha':2.99
}

def soma(lista_de_compras):
    total = 0
    for item in lista_de_compras: #Pra cada item que estiver na lista de comrpas
        if item in supermercado: #Verifica se o item tem no supermercado
            total += supermercado[item] #Adiciona no carrinho e conta o valor do carrinho
    return total

print(soma(lista_de_compras))

