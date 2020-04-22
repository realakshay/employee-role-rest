from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.employee import Employee
from resources.role import Role
from resources.user import UserRegister

app=Flask(__name__)
app.secret_key="Akshay"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'
api=Api(app)
jwt=JWT(app, authenticate, identity)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(Employee, '/employee/<string:empid>')
api.add_resource(Role, '/role/<string:name>')
api.add_resource(UserRegister,'/user/<string:username>')

if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(debug=True)