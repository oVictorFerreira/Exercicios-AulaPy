#Bubble sort - Organização de listas

#Tem-se um piscina cheia de bolhas, maior bolha vai ir pro topo primeiro e assim por diante -- NO CASO DA LISTA O MAIOR VAI IR PRO FINAL

lista = [84,41,50,7,2]

def bubbleSort(lista):
    for i in range(len(lista)):
        for j in range(len(lista) - 1 - i):
            if lista[j] > lista[j+1]:
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux

    return(lista)

print(bubbleSort(lista))