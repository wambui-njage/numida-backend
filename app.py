import datetime
from flask import Flask
from flask_graphql import GraphQLView
from flask_cors import CORS
from schema import schema
from routes import payments_bp,error_bp

def create_app():
    app = Flask(__name__)
    CORS(app)
    
    app.add_url_rule(
        "/graphql", view_func=GraphQLView.as_view("graphql", schema=schema, graphiql=True)
    )
    
    app.route("/")(lambda: "Welcome to the Loan Application API")

    app.register_blueprint(payments_bp, url_prefix="/payments")
    app.register_blueprint(error_bp) 
    
    return app

if __name__ == "__main__":
    create_app().run(host="0.0.0.0", port=2024, debug=True)
