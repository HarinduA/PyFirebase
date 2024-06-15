# Filename: add_data_realtime_db.py

import firebase_admin
from firebase_admin import credentials, db

# Initialize the Firebase app with a service account, granting admin privileges
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://<your-database-name>.firebaseio.com/'  # Replace <your-database-name> with your actual database name
})

# Reference the database location you want to add data to
ref = db.reference('users')  # Replace 'users' with your specific path

# Data to be added
new_data = {
    'name': 'John Doe',
    'email': 'johndoe@example.com',
    'age': 30
}

# Add the new data to the database
ref.push(new_data)  # Push creates a new unique key for each new entry

print("Data added to Realtime Database!")
