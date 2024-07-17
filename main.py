import streamlit as st
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

with open("config/secret.json", "r") as f:
    data = json.load(f)

key = data['DBKey']
cred = credentials.Certificate('config/firebase-key.json')
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://minor-piece-4ade8-default-rtdb.firebaseio.com/'
    });

# print(datetime.date)
now = datetime.now()
ref = db.reference(f'{now.date()}')
