import requests #Importar a biblioteca requests para apis

#Exercício:
# 1) Faça uma função para extrair as informações de um dado CEP. (Teste com o seu CEP).

def consultar_cep(cep):

    url = f' https://viacep.com.br/ws/{cep}/json/'
    r = requests.get(url) #Vai pegar no dicionario requests as informações e armazenar na variavel r
    return(r.json())

print(consultar_cep('04016034'))

#2) Faça uma função para extrair o tipo e o id do pokémon na pokedex.

def typeid_pokemon(pokemon):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}/"
    r = requests.get(url)

    id = r.json()['id']
    type = r.json()['types'][0]['type']['name']
    return id, type

print(typeid_pokemon('ditto'))

#3) Faça uma função para extrair a quantidade de medalhas totais, ouro, para e bronze do país escolhido.

def medals(pais):
    url = f"https://apis.codante.io/olympic-games/countries"
    r = requests.get(url)
    dados = r.json()['data']
    for i in dados:
        if pais == i['name']:
            ouro = i['gold_medals']
            prata = i['silver_medals']
            bronze =i['bronze_medals']
            total = i['total_medals']
            return ouro, prata, bronze, total

print(medals("EUA"))

#4) Gere vários perfis com nome, email, telefone, cidade, estados, país


url= f'https://randomuser.me/api/'
r = requests.get(url)
dados = r.json()['results'][0]
primeironome = dados['name']['first']
segundonome =  dados['name']['last']
nome = primeironome + " " + segundonome
email = dados['email']
telefone = dados['phone']
cidade = dados['location']['city']
estado = dados['location']['state']
pais = dados['location']['country']

print(f"Nome: {nome}\n Endereço: {cidade}, {estado}, {pais}\n Telefone: {telefone}\n Email: {email}")