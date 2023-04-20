# integration_test/test_routes.py

import pytest
from name import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    

def test_overlaps(client):
    response = client.get('/overlaps')
    assert response.status_code == 200
    

def test_settings(client):
    response = client.get('/settings')
    assert response.status_code == 200
    
