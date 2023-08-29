#join() Une os elementos de um iterável ao final da string
numeros = ["1, 2, 3, 4, 5"]

# Usando o método join() para unir os números da lista como uma string separada por vírgulas
numeros_como_string = ", ".join(map(str, numeros))

print(numeros_como_string)  # Saída: "1, 2, 3, 4, 5"