import sys
import os

# Add parent directory to path to import app
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, Property
import pytest


@pytest.fixture
def client():
    """Create a test client for the app"""
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            # Add a test property
            test_property = Property(
                title="Test Property",
                description="Test Description",
                price=100000,
                bedrooms=2,
                bathrooms=1,
                square_feet=1000,
                address="123 Test St",
                city="Test City",
                state="TS"
            )
            db.session.add(test_property)
            db.session.commit()
        yield client


def test_home_page(client):
    """Test that home page loads"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'DreamHome Realty' in response.data


def test_properties_page(client):
    """Test that properties page loads"""
    response = client.get('/properties')
    assert response.status_code == 200
    assert b'Test Property' in response.data


def test_property_detail(client):
    """Test that property detail page loads"""
    response = client.get('/property/1')
    assert response.status_code == 200
    assert b'Test Property' in response.data
    assert b'$100,000' in response.data


def test_property_not_found(client):
    """Test 404 for non-existent property"""
    response = client.get('/property/999')
    assert response.status_code == 404