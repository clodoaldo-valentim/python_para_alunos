# Dada a tupla original de números inteiros
tupla_original = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# Criando uma nova tupla contendo apenas os números pares
#tuple() converte a lista resultante em uma tupla
#numero: Isso é o que será incluído na nova sequência (ou seja, na nova tupla de números pares). É uma referência ao elemento atual da iteração.
tupla_pares = tuple(numero for numero in tupla_original if numero % 2 == 0)

# Exibindo a nova tupla de números pares
print(tupla_pares)
