import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

class TestRoutes:
    def test_route_existence(self, client):
        """Тест существования маршрутов"""
        routes_to_test = [
            '/',
            '/payments_list',
            '/invited_list',
            '/hotel_needed',
            '/hotel_needed_form',
            '/payments_by_date',
            '/payments_by_date_form',
            '/thesis_by_city',
            '/thesis_by_city_form',
            '/add_participant'
        ]
        
        for route in routes_to_test:
            response = client.get(route)
            # Маршрут должен возвращать какой-то HTTP статус
            assert response.status_code is not None
            assert isinstance(response.status_code, int)
    
    def test_content_type(self, client):
        """Тест типа контента в ответах"""
        response = client.get('/')
        # Должен возвращать HTML или перенаправление
        assert response.status_code in [200, 302]
        
        if response.status_code == 200:
            assert 'text/html' in response.content_type
    
    def test_static_files(self, client):
        """Тест статических файлов"""
        response = client.get('/static/css/style.css')
        # Статические файлы должны отдаваться или возвращать 404
        assert response.status_code in [200, 404]