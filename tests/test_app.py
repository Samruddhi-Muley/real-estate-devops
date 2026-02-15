import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app
import pytest


@pytest.fixture
def client():
    """Create a test client for the app"""
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    """Test that home page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'DreamHomes' in response.data
    assert b'Find Your Dream Home' in response.data


def test_properties_page(client):
    """Test that properties page loads"""
    response = client.get('/properties')
    assert response.status_code == 200
    assert b'Properties' in response.data


def test_property_detail_exists(client):
    """Test that a property detail page loads"""
    response = client.get('/property/1')
    assert response.status_code == 200
    # Check for common elements on property pages
    assert b'Bedroom' in response.data or b'bedroom' in response.data


def test_property_not_found(client):
    """Test 404 for non-existent property"""
    response = client.get('/property/999')
    assert response.status_code == 404