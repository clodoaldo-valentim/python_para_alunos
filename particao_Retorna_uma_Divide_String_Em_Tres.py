#partição() #Retorna uma tupla onde a string é dividida em três partes
frase = "Python é uma linguagem de programação"

# Usando o método partition() para dividir a frase em três partes com base no separador "é"
antes, separador, depois = frase.partition("é")

print("Antes:", antes)  # Saída: "Python "
print("Separador:", separador)  # Saída: "é"
print("Depois:", depois)  # Saída: " uma linguagem de programação"