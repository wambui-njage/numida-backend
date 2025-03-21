import datetime

loans = [
    {"id": 1, "name": "Tom's Loan", "interest_rate": 5.0, "principal": 10000, "due_date": datetime.date(2025, 3, 1)},
    {"id": 2, "name": "Chris Wailaka", "interest_rate": 3.5, "principal": 500000, "due_date": datetime.date(2025, 3, 1)},
    {"id": 3, "name": "NP Mobile Money", "interest_rate": 4.5, "principal": 30000, "due_date": datetime.date(2025, 3, 1)},
    {"id": 4, "name": "Esther's Autoparts", "interest_rate": 1.5, "principal": 40000, "due_date": datetime.date(2025, 3, 1)},
]


loan_payments = [
    {"id": 1, "loan_id": 1, "payment_date": datetime.date(2025, 3, 4)},
    {"id": 2, "loan_id": 2, "payment_date": datetime.date(2025, 3, 15)},
    {"id": 3, "loan_id": 3, "payment_date": datetime.date(2025, 4, 5)},
]

def get_loans():
    """Retrieve all loans"""
    return loans

def get_loan_payments():
    """Retrieve all loan payments"""
    return loan_payments

def add_loan_payment(loan_id, payment_date):
    """Add a new payment to the list and return the new entry."""

    if isinstance(payment_date, str):
        payment_date = datetime.datetime.strptime(payment_date, "%Y-%m-%d").date()
    

    new_payment = {
        "id": len(loan_payments) + 1,
        "loan_id": loan_id,
        "payment_date": payment_date,  
    }
    
 
    loan_payments.append(new_payment)
    
    return new_payment
