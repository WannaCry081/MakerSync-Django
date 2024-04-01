from pathlib import Path
from firebase_admin import initialize_app, credentials, firestore


def firebase_firestore():
    
    current_dir=Path(__file__).resolve().parent.parent.parent.parent
    service_key=f"{current_dir}\\serviceAccountKey.json"
    
    credential=credentials.Certificate(service_key)
    initialize_app(credential)
    
    return firestore.client()
    