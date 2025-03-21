def categorize_payment(due_date, payment_date):
    if payment_date is None:
        return "Unpaid"
    delta = (payment_date - due_date).days
    if delta <= 5:
        return "On Time"
    elif 6 <= delta <= 30:
        return "Late"
    else:
        return "Defaulted"
