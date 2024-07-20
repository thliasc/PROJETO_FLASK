class Genero:
    def __init__(self, titulo, preco, imagem):
        self.titulo = titulo
        self.preco = preco
        self.imagem = imagem
    

class Livros:
    def __init__(self, genero):
        self.genero = genero
        self.livros = []

    def adicionarLivro(self, livro):
        self.livros.append(livro)