from utils import Utils
from models.models import Models

if __name__ == "__main__":

    utils = Utils()
    models = Models('user')
    data = utils.load_from_csv('./in/user_data.csv')
    X, y = utils.features_target(data, ['user_id'],['user_id'])
    models.grid_training(X,y)


    models = Models('job_offer')
    data = utils.load_from_csv('./in/job_offer_data.csv')
    X, y = utils.features_target(data, ['user_id'],['user_id'])
    models.grid_training(X,y)
