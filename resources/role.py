from flask_restful import Resource, reqparse
from models.role import RoleModel
from flask_jwt import jwt_required

class Role(Resource):
    parser=reqparse.RequestParser()
    parser.add_argument("name",
        type=str,
        required=True,
        help="name should be there"
    )

    @jwt_required()
    def get(self, name):
        role=RoleModel.find_by_role_name(name)
        if role:
            return role.json()
        return {"message":"Designation not found"},404
    
    def post(self, name):
        role=RoleModel.find_by_role_name(name)
        if role:
            return {"message":"Designation already there"}
        else:
            role=RoleModel(name)
            role.insert_role()
            return {"message":"Designation inserted successfully"}, 201

    @jwt_required()
    def delete(self, name):
        role=RoleModel.find_by_role_name(name)
        if role:
            role.delete_role()
            return {"message":"Designation deleted success"}, 201
        return {"message":"Designation not found"},404