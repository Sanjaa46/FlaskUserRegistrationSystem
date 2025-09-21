from flask import Flask
from flask_jwt_extended import JWTManager
from models import db
from config import Config
from routes import init_routes

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
jwt = JWTManager(app)

init_routes(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
    # app.run(debug=True)
