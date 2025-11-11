from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from extentions import db
from flask_migrate import Migrate
from routes import main_routes
from flask_cors import CORS


def create_app():
    app = Flask(__name__, template_folder="../Frontend/templates")
    app.config.from_object(Config)

    db.init_app(app)
    migrate = Migrate(app, db)

    CORS(app)

    app.register_blueprint(main_routes)

    return app


app = create_app()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
