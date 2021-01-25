import firebase_admin
from firebase_admin import firestore
from datetime import datetime
import random

firebase_admin.initialize_app()
db = firestore.client()


def set_expense(request):
    try:
        ref = db.collection('expenses').document()
        ref.set({
            'createdAt': datetime.now(),
            'expenses': random.randint(1,200)
        })
    except Exception as e:
        return f'Error: {e}', 400

    return 'OK', 200

