import re 
def verifica_senha(senha):
    
    if len(senha) < 8:
        return False
    if not re.search(r"[a-z]", senha):
        return False
    if not re.search(r"[A-Z]", senha):
        return False
    if not re.search(r"\d", senha):
        return False
    if not re.search(r"[@#$%^&+=]", senha):
        return False
    return True


senha = input("Crie uma senha: ")

if verifica_senha(senha):
    print("Senha válida!")
else:
    print("A senha não atende aos requisitos.")