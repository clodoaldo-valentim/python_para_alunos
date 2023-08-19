import math


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y == 0:
        return "Divisão por zero não é permitida."
    return x / y


def exponenciacao(x, y):
    return x ** y


def raiz_quadrada(x):
    if x < 0:
        return "Não é possível calcular a raiz quadrada de um número negativo."
    return math.sqrt(x)


print("Operações disponíveis:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
print("5. Exponenciação")
print("6. Raiz Quadrada")

escolha = input("Escolha uma operação (1/2/3/4/5/6): ")

if escolha in ('1', '2', '3', '4', '5', '6'):
    if escolha == '6':
        numero = float(input("Digite um número: "))
        print("Raiz quadrada:", raiz_quadrada(numero))
    else:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado:", adicao(num1, num2))
        elif escolha == '2':
            print("Resultado:", subtracao(num1, num2))
        elif escolha == '3':
            print("Resultado:", multiplicacao(num1, num2))
        elif escolha == '4':
            print("Resultado:", divisao(num1, num2))
        elif escolha == '5':
            print("Resultado:", exponenciacao(num1, num2))
else:
    print("Escolha inválida.")
