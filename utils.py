import pandas as pd
import joblib
import math

class Utils:

    def load_from_csv(self, path):
        return pd.read_csv(path)

    def load_from_mysql(self):
        pass

    def features_target(self, dataset, drop_cols, y):
        X = dataset.drop(drop_cols, axis=1)
        y = dataset[y]
        return X,y

    def model_export(self, clf, score, models_type):
        score = round(score)
        joblib.dump(clf, f'./best_models/{models_type}_model_{score}.pkl')

    def haversine(lat1,len1,lat2,len2):
        """ Calculate the distance between two 
            points of geolocalization based on Haversine metodh. """
        rad = math.pi/180 
        dlat=lat2-lat1
        dlen=len2-len1
        R=6372.795477598
        a=(math.sin(rad*dlat/2))**2 + math.cos(rad*lat1)*math.cos(rad*lat2)*(math.sin(rad*dlen/2))**2
        distancia = 2*R*math.asin(math.sqrt(a))
        return distancia 