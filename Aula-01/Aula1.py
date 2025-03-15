#Módulos
#todos arquivos .py são um modulo
# import * chama todas as funções do outro arquivo .py

from calculadora import *
from multdiv import *
while True:
    op = input("Selecione se deseja somar(+), subtrair(-), multiplicar(*), dividir(/) ou sair: ")
    if op == "+":
        a = int(input("Digite um valor: "))
        b = int(input("Digite outro valor :"))
        adc(a,b)

    elif op == "-":
        a = int(input("Digite um valor: "))
        b = int(input("Digite outro valor :"))
        sub(a, b)

    elif op == "*":
        a = int(input("Digite um valor: "))
        b = int(input("Digite outro valor: "))
        mult(a, b)

    elif op == "/":
        a = int(input("Digite um valor: "))
        b = int(input("Digite outro valor: "))
        div(a, b)

    elif op == "sair":
        break

    else:
        print("Operação inválida")
