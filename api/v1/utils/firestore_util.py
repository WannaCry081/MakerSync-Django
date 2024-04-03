import os
from pathlib import Path
from dotenv import load_dotenv
from firebase_admin import initialize_app, credentials, firestore


load_dotenv()

current_dir = Path(__file__).resolve().parent.parent.parent.parent
service_key_path = current_dir / "serviceAccountKey.json"

if not service_key_path.exists():
    service_key = {
        "type": os.environ.get("TYPE"),
        "project_id": os.environ.get("PROJECT_ID"),
        "private_key_id": os.environ.get("PRIVATE_KEY_ID"),
        "private_key": os.environ.get("PRIVATE_KEY").replace("\\n", "\n"),
        "client_email": os.environ.get("CLIENT_EMAIL"),
        "client_id": os.environ.get("CLIENT_ID"),
        "auth_uri": os.environ.get("AUTH_URI"),
        "token_uri": os.environ.get("TOKEN_URI"),
        "auth_provider_x509_cert_url": os.environ.get("AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.environ.get("CLIENT_X509_CERT_URL"),
        "universe_domain": os.environ.get("UNIVERSE_DOMAIN")
    }
else:
    service_key = str(service_key_path)  
     
credential = credentials.Certificate(service_key)
initialize_app(credential)  


def firebase_firestore():    
    return firestore.client()
