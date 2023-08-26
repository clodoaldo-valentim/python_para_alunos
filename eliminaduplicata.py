numeros = [1, 2, 2, 3, 4, 4, 5]

# Criar uma nova lista para armazenar os elementos únicos
numeros_unicos = []

# Iterar sobre os elementos da lista original
for numero in numeros:
    # Verificar se o elemento já está na lista de elementos únicos
    if numero not in numeros_unicos:
        numeros_unicos.append(numero)

# Imprimir a lista de elementos únicos
print(numeros_unicos)
