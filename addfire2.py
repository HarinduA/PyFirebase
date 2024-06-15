# Filename: add_data_firestore.py

import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase app with a service account, granting admin privileges
cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()

# Reference to a collection and document
# Replace 'users' with your collection name
# Replace 'user_id' with a specific document ID or use db.collection('users').add() to auto-generate an ID
doc_ref = db.collection('users').document('user_id')

# Data to be added
new_data = {
    'name': 'Jane Doe',
    'email': 'janedoe@example.com',
    'age': 25
}

# Set the data (this will create or overwrite the document)
doc_ref.set(new_data)

print("Data added to Firestore!")
