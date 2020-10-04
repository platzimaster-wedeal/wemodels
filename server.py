#Flask
from flask import Flask
from flask import jsonify

#We_deal
from models.graph import Graph, Vertex
from data_base.load import db, Users
from data_base.queries import get_persona

# Tools
import joblib
import numpy as np
#import urllib.parse
from decouple import config

server =  config('Server_name')
database = config('Data_base')
username =  config('User_name')
password = config('Password') 
cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

# Initializing app

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mssql+pymssql://{User_name}:{Password}@{Server_name}/{Data_base}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db.init_app(app)






# Routes
@app.route('/user', methods=['GET'])
def predict_user():
    Users.query.all()
    #user = Users.query.filter_by(id=2).first()
    #print(user)
    #model = joblib.load('./best_models/user_model_16.pkl')
    #X_test = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,4.3])
    #prediction = model.predict(X_test.reshape(1,-1))
    #return jsonify({'user_work_area' : users.id_work_area }) # users.id_work_area

@app.route('/job_offer', methods=['GET'])
def predict_job_offer():
    model = joblib.load('./best_models/job_offer_model_16.pkl')
    X_test = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0])
    prediction = model.predict(X_test.reshape(1,-1))
    return jsonify({'prediccion' : list(prediction)})

@app.route('/vertex', methods=['GET'])
def new_vertex(user):
    """ Create a new vertex. 
        Time complexity = O(2A)
        Space complexity = O(A+E)
        """
    V = Vertex(user,latitude, length)
    G = Graph()
    G.verteces.append(V) 
    V.search_neighbours() #O(V)
    update_graph(V) #O(V)
    print(f'New vertex of user {V.value} was created successful.')

@app.route('/location', methods=['GET'])
def localization_filter (user):
    """ Find  closer users based on his location. 
        O(V)+O(sorted)
       """
    G = Graph()
    for vertex in G.verteces:
        if user == vertex.value:
            nearest_neighbours= sorted(vertex.weights, key=lambda x: x[1])
        else:
            print(f'user {user} is not in graph yet, first you have to add it in graph.')
    return jsonify({'prediccion' : list(nearest_neighbours)}) 

if __name__ == "__main__":
    app.run(port=8080)
