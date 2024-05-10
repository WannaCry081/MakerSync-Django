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
		"HOST": os.environ.env("HOST"), 
		"NAME": os.environ.env("NAME"), 
		"USER": os.environ.env("USER"), 
		"PASSWORD": os.environ.env("PASSWORD"), 
		"PORT": os.environ.env("PORT"), 
	} 
}