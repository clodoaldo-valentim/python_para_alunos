def verifica_senha(senha):
    if len(senha) < 8:
        return False
    
    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False
    
    caracteres_especiais = "@#$%^&+="

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        if caractere.islower():
            tem_minuscula = True
        if caractere.isdigit():
            tem_numero = True
        if caractere in caracteres_especiais:
            tem_especial = True
    
    return tem_maiuscula and tem_minuscula and tem_numero and tem_especial

senha = input("Crie uma senha: ")

if verifica_senha(senha):
    print("Senha válida!")
else:
    print("A senha não atende aos requisitos.")