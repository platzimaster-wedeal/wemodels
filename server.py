"""This is the main  file that control all aplication internal  flow"""
#Flask
from flask import Flask, make_response, jsonify, redirect, url_for
from configuration import Configuration
from flask_cors import CORS, cross_origin
#We_deal
from models.graph import Graph, Vertex
from queries.queries import Get_work_area, Get_user_qualification, Get_user_latitude, Get_user_longitude, Get_info_based_on_work_area, Get_work_area_id
from utils import Utils
from models.bar import Users_list
# Tools
import joblib
import pyodbc
import os


# Initializing app
app = Flask(__name__)
app.config.from_object(Configuration)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'WeDeal'
# Initializing data base conexion 
server = os.environ.get('DB_HOST')
database = os.environ.get('DB_NAME')
username =  os.environ.get('DB_USER')
password =   os.environ.get('DB_PASS')
url_conexion='DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+password+''
# Initializing Graph
G = Graph('test','version1')
# Initializing User List
userslist = Users_list()


# Routes
@app.route('/', methods=['GET'])
@cross_origin()
def init():
    return "Welcome to We deal, this api is only available to We Deal developers"

@app.route('/user/<id_user>', methods=['GET'])
@cross_origin()
def predict_user(id_user):
    """ This route responses with a prediction based on user's work area
        and qualification to use it  need as parameter a id user, 
        at the end return a json with the response . 
        Prediction use the best model with the best score 
        located in best_models."""
    return "entre"    
    cnxn = pyodbc.connect(url_conexion)
    return "hola"
    cursor = cnxn.cursor()
    row = cursor.execute("SELECT title FROM work_areas WHERE id=?", id ).fetchone()
    work_area = Get_work_area(id_user, cnxn, 'user')
    qualification = Get_user_qualification(id_user, cnxn)
    if work_area == None or qualification == None:
        response = make_response(
                jsonify({'Someting was wrong with user data' : id_user}),
                400,)
    else:
        X_test = Utils.Convert_user_data(work_area, qualification)
        model = joblib.load('./best_models/user_model_16.pkl')
        prediction = model.predict(X_test.reshape(1,-1))
        response = make_response(
                jsonify({'prediccion' : list(prediction)}),
                200,)
    cnxn.close()
    return response
    

@app.route('/job_offer/<id_job_offer>', methods=['GET'])
@cross_origin()
def predict_job_offer(id_job_offer):
    """ This route responses with a prediction based on job offer work area
        to use it  need as parameter a id job offer, 
        at the end return a json with the response . 
        Prediction use the best model with the best score 
        located in best_models."""
    cnxn = pyodbc.connect(url_conexion)
    work_area = Get_work_area(id_job_offer, cnxn, 'job_offer')
    if work_area == None:
        response = make_response(
                jsonify({'Someting was wrong with job_offer data' : id_job_offer}),
                400,)
    else:
        X_test = Utils.Convert_job_offer_data(work_area)
        model = joblib.load('./best_models/job_offer_model_16.pkl')
        prediction = model.predict(X_test.reshape(1,-1))
        response = make_response(
                jsonify({'prediccion' : list(prediction)}),
                200,)
    cnxn.close()
    return response

@app.route('/vertex/<id_user>', methods=['GET'])
@cross_origin()
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
        if latitude == None or longitude == None:
            response = make_response(
                jsonify({'Someting was wrong with job_offer data' : id_user}),
                400,)
        else:
            V = Vertex(id_user,latitude, longitude)
            G.verteces.append(V) 
            V.search_neighbours(G) #O(V)
            V.update_graph() #O(V)
            response = make_response(
                jsonify({'New user was add succesful' : V.value}),
                200,)
    cnxn.close()
    return response

@app.route('/location/<id_user>', methods=['GET'])
@cross_origin()
def localization_filter (id_user):
    """ This route find  closer users of a user based on his location.
        This route receive a id user and redirec to rute /bar 
        O(V)+O(sorted)
       """
    cnxn = pyodbc.connect(url_conexion)
    exist = Utils.User_already_exist(id_user, G)
    if exist == False:
        response = make_response(
               jsonify({'user is not in graph yet, first you have to add it in graph' : id_user }),
               400,)
        return response
    else : 
        for vertex in G.verteces:
            if id_user == vertex.value:
                nearest_neighbours= sorted(vertex.weights, key=lambda x: x[1])
                users = []
                for element in nearest_neighbours:
                    users.append(int(element[0]))
                userslist.users2 = users
                #response = make_response(
                #jsonify({'nearest_neighbours' : list(nearest_neighbours)}),
                # 200,)
    userslist.bar_filter()
    cnxn.close()
    return redirect(url_for('bar'))

@app.route('/bar/<work_area>/<type_>',methods=['GET'])
@cross_origin()
def Search_bar_filter(work_area, type_):
    """ This route find an id users or id job offer 
        based on a specific work area. 
        This route recieve a work area name and a type, 
        user type or job offer type  and redirect to route /bar """
    cnxn = pyodbc.connect(url_conexion)
    id_work_area = Get_work_area_id(work_area, cnxn)
    if type_ == 'job_offer':
      users = Get_info_based_on_work_area(id_work_area, cnxn, type_)
    else:
        users = Get_info_based_on_work_area(id_work_area, cnxn, type_)
    if id_work_area == None or users == None:
        response = make_response(
                        jsonify({'Someting was wrong with  your request' : work_area}),
                        400,)
        return response
    #elif type_ == 'user':
    #    response = make_response(
    #            jsonify({'users filter by work area' : users}),
    #            200,)
    #elif type_ == 'job_offer':
    #    response = make_response(
    #            jsonify({'job_offer filter by work area' : users}),
    #            200,)
    userslist.users1 = users
    userslist.bar_filter()
    cnxn.close()
    return redirect(url_for('bar'))
    

@app.route('/bar', methods=['GET'])
@cross_origin()
def bar():
    """ This route create a list of user based on 
        two filters, filter by work area and filter by location.
        this route  receive nothing and retorn a lists of 10 users
        order by filters"""  
    if len(userslist.users) == 0:
        response = make_response(
                jsonify({'there are not more imformation to send' : userslist.users}),
                400,)
        return response
    elif len(userslist.users) >= 10:
        list1 = userslist.users[:10]
        for i in range(11):
            userslist.users.pop(0)
        response = make_response(
                jsonify({'users list is' : list1}),
                200,)
        return response
    else: 
        response = make_response(
                jsonify({'users list is' : userslist.users}),
                200,)
        userslist.users = []   
        return response
        
        



if __name__ == "__main__":
    app.run()
