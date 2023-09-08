# Dada a tupla original
tupla = (5, 2, 3, 5, 7, 5, 9, 5)

# Elemento específico a ser contado
elemento = 5

# Contando quantas vezes o elemento aparece na tupla
quantidade = tupla.count(elemento)

# Exibindo a quantidade de vezes que o elemento aparece
#f  indica que a string é uma f-string conveniente para criar strings com valores de variáveis inseridos
#{} são usadas para inserir valores de variáveis dentro da string.
print(f"O elemento {elemento} aparece {quantidade} vezes na tupla.")
