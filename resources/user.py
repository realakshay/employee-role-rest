from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser= reqparse.RequestParser()
    parser.add_argument("username",
        type=str,
        required=True,
        help="Username necessory"
    )
    parser.add_argument("password",
        type=str,
        required=True,
        help="password necessory"
    )

    def post(self, username):
        data=UserRegister.parser.parse_args()
        user=UserModel.find_by_username(username)
        if user:
            return {"message":"username already taken"}
        else:
            user=UserModel(data['username'], data['password'])
            user.insert_user()
            return {"message":"Record Insert Successfully"}
