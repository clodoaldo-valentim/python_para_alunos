class ContaBancaria:
    def __init__(self, saldo):
        self._saldo = saldo  # Atributo privado

    def get_saldo(self):
        return self._saldo  # Getter

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

# Criação de um objeto da classe ContaBancaria
conta = ContaBancaria(100)

# Acessando o saldo usando o getter
print(conta.get_saldo())  # Saída: 100

# Depositando dinheiro na conta
conta.depositar(50)
print(conta.get_saldo())  # Saída: 150
