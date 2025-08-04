import mysql.connector as mc

bd = mc.connect(
    host = "localhost",
    user = "root",
    password = "admin", 
    database = "bdbuffet"
)
#INSERIR OS DADOS DO USUARIO NO BD
def insere_usuario(nome, email, celular,cpf, rua, bairro, numero, cidade, uf, cep, senha):
    if bd.is_connected():
        comando = 'insert into usuario(nome, email, cpf, celular, rua, bairro, numero, cidade, uf, cep, senha) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'#valores q nao sabemos
        cursor = bd.cursor()
        valores = (nome, email, celular, cpf,rua, bairro, numero, cidade, uf, cep, senha)# os trem do bd
        cursor.execute(comando,valores)
        bd.commit()

#INSERIR OS DADOS DO ADM NO BD
def insere_admin(nome, email, celular, senha):
    if bd.is_connected():
        comando = 'insert into admin(nome_adm, email_adm, celular_adm, senha_adm) values(%s, %s, %s, %s)'
        cursor = bd.cursor()
        valores = (nome, email, celular, senha)
        cursor.execute(comando,valores)
        bd.commit()
#ENTRAR COM O USUARIO NA PAGINA
def verifica_loginUser(email,senha):
    if bd.is_connected():
        consulta = 'select email,senha from usuario where email = %s and senha = %s'
        valores = (email, senha)
        cursor = bd.cursor()
        cursor.execute(consulta, valores)
        return cursor.fetchall()
    
#ENTRAR COM O ADM NA PAGINA   
def verifica_loginAdm(email,senha):
    if  bd.is_connected():
        consulta = 'select email_adm, senha_adm from adm where email_adm = %s and senha_adm = %s'
        valores = (email, senha)
        cursor = bd.cursor()
        cursor.execute(consulta, valores)
        return cursor.fetchall()
    
def dados_cliente():
    if  bd.is_connected():
        consulta = "select * from usuarios order by nome"
        cursor = bd.cursor()
        cursor.execute(consulta)
        return cursor.fetchall()
        
    
#COLETA OS ID    
def coleta_id(email):
    consulta = "select id from usuarios where email = %s"
    valores = email
    cursor = bd.cursor()
    cursor.execute(consulta, valores)
    try:
        id_user = cursor.fetchone()         
    #  return (id_user[0])
    except:
        pass
    
#INSERIR OS PRODUTOS NO BD
def insere_produtos(nome, preco, qtde):
    if bd.is_connected():
        comando = 'insert into admin(nome, preco, qtde) values(%s, %s, %s)'
        cursor = bd.cursor()
        valores = (nome, preco, qtde)
        cursor.execute(comando,valores)
        bd.commit()
