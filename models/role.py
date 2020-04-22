from db import db

class RoleModel(db.Model):
    __tablename__='roles'

    id=db.Column(db.Integer, primary_key=True)
    role=db.Column(db.String(80), unique=True)

    employees=db.relationship('EmployeeModel', lazy='dynamic')

    def __init__(self, role):
        self.role=role

    def json(self):
        return {'role':self.role, 'employees':[employee.json() for employee in self.employees.all()]}
    
    @classmethod
    def find_by_role_name(cls, rolename):
        return cls.query.filter_by(role=rolename).first()

    def insert_role(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_role(self):
        db.session.delete(self)
        db.session.commit()
    

