from flask import *
from flask import Flask, render_template, request, redirect, url_for, flash
from bancodados import *
from flask_sqlalchemy import SQLAlchemy

import bancodados as bd

app = Flask(__name__)
app.secret_key = 'passwords'
#criar página
#pagina contem route = são os caminhos que definem qual link abre qual pagina
#  função = o que voce quer exebir naquela pagina
#decorator é uma linha de codigo que atribui uma função que vem logo abaixo dela

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///orcamentos.sqlite3"
app.config['SECRET_KEY'] = "random string" #NECESSARIO PRO FLASH FUNCIONAR

db = SQLAlchemy(app)

class orcamentos(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        nome = db.Column(db.String(50))
        celular = db.Column(db.String(12))
        data = db.Column(db.String(10))
        hora = db.Column(db.String(6))
        descricao = db.Column(db.String(150))

        def __init__(self,nome,celular,data,hora,descricao):
            self.nome = nome
            self.celular = celular
            self.data = data
            self.hora = hora
            self.descricao = descricao


@app.route('/', methods=["GET","POST"]) # abre na pagina principal
def base(): # função da homepage
    return render_template("login.html")

# rota de orçamentos
@app.route('/orcamentos') # SELECT- LISTA A TABELA Orçamentos
def lista_orcamentos():
	return render_template("orcamentos.html", orcamentos=orcamentos.query.all())
# cria o orçamento
@app.route('/cria_orcamento', methods=["GET", "POST"]) ## CREATE- INSERE DADOS NO BANCO DE DADOS SQL
def cria_orcamento(): 
        nome = request.form.get('nome')
        celular = request.form.get('celular')
        data = request.form.get('data')
        hora = request.form.get('hora')
        descricao = request.form.get('descricao')

        if request.method == 'POST':
            if not nome or not descricao or not data or not hora or not descricao:
                flash('Preencha todos os campos de forma correta',"error")
            else:
                orcamento = orcamentos(nome, celular, data, hora ,descricao)
                db.session.add(orcamento)
                db.session.commit()
                return redirect(url_for('lista_orcamentos'))
        return render_template("novo_orcamento.html")

# #atualiza orcamento
# @app.route('/<int:id>/atualiza_orcamento', methods=["GET", "POST"])
# def atualiza_orcamento(id):
#     orcamento = orcamentos.query.filter_by(id=id).first()
#     if request.method == 'POST':
#         nome = request.form["nome"]
#         celular = request.form["celular"]
#         data = request.form["data"]
#         hora = request.form["hora"]
#         descricao = request.form["descricao"]
#         orcamentos.query.filter_by(id=id).update({"nome":nome, "celular":celular, "data":data, "hora":hora,"descricao":descricao})
#         db.session.commit()
#         return redirect(url_for('lista_orcamento'))
#     return render_template ("atualiza_orcamento.html", orcamento=orcamento)

#remove orcamento
@app.route('/<int:id>/remove_orcamento') 
def remove_orcamento(id):
        orcamento = orcamentos.query.filter_by(id=id).first()
        db.session.delete(orcamento)
        db.session.commit()
        return redirect(url_for('lista_orcamentos'))

#rota homepage----------------------------------------------------------------------------
@app.route('/homepage', methods=["GET","POST"])
def homepage():
    return render_template("homepage.html")

#rota login------------------------------------------------
@app.route('/login', methods=["GET","POST"])
def login():
    return render_template("login.html")

#rota registrar usuarios------------------------------------------------
@app.route('/registra', methods=["GET","POST"])
def registra():
    return render_template("registra.html")
#rota administrador
@app.route('/administrador', methods = ["GET","POST"])
def administrador():
    return render_template("administrador.html", orcamentos=orcamentos.query.all())

#rota contato
@app.route('/contato', methods=["GET","POST"])
def contato():
    return render_template("contato.html")

#rota esqueceu a senha
@app.route('/esquece_senha', methods= ["GET","POST"])
def esquece_senha():
    return render_template("esqsenha.html")

#rota renovar a senha
@app.route('/novasenha', methods= ["GET","POST"])
def novasenha():
    return render_template("novasenha.html")


#condições da navbar--------------------------------------------
@app.route('/cardapio/<opcoes>')
def cardapio(opcoes):
    if opcoes == 'docinhos':
        return render_template("docinhos.html")
    elif opcoes == 'bolo_aniversario':
        return render_template("bolo_aniversario.html")
    elif opcoes == 'bolo_casamento':
        return render_template("bolo_casamento.html")
    elif opcoes == 'salgados':
        return render_template("salgados.html")
    return render_template("base.html")

#cadastrar o usuario
@app.route('/cadastra_usuario', methods = ["POST"])
def cadastrar():
    nome_user = request.form['nome']
    email = request.form['email']
    celular = request.form['celular']
    cpf = request.form['cpf']
    rua = request.form['rua']
    bairro = request.form['bairro']
    numero = request.form['numero']
    cidade = request.form['cidade']
    uf = request.form['uf']
    cep = request.form['cep']
    senha = request.form['senha']
    senha_verificada = request.form['senha_veri']

    if senha == senha_verificada:
        insere_usuario(nome_user, email, celular, cpf, rua, bairro, numero, cidade, uf, cep, senha)
        return redirect('/')
    else:
        return render_template('registra.html', mensagem = 'Senha Inválida')


#cadastrar o adm



if __name__ == "__main__":
#o Ifroda quando o arquivo app.py, seja importado diretamente por ele
    app.run(debug=True)#coloca o site no ar
# todas as edições feitas no codigo aparecem no site, quando se usa debug=True
#@app.route("/usuarios/<nome_usuario>") #retorna o nome do usuario colocado na barra de pesquisa ex:http://127.0.0.1:5000/usuarios/anajulia   
#def usuarios(nome_usuario):
 #   return render_template("usuarios.html", nome_usuario=nome_usuario)

