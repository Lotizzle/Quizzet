# setup.py

from app import db

# Create all the tables
db.create_all()

print("Database tables created successfully.")