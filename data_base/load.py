from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    def __init__(self, id, first_name, last_name, email, date_of_birth, telephone, id_city, id_work_area, avatar, employee, employer, latitude, longitude, description):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.date_of_birth = date_of_birth
        self.telephone = telephone
        self.id_city = id_city
        self.id_work_area = id_work_area
        self.avatar = avatar
        self.employee = employee
        self.employer = employer
        self.latitude = latitude
        self.longitude = longitude
        self.description = description

    

    id = db.Column('id', db.Integer, primary_key=True, nullable=False)
    first_name = db.Column('first_name', db.String(40), nullable=False)
    last_name = db.Column('last_name', db.String(40), nullable=False)
    email = db.Column('email', db.String(254), nullable=False)
    date_of_birth = db.Column('date_of_birth', db.DateTime, nullable=False)
    telephone = db.Column('telephone', db.String(15), nullable=False)
    id_city = db.Column('id_city', db.Integer,db.ForeignKey('cities.id'), nullable=False)
    id_work_area = db.Column('id_work_area', db.Integer, db.ForeignKey('work_areas.id'), nullable=False)
    avatar = db.Column('avatar', db.Text, nullable=False)
    employee = db.Column('employee', db.Integer, nullable=False)
    employer = db.Column('employer', db.Integer, nullable=False)
    latitude = db.Column('latitude', db.Float, nullable=False)
    longitude = db.Column('longitude', db.Float, nullable=False)
    description = db.Column('descriptio', db.Text, nullable=False)


    
