from app import app, db, Property
from datetime import datetime


def init_database():
    with app.app_context():
        # Create tables
        db.create_all()

        # Check if data already exists
        if Property.query.first() is None:
            print("Initializing database with sample data...")

            properties = [
                Property(
                    title="Modern Downtown Apartment",
                    description="Beautiful modern apartment in the heart of downtown with amazing city views. Features floor-to-ceiling windows, hardwood floors, and access to rooftop terrace.",
                    price=450000,
                    bedrooms=2,
                    bathrooms=2,
                    square_feet=1200,
                    address="123 Main Street",
                    city="Seattle",
                    state="WA",
                    image_url="https://images.unsplash.com/photo-1545324418-cc1a3fa10c00?w=800&h=600&fit=crop"
                ),
                Property(
                    title="Spacious Family Home",
                    description="Perfect family home with large backyard and excellent school district. Recently renovated kitchen with granite countertops and stainless steel appliances.",
                    price=675000,
                    bedrooms=4,
                    bathrooms=3,
                    square_feet=2500,
                    address="456 Oak Avenue",
                    city="Portland",
                    state="OR",
                    image_url="https://images.unsplash.com/photo-1568605114967-8130f3a36994?w=800&h=600&fit=crop"
                ),
                Property(
                    title="Cozy Studio Loft",
                    description="Charming studio loft perfect for young professionals. Exposed brick walls, high ceilings, and walking distance to cafes and public transit.",
                    price=285000,
                    bedrooms=1,
                    bathrooms=1,
                    square_feet=650,
                    address="789 Pine Street",
                    city="San Francisco",
                    state="CA",
                    image_url="https://images.unsplash.com/photo-1484154218962-a197022b5858?w=800&h=600&fit=crop"
                ),
                Property(
                    title="Luxury Waterfront Villa",
                    description="Stunning waterfront property with private dock and panoramic ocean views. Features infinity pool, wine cellar, and smart home technology throughout.",
                    price=2500000,
                    bedrooms=5,
                    bathrooms=4,
                    square_feet=4500,
                    address="101 Beach Boulevard",
                    city="Miami",
                    state="FL",
                    image_url="https://images.unsplash.com/photo-1613490493576-7fde63acd811?w=800&h=600&fit=crop"
                ),
                Property(
                    title="Mountain Retreat Cabin",
                    description="Peaceful mountain cabin surrounded by nature. Perfect weekend getaway with wood-burning fireplace, large deck, and hiking trails nearby.",
                    price=425000,
                    bedrooms=3,
                    bathrooms=2,
                    square_feet=1800,
                    address="2020 Alpine Road",
                    city="Denver",
                    state="CO",
                    image_url="https://images.unsplash.com/photo-1542718610-a1d656d1884c?w=800&h=600&fit=crop"
                ),
                Property(
                    title="Historic Brownstone",
                    description="Beautifully preserved historic brownstone with original architectural details. Updated with modern amenities while maintaining classic charm.",
                    price=1250000,
                    bedrooms=4,
                    bathrooms=3,
                    square_feet=3200,
                    address="567 Heritage Lane",
                    city="Boston",
                    state="MA",
                    image_url="https://images.unsplash.com/photo-1580587771525-78b9dba3b914?w=800&h=600&fit=crop"
                )
            ]

            for property in properties:
                db.session.add(property)

            db.session.commit()
            print(f"Successfully added {len(properties)} properties!")
        else:
            print("Database already contains data. Skipping initialization.")


if __name__ == '__main__':
    init_database()