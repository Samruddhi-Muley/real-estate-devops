from app import app, db, Property

with app.app_context():
    properties = Property.query.all()
    print(f"\n{'=' * 50}")
    print(f"Total properties in database: {len(properties)}")
    print(f"{'=' * 50}\n")

    if len(properties) == 0:
        print("❌ Database is EMPTY!")
        print("Solution: Run 'python add_sample_data.py'")
    else:
        print("✅ Database has data!")
        print("\nProperty list:")
        for prop in properties:
            print(f"  - ID: {prop.id}, Title: {prop.title}, Price: ${prop.price:,.0f}")