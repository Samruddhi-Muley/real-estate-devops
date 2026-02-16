# init_db.py
from app import app, db, Property


def init_database():
    with app.app_context():
        # Create tables
        db.create_all()

        # Only add data if database is empty
        if Property.query.count() == 0:
            print("📊 Initializing database with sample data...")

            properties = [
                # ... (same properties as in app.py)
            ]

            for property in properties:
                db.session.add(property)

            db.session.commit()
            print(f"✅ Successfully added {len(properties)} properties!")
        else:
            print(f"✅ Database already contains {Property.query.count()} properties")


if __name__ == '__main__':
    init_database()