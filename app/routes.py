from flask import Blueprint, jsonify

main = Blueprint('main', __name__)

@main.route("/", methods=["GET"])
def index():
    return jsonify({"message": "PhishGuard backend is up and running!"})
