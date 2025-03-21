from flask import Blueprint, request, jsonify
from database import add_loan_payment
from datetime import datetime

payments_bp = Blueprint("payments", __name__) 

@payments_bp.route("/add-payment", methods=["POST"])
def add_payment():
    """Handles adding a new loan payment."""
    data = request.get_json()
    loan_id = data.get("loan_id")

    if not loan_id:
        return jsonify({"error": "loan_id is required"}), 400
    payment_date = datetime.utcnow().date()
    new_payment = add_loan_payment(loan_id,payment_date)
    return jsonify(new_payment), 201
