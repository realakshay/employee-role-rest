from db import db

class EmployeeModel(db.Model):
    __tablename__ = "employees"

    id=db.Column(db.Integer, primary_key=True)
    empid=db.Column(db.String(80), unique=True)
    name=db.Column(db.String(80))
    role_id=db.Column(db.Integer, db.ForeignKey('roles.id'))
    role=db.relationship('RoleModel')

    def __init__(self, empid, name, role_id):
        self.empid=empid
        self.name=name
        self.role_id=role_id

    def json(self):
        return {'empid':self.empid, 'name':self.name, 'role_id':self.role_id}

    def insert_in_db(self):
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def find_by_empid(cls,empid):
        return cls.query.filter_by(empid=empid).first()

    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
