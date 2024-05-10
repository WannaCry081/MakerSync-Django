import os
from dotenv import load_dotenv
from config.settings.base import *


DEBUG = False

ALLOWED_HOSTS = [
    ".vercel.app", 
    ".now.sh",
    "maker-sync-django.vercel.app"]

DATABASES = { 
	"default": { 
		"ENGINE": "django.db.backends.postgresql_psycopg2", 
		"HOST": os.environ.get("HOST"), 
		"NAME": os.environ.get("NAME"), 
		"USER": os.environ.get("USER"), 
		"PASSWORD": os.environ.get("PASSWORD"), 
		"PORT": os.environ.get("PORT"), 
	} 
}