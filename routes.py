from flask import request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import db, User

bcrypt = Bcrypt()

def init_routes(app):
    bcrypt.init_app(app)

    # Register endpoint
    @app.route("/register", methods=["POST"])
    def register():
        data = request.get_json()
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        if not username or not email or not password:
            return jsonify({"error": "All fields are required"}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({"error": "Email already registered"}), 400

        hashed_pw = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, email=email, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({"message": "User registered successfully!"}), 201

    # Login endpoint
    @app.route("/login", methods=["POST"])
    def login():
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password required"}), 400

        user = User.query.filter_by(email=email).first()
        if not user or not bcrypt.check_password_hash(user.password, password):
            return jsonify({"error": "Invalid credentials"}), 401

        token = create_access_token(identity=str(user.id))
        return jsonify({"message": "Login successful", "token": token}), 200

    # Protected endpoint
    @app.route("/profile", methods=["GET"])
    @jwt_required()
    def profile():
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })
    
    # Update password endpoint
    @app.route("/profile/password", methods=["PUT"])
    @jwt_required()
    def update_password():
        data = request.get_json()
        old_password = data.get("old_password")
        new_password = data.get("new_password")
        user_id = int(get_jwt_identity())
        user = User.query.get(user_id)

        if not old_password or not new_password:
            return jsonify({"error": "Old and new passwords are required"}), 400
        
        if not bcrypt.check_password_hash(user.password, old_password):
            return jsonify({"error": "Password did not match!"}), 401
        
        user.password = bcrypt.generate_password_hash(new_password).decode("utf-8")
        db.session.commit()

        return jsonify({"message": "Password updated successfully!"}), 200