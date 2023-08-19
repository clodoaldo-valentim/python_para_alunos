print("Olá mundo!!")
idade = 50
nome = "Clodoaldo"
nota1 = 6
nota2 = 6
nota3 = 6
nota4 = 6
media = (nota1 + nota2 + nota3 + nota4) / 4
if media >= 7:
    print("Você passou")
elif media>=6:
    print("Você está em recuperação")
else:
    print("Você foi reprovado")
print("Sua idade é " + str(idade) +" anos"+ " e a média das notas é " + str(media))
