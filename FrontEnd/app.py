from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

#Conexão com banco de dados
app.config['MYSQL_HOST'] = 'localhost' #127.0.0.1
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'Api'

mysql = MySQL(app)


@app.route('/')
def home(): 
    return render_template("index.html")

@app.route("/consultar")
def consultar():
    return render_template("consultar.html")

@app.route("/gastos")
def gastos():
    return render_template("gastos.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/info")
def info():
    return render_template("covid.html")

@app.route("/graficos")
def graficos():
    return render_template("graficos.html") 

@app.route("/graficosgastos")
def graficosgastos():
    return render_template("graficosgastos.html") 

 @app.route('/sugestao', methods=["GET", "POST"])
def cadastro():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['sugestao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contatos(email, assunto, descricao) values (%s, %s, %s)", (email, assunto, sugestao))

        mysql.connection.commit()

        cur.close()

        return render_template("sucesso.html")
    return render_template("sugestao.html")
