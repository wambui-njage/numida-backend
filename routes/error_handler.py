from flask import Blueprint, jsonify

error_bp = Blueprint("error_handler", __name__)

@error_bp.app_errorhandler(404)
def not_found(error):
    return jsonify({"error": "Resource not found"}), 404

@error_bp.app_errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

@error_bp.app_errorhandler(Exception)
def handle_exception(error):
    return jsonify({"error": str(error)}), 500
