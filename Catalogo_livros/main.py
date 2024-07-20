from flask import Flask, render_template, request, session
from classes import *

app = Flask(__name__)
app.secret_key = 'O34DKSDm2o10'
# Catálogo de Livros Online 
# - pesquisa de livros, postagem de livros, ver detalhes, adicionar comentarios ... [sistema de login]

genero_infantil = Livros("Literatura Infantil")

livro1 = Genero('O Pequeno Príncipe', 20, 'pequenoprincipe.jpg')
genero_infantil.adicionarLivro(livro1)

genero_romance = Livros("Literatura Romântica")

livro2 = Genero('Moby Dick', 75, 'mobydick.jpg')
genero_romance.adicionarLivro(livro2)
livro3 = Genero('O cortiço', 15, 'ocortico.jpg')
genero_romance.adicionarLivro(livro3)
livro4 = Genero('Bom Crioulo', 45, 'bomcrioulo.jpg')
genero_romance.adicionarLivro(livro4)


lista_livros = [genero_infantil, genero_romance]


@app.route("/")
def paginaInicial(): # home
    if "login" not in session:
        session["login"] = False
    
    
    return render_template("index.html", parLivros = lista_livros)


@app.route("/dashboard")
def dashboard(): # ver 
    #if not session["login"]: 
    #    return render_template('acessonegado.html')  
     
    return render_template("dashboard.html", parLivros = lista_livros)


@app.route("/escolha/<nome_genero>", methods=['GET', 'POST'])
def escolhaGenero(nome_genero):
    return render_template('editar_livros.html', parGenero = nome_genero)

@app.route("/adicionar", methods=['GET', 'POST'])
def addLivro():
    if request.files['imagem'] != '':
        imagem = request.files['imagem']
        imagem.save('static/images/' + imagem.filename)
    for gnr in lista_livros:
        if gnr.genero == request.form['genero']:
            for livro in gnr.livros:
                if livro.titulo == request.form['titulo']:
                    return render_template('msg.html', parMsg = "Este livro já foi cadastrado!")
            break
    gnr.adicionarLivro(Genero(request.form['titulo'], request.form['preco'], imagem.filename))
    return render_template('msg.html', parMsg = "Livro Adicionado")

@app.route("/logout")
def logout():
    session['login'] = False
    return render_template("logout.html")


if (__name__ == "__main__"):
    app.run(debug=True)