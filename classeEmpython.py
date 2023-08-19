class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def emprestar(self):
        self.emprestado = True

    def devolver(self):
        self.emprestado = False

# Instanciando um objeto da classe Livro
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")

# Acesso aos atributos do objeto
print(livro1.titulo)  # Saída: O Senhor dos Anéis
print(livro1.autor)   # Saída: J.R.R. Tolkien
