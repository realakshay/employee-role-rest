from flask_restful import Resource, reqparse
from models.employee import EmployeeModel
from flask_jwt import jwt_required

class Employee(Resource):

    parser=reqparse.RequestParser()
    parser.add_argument("empid",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument("name",
        type=str,
        required=True,
        help="This field cannot be blank"
    )
    parser.add_argument("role_id",
        type=int,
        required=True,
        help="This field cannot be blank"
    )

    @jwt_required()
    def get(self, empid):
        employee=EmployeeModel.find_by_empid(empid)
        if employee:
            return employee.json()
    
        return {"message":"Record Not Found"},404

    def post(self, empid):
        data=Employee.parser.parse_args()
        employee=EmployeeModel.find_by_empid(empid)
        if employee:
            return {"message":"Record Already Exist"},201
        else:
            employee=EmployeeModel(empid, data['name'], data['role_id'])
            employee.insert_in_db()
            return employee.json(), 201

    def put(self, empid):
        data=Employee.parser.parse_args()
        employee=EmployeeModel.find_by_empid(empid)
        if employee is None:
            return {"message":"Record Not Found For This Record"},404
        else:
            employee.name=data['name']
            employee.role_id=data['role_id']
            employee.insert_in_db()
            return employee.json(), 201

    def delete(self, empid):
        employee=EmployeeModel.find_by_empid(empid)
        if employee:
            employee.delete_from_db()

        return {"message":"Employee Deleted"},201
