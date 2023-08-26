class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
    
    def depositar(self, valor):
        valor = float(input("Digite o valor a depositar: "))
        self.saldo += valor
    
    def sacar(self, valor):
        valor = float(input("Digite o valor do saque: "))
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

conta = ContaBancaria("Clodoaldo", 0)
conta.depositar(500)
conta.sacar(100)
print("Olá senhor {} seu saldo atual é: R$ {:.2f}".format(conta.titular,conta.saldo))
