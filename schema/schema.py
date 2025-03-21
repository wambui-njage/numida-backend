import graphene
from models import Loan
from database import get_loans, get_loan_payments
from utils import categorize_payment

class Query(graphene.ObjectType):
    loans = graphene.List(Loan)

    def resolve_loans(self, info):
        loans = get_loans()
        payments = get_loan_payments()

        return [
            Loan(
                id=loan["id"],
                name=loan["name"],
                interest_rate=loan["interest_rate"],
                principal=loan["principal"],
                dueDate=loan["due_date"].strftime("%Y-%m-%d"),
                paymentDate=next(
                    (p["payment_date"].strftime("%Y-%m-%d") for p in payments if p["loan_id"] == loan["id"]), None
                ),
                status=next(
                    (categorize_payment(loan["due_date"], p["payment_date"]) for p in payments if p["loan_id"] == loan["id"]),
                    "Unpaid",
                ),
            )
            for loan in loans
        ]

schema = graphene.Schema(query=Query)
