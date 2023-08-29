#casefold() Converte string em minúsculas
#Neste exemplo, os três textos "Maçã", "maçã" e "MACA" foram convertidos para minúsculas e tratados para a comparação usando o método casefold(). Isso torna as comparações de strings insensíveis a maiúsculas/minúsculas e tratamento de caracteres acentuados.
texto1 = "Maçã"
texto2 = "maçã"
texto3 = "MACA"

resultado1 = texto1.casefold()
resultado2 = texto2.casefold()
resultado3 = texto3.casefold()
print(resultado1 == resultado2)  # Saída: True
print(resultado1 == resultado3)  # Saída: True