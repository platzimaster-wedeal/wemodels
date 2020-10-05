"""This is the main  file that control all aplication internal  flow"""
#Flask
from flask import Flask, make_response, jsonify
from configuration import Configuration
#We_deal
from models.graph import Graph, Vertex
from queries.queries import Get_work_area, Get_user_qualification, Get_user_latitude, Get_user_longitude
from utils import Utils
# Tools
import joblib
import pyodbc
import os


# Initializing app
app = Flask(__name__)
app.config.from_object(Configuration)
# Initializing data base conexion 
server = os.environ['WEDEAL_SERVER'] 
database = os.environ['WEDEAL_DATABASE'] 
username = os.environ['WEDEAL_USER_NAME'] 
password = os.environ['WEDEAL_PASSWORD'] 
url_conexion='DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+''
# Initializing Graph
G = Graph('test','version1')


# Routes
@app.route('/user/<id_user>', methods=['GET'])
def predict_user(id_user):
    """ This route responses with a prediction based on user's work area
        and qualification to use it  need as parameter a id user, 
        at the end return a json with the response . 
        Prediction use the best model with the best score 
        located in best_models."""
    cnxn = pyodbc.connect(url_conexion)
    work_area = Get_work_area(id_user, cnxn, 'user')
    qualification = Get_user_qualification(id_user, cnxn)
    X_test = Utils.Convert_user_data(work_area, qualification)
    model = joblib.load('./best_models/user_model_16.pkl')
    prediction = model.predict(X_test.reshape(1,-1))
    cnxn.close()
    return jsonify({'prediccion' : list(prediction)})
    

@app.route('/job_offer/<id_job_offer>', methods=['GET'])
def predict_job_offer(id_job_offer):
    """ This route responses with a prediction based on job offer work area
        to use it  need as parameter a id job offer, 
        at the end return a json with the response . 
        Prediction use the best model with the best score 
        located in best_models."""
    cnxn = pyodbc.connect(url_conexion)
    work_area = Get_work_area(id_job_offer, cnxn, 'job_offer')
    X_test = Utils.Convert_job_offer_data(work_area)
    model = joblib.load('./best_models/job_offer_model_16.pkl')
    prediction = model.predict(X_test.reshape(1,-1))
    cnxn.close()
    return jsonify({'prediccion' : list(prediction)})

@app.route('/vertex/<id_user>', methods=['GET'])
def new_vertex(id_user):
    """ This route create a new vertex. 
        Time complexity = O(2A)
        Space complexity = O(A+E)
        """
    cnxn = pyodbc.connect(url_conexion)
    exist = Utils.User_already_exist(id_user, G)
    if exist == True:
        response = make_response(
                jsonify({'User already exist' : id_user}),
                400,)
    else :
        latitude = Get_user_latitude(id_user, cnxn)
        longitude = Get_user_longitude(id_user, cnxn)
        V = Vertex(id_user,latitude, longitude)
        G.verteces.append(V) 
        print(G.verteces)
        V.search_neighbours(G) #O(V)ok
        V.update_graph() #O(V)
        response = make_response(
            jsonify({'New user was add succesful' : V.value}),
            200,)
    cnxn.close()
    return response

@app.route('/location/<id_user>', methods=['GET'])
def localization_filter (id_user):
    """ This route find  closer users of a user based on his location. 
        O(V)+O(sorted)
       """
    cnxn = pyodbc.connect(url_conexion)
    exist = Utils.User_already_exist(id_user, G)
    if exist == False:
        response = make_response(
            jsonify({'user is not in graph yet, first you have to add it in graph' : id_user }),
            400,)
    else : 
        for vertex in G.verteces:
            if id_user == vertex.value:
                nearest_neighbours= sorted(vertex.weights, key=lambda x: x[1])
                response = make_response(
                jsonify({'nearest_neighbours' : list(nearest_neighbours)}),
                200,)
    cnxn.close()
    return response

if __name__ == "__main__":
    app.run()
