#A compreensão de lista oferece uma sintaxe mais curta quando você deseja criar uma nova lista com base nos valores de uma lista existente.
frutas = ["maçã", "banana", "morango", "kiwi", "manga", "pêssego"]

novalista = [menosFrutas for menosFrutas in frutas if "i" in menosFrutas]

print(novalista)