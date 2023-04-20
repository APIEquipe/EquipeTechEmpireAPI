from flask import Flask, render_template
app = Flask(__name__)


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

@app.route("/graficos")
def graficos():
    return render_template("graficos.html") 
