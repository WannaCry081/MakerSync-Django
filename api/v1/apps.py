from pathlib import Path
from django.apps import AppConfig
from firebase_admin import credentials, initialize_app


class V1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'v1'


    def ready(self):
        current_dir=Path(__file__).resolve().parent.parent
        service_key=current_dir+"\\serviceAccountKey.json"

        credential=credentials.Certificate(service_key)
        initialize_app(credetial)