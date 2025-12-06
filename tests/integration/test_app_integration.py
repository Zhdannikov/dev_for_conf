import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class TestAppIntegration:
    def test_main_routes(self, client):
        routes = ['/', '/payments_list', '/invited_list']
        for route in routes:
            response = client.get(route)
            assert response.status_code != 500
    
    def test_form_routes(self, client):
        routes = ['/hotel_needed_form', '/payments_by_date_form', '/thesis_by_city_form']
        for route in routes:
            response = client.get(route)
            assert response.status_code in [200, 302, 404]
    
    def test_template_rendering(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b'<html' in response.data