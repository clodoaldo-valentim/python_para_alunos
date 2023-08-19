import matplotlib.pyplot as plt

# Cria um conjunto de dados
notas = [8, 9, 10, 7, 6]
assuntos = ["Matemática", "Português", "História", "Geografia", "Ciências"]

# Cria o gráfico de barras
plt.plot(assuntos, notas)

# Adiciona títulos e rótulos aos eixos
plt.title("Notas do aluno")
plt.xlabel("Assuntos")
plt.ylabel("Notas")
# Exibe o gráfico
plt.show()



