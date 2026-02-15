import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app, db, Property
import pytest


@pytest.fixture
def client():
    """Create a test client for the app with in-memory database"""
    # Configure app for testing
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'

    with app.app_context():
        # Create all tables
        db.create_all()

        # Add test data
        test_property = Property(
            title="Test Property",
            description="Test Description for testing purposes",
            price=100000,
            bedrooms=2,
            bathrooms=1,
            square_feet=1000,
            address="123 Test Street",
            city="Test City",
            state="TS"
        )
        db.session.add(test_property)
        db.session.commit()

    # Create test client
    with app.test_client() as client:
        yield client

    # Cleanup
    with app.app_context():
        db.drop_all()


def test_home_page(client):
    """Test that home page loads successfully"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'DreamHomes' in response.data or b'Find Your Dream Home' in response.data


def test_properties_page(client):
    """Test that properties page loads"""
    response = client.get('/properties')
    assert response.status_code == 200


def test_property_detail_exists(client):
    """Test that a property detail page loads"""
    response = client.get('/property/1')
    assert response.status_code == 200
    # Check for common property page elements
    assert b'Test Property' in response.data or b'bedroom' in response.data.lower()


def test_property_not_found(client):
    """Test 404 for non-existent property"""
    response = client.get('/property/999')
    assert response.status_code == 404