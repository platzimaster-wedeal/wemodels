from flask_testing import TestCase
from flask import current_app, url_for
from server import app  
class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED']= False
        return app
    
    def test_app_exist(self):
        self.assertIsNotNone(current_app)

    def test_app_in_test_mode(self):
        self.assertTrue(current_app.config['TESTING'])

    def test_root(self):
        response = self.client.get(url_for('init'))
        self.assert200(response)

    def test_predict_user_successful(self):
        id_user_test = 15
        response = self.client.get(f'/user/{id_user_test}')
        self.assert200(response)

    def test_predict_user_faild_not_data_in_database(self):
        id_user_test_wrong = -1
        response = self.client.get(f'/user/{id_user_test_wrong}')
        self.assert400(response)

    def test_predict_user_faild_id_not_type_int(self):
        id_user_test_wrong = 'user'
        response = self.client.get(f'/user/{id_user_test_wrong}')
        self.assert400(response)

    def test_predict_job_offer_successful(self):
        id_job_offer_test = 15
        response = self.client.get(f'/job_offer/{id_job_offer_test}')
        self.assert200(response)

    def test_predict_job_offer_faild_not_data_in_database(self):
        id_job_offer_test_wrong = -1
        response = self.client.get(f'/job_offer/{id_job_offer_test_wrong}')
        self.assert400(response)
    #
    def test_predict_job_offer_faild_id_not_type_int(self):
        id_job_offer_test_wrong = 'job_offer'
        response = self.client.get(f'/job_offer/{id_job_offer_test_wrong}')
        self.assert400(response)

    def test_add_new_user_on_vertex_successful(self):
        id_user_test = 15
        response = self.client.get(f'/vertex/{id_user_test}')
        self.assert200(response)

    def test_not_add_user_if_user_already_exist(self):
        id_user_test = 15
        self.client.get(f'/vertex/{id_user_test}')
        response = self.client.get(f'/vertex/{id_user_test}')
        self.assert400(response)  
    
    def test_add_new_user_faild_not_data_in_database(self):
        id_user_test_wrong = -1
        response = self.client.get(f'/vertex/{id_user_test_wrong}')
        self.assert400(response)
    #
    def test_add_new_user_faild_id_not_type_int(self):
        id_user_test_wrong = 'user'
        response = self.client.get(f'/vertex/{id_user_test_wrong}')
        self.assert400(response)

    def test_localization_filter_redirect_successful(self):
        id_user_test = 15
        response = self.client.get(f'/location/{id_user_test}')
        self.assertRedirects(response, url_for('bar'))

    def test_location_filter_faild_not_data_in_database(self):
        id_user_test_wrong = -1
        response = self.client.get(f'/location/{id_user_test_wrong}')
        self.assert400(response)

    def test_location_filter_faild_id_not_type_int(self):
        id_user_test_wrong = 'user'
        response = self.client.get(f'/location/{id_user_test_wrong}')
        self.assert400(response)

    def test_work_area_filter_redirect_successful_type_user(self):
        name_work_area_test = 'Designing'
        type_ = 'user'
        response = self.client.get(f'/bar/{name_work_area_test}/{type_}')
        self.assertRedirects(response, url_for('bar'))

    def test_work_area_filter_redirect_successful_type_job_offer(self):
        name_work_area_test = 'Designing'
        type_ = 'job_offer'
        response = self.client.get(f'/bar/{name_work_area_test}/{type_}')
        self.assertRedirects(response, url_for('bar'))

    def test_work_area_filter_faild_not_data_in_database_type_job_offer(self):
        name_work_area_test = 'Designing_wrong'
        type_ = 'job_offer'
        response = self.client.get(f'/bar/{name_work_area_test}/{type_}')
        self.assert400(response)

    def test_work_area_filter_faild_not_data_in_database_type_user(self):
        name_work_area_test = 'Designing_wrong'
        type_ = 'user'
        response = self.client.get(f'/bar/{name_work_area_test}/{type_}')
        self.assert400(response)

    def test_bar_list_len_equal_to_zero_successful(self):
        response = self.client.get('/bar')
        self.assert400(response)