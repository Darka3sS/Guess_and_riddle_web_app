from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from extentions import db
from config import Config


app = Flask(__name__, template_folder="../Frontend/templates")
app.config.from_object(Config)

db.init_app(app)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/AI_indovinello", methods=["GET"])
def get_AI_indovinello():
    return 1


# comando CLI personalizzato
@app.cli.command("init-db")
def init_db_command():
    """Crea le tabelle del database."""
    db.create_all()
    print("Database tables created.")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
