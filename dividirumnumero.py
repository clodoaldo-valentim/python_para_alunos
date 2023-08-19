def verificar_numero_positivo():
    while True:
        numero = int(input("Digite um número inteiro positivo: "))
        if numero > 0:
            return numero
        else:
            print("Número não é positivo. Tente novamente.")

def calcular_soma_digitos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

numero = verificar_numero_positivo()
soma_digitos = calcular_soma_digitos(numero)

print(f"A soma dos dígitos de {numero} é {soma_digitos}")
