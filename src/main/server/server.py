from flask import Flask
from flask_cors import CORS
from src.models.settings.connection import db_connetction_handler
from src.main.routes.events_routes import event_route_bp

db_connetction_handler.connect_to_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_route_bp)
