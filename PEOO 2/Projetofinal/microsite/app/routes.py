from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    dicionario={
        'nome':"Anderson",
        'titulo':"Titulo do bom"
    }
    return render_template("index.html", **dicionario)