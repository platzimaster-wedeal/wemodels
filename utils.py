""" Some utilities that are used in the application"""
import pandas as pd
import numpy as np
import joblib
import math

class Utils:

    def load_from_csv(self, path):
        """ Read a csv """
        return pd.read_csv(path)

    def features_target(self, dataset, drop_cols, y):
        """ Divide a dataset in two variables X and y """
        X = dataset.drop(drop_cols, axis=1)
        y = dataset[y]
        return X,y

    def model_export(self, clf, score, models_type):
        """ Export a machine learning model"""
        score = round(score)
        joblib.dump(clf, f'./best_models/{models_type}_model_{score}.pkl')

    def haversine(self, lat1,lon1,lat2,lon2):
        """ Calculate the distance between two 
            points of geolocalization based on Haversine metodh. """
        rad = math.pi/180 
        dlat=lat2-lat1
        dlon=lon2-lon1
        R=6372.795477598
        uno = dlat/2
        a= (math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlon/2))**2
        distancia = 2*R*math.asin(math.sqrt(a))
        return distancia 

    def Convert_user_data(work_area, qualification):
        """ Convert user data in a data with the necessary format 
            to use in the model prediction"""
        areas = ['HR', 'Designing', 'Managment', 'Information Technology',
        'Education', 'Advocate', 'Business Development',
        'Health & Fitness', 'Agricultural', 'BPO', 'Sales', 'Consultant',
        'Digital Media', 'Building & Construction', 'Automobile',
        'Banking', 'Engineering', 'Food & Beverages', 'Finance', 'Apparel',
        'Accountant', 'Architects', 'Public Relations', 'Arts', 'Aviation']
        x = []
        for area in areas:
            if area == work_area:
                x.append(1)
            else:
                x.append(0)
        x.append(qualification)
        return np.array(x)

    def Convert_job_offer_data(work_area):
        """ Convert job offer data in a data with the necessary format 
            to use in the model prediction"""
        areas = ['HR', 'Designing', 'Managment', 'Information Technology',
        'Education', 'Advocate', 'Business Development',
        'Health & Fitness', 'Agricultural', 'BPO', 'Sales', 'Consultant',
        'Digital Media', 'Building & Construction', 'Automobile',
        'Banking', 'Engineering', 'Food & Beverages', 'Finance', 'Apparel',
        'Accountant', 'Architects', 'Public Relations', 'Arts', 'Aviation']
        x = []
        for area in areas:
            if area == work_area:
                x.append(1)
            else:
                x.append(0)
        return np.array(x)

    def User_already_exist(id_user, G):
        for vertex in G.verteces:
            if vertex.value == id_user:
                return True
            else :
                return False



