# add_sample_data.py
from app import app, db, Property

with app.app_context():
    # Clear existing data
    db.drop_all()
    db.create_all()

    # Add sample properties
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
        ),
        Property(
            title="Contemporary Condo",
            description="Sleek contemporary condo in vibrant neighborhood. Open floor plan, chef's kitchen, and floor-to-ceiling windows with city skyline views.",
            price=525000,
            bedrooms=2,
            bathrooms=2,
            square_feet=1400,
            address="890 Urban Plaza",
            city="Chicago",
            state="IL",
            image_url="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?w=800&h=600&fit=crop"
        ),
        Property(
            title="Suburban Ranch House",
            description="Classic ranch-style home on quiet cul-de-sac. Spacious yard, attached garage, and close to parks and schools. Move-in ready!",
            price=395000,
            bedrooms=3,
            bathrooms=2,
            square_feet=1900,
            address="345 Maple Drive",
            city="Austin",
            state="TX",
            image_url="https://images.unsplash.com/photo-1570129477492-45c003edd2be?w=800&h=600&fit=crop"
        ),
        Property(
            title="Penthouse Suite",
            description="Exclusive penthouse with 360-degree city views. Private elevator, wraparound terrace, and luxury finishes throughout. True urban living at its finest.",
            price=3200000,
            bedrooms=3,
            bathrooms=3,
            square_feet=3500,
            address="777 Sky Tower",
            city="New York",
            state="NY",
            image_url="https://images.unsplash.com/photo-1613977257363-707ba9348227?w=800&h=600&fit=crop"
        ),
        Property(
            title="Farmhouse on Acreage",
            description="Charming farmhouse on 5 acres with barn and pasture. Perfect for hobby farming or horses. Peaceful country living just 30 minutes from downtown.",
            price=580000,
            bedrooms=4,
            bathrooms=2,
            square_feet=2200,
            address="1500 Country Road",
            city="Nashville",
            state="TN",
            image_url="https://images.unsplash.com/photo-1605276374104-dee2a0ed3cd6?w=800&h=600&fit=crop"
        ),
        Property(
            title="Beach Cottage",
            description="Adorable beach cottage steps from the sand. Perfect vacation home or rental investment. Enjoy sunrise coffee on the porch and sunset beach walks.",
            price=650000,
            bedrooms=2,
            bathrooms=2,
            square_feet=1100,
            address="88 Seaside Avenue",
            city="San Diego",
            state="CA",
            image_url="https://images.unsplash.com/photo-1499916078039-922301b0eb9b?w=800&h=600&fit=crop"
        ),
        Property(
            title="Modern Townhouse",
            description="Brand new construction townhouse in desirable neighborhood. Energy-efficient design, attached garage, and low-maintenance living.",
            price=475000,
            bedrooms=3,
            bathrooms=2,
            square_feet=1700,
            address="234 Newbury Street",
            city="Phoenix",
            state="AZ",
            image_url="https://images.unsplash.com/photo-1600596542815-ffad4c1539a9?w=800&h=600&fit=crop"
        )
    ]

    for property in properties:
        db.session.add(property)

    db.session.commit()
    print(f"Successfully added {len(properties)} properties!")