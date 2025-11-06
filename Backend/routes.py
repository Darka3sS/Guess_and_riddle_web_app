from flask import Blueprint, request, jsonify, render_template
from extentions import db
from models.partite_model import Partite
from google import genai
from utils import Livello

client = genai.Client()

main_routes = Blueprint("main", __name__)


@main_routes.route("/home", methods=["GET"])
def index():
    return render_template("index.html")


@main_routes.route("/api/AI_indovinello", methods=["GET"])
def get_AI_indovinello(req):
    data = request.get_json()
    livello = data.get("livello")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Genera un indovinello di livello {livello.value} in italiano.",
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    msg_indovinello = response.text
    return jsonify({"indovinello": msg_indovinello}), 200


@main_routes.route("/api/aiuto_indovinello", methods=["GET"])
def get_aiuto_indovinello(req):
    data = request.get_json()
    indovinello = data.get("indovinello")
    livello = data.get("livello")
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Fornisci un aiuto per risolvere questo indovinello di livello {livello.value}: {indovinello}",
        )
        msg_aiuto = response.text
        return jsonify({"aiuto": msg_aiuto}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# comando CLI personalizzato
@main_routes.cli.command("init-db")
def init_db_command():
    """Crea le tabelle del database."""
    db.create_all()
    print("Database tables created.")
