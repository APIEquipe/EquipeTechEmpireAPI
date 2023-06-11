from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__)

#Conexão com banco de dados
app.config['MYSQL_HOST'] = 'localhost'
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


