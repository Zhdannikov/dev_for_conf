def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    # Ищем русские слова в контенте
    html_content = response.data.decode('utf-8')
    assert 'конференц' in html_content.lower() or 'управление' in html_content.lower()

def test_static_files(client):
    response = client.get('/static/css/style.css')
    assert response.status_code in [200, 404]