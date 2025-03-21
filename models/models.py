import graphene

class Loan(graphene.ObjectType):
    id = graphene.Int()
    name = graphene.String()
    interest_rate = graphene.Float()
    principal = graphene.Int()
    dueDate = graphene.String()
    paymentDate = graphene.String()
    status = graphene.String()
