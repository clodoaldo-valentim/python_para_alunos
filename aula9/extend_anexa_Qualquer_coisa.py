#O extend()método não precisa anexar listas , você pode adicionar qualquer objeto iterável (tuplas, conjuntos, dicionários etc.).
alista = ["apple", "banana", "cherry"]
atupla = ("kiwi", "orange")
alista.extend(atupla)
print(alista)