from flask import request, jsonify, render_template
from extentions import db
from models.partite_model import Partite
from . import app


@app.route("/home", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/api/AI_indovinello", methods=["GET"])
def get_AI_indovinello(req):
    data = request.get_json()  # request per le ggere richieste dal frontend
    domanda = data.get("domanda")
    livello = data.get("livello")


# comando CLI personalizzato
@app.cli.command("init-db")
def init_db_command():
    """Crea le tabelle del database."""
    db.create_all()
    print("Database tables created.")
