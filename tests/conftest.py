import pytest
import sys
import os
from unittest.mock import patch, MagicMock

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

@pytest.fixture(autouse=True)
def mock_dependencies():
    with patch('pymongo.MongoClient') as mock_mongo:
        mock_client = MagicMock()
        mock_collection = MagicMock()
        mock_collection.find.return_value = []
        mock_collection.find_one.return_value = None
        mock_client.conference_db.participants = mock_collection
        mock_client.conference_db.invited = mock_collection  
        mock_client.conference_db.payments = mock_collection
        mock_mongo.return_value = mock_client
        yield

@pytest.fixture
def app():
    from app import app as flask_app
    flask_app.config.update({'TESTING': True, 'WTF_CSRF_ENABLED': False})
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()