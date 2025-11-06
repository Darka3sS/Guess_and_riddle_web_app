from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from extentions import db
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__, template_folder="../Frontend/templates")
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    # Importa le routes dopo per evitare import circolari
    from . import routes

    # Registra i blueprints se ne hai
    # app.register_blueprint(...)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
