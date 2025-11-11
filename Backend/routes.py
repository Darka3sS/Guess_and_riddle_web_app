from flask import Blueprint, request, jsonify, render_template
from extentions import db
from models.partite_model import partite
from google import genai
from utils import Livello
import os
from dotenv import load_dotenv

load_dotenv(".env")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=GEMINI_API_KEY)

main_routes = Blueprint("main", __name__)


@main_routes.route("/home", methods=["GET"])
def index():
    return jsonify(
        {
            "message": "Ciao! L'API del Backend è attiva e funzionante!",
            "status": "success",
        }
    )


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
