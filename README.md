# PyFirebase

These Python scripts provide a streamlined and automated way to add data to Firebase, leveraging its powerful cloud-based database services. With two distinct scripts, you can choose to store your data in either Firebase Realtime Database or Firestore, depending on your application's needs.

Firebase Realtime Database Script:

The add_data_realtime_db.py script is designed to seamlessly insert new records into the Firebase Realtime Database. Users can define their data and specify the target database path. The script automatically handles data insertion by generating unique keys for each entry, ensuring no data overwrites existing records unless specified. This functionality is ideal for applications requiring real-time data synchronization and updates, such as chat applications or live scoreboards.
Firestore Script:

The add_data_firestore.py script focuses on interacting with Firebase's Firestore database, a flexible and scalable NoSQL cloud database. This script allows users to insert data into a specific document within a collection, either by specifying a document ID or by letting Firestore generate one. Firestore's document-based structure is well-suited for use cases where hierarchical data organization and advanced querying capabilities are needed, such as user profiles or product inventories.
