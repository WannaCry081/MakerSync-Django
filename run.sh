#!/usr/bin/bash

VENV_PATH="$(pwd)/venv"
DEPENDENCIES_PATH="$(pwd)/requirements.txt"

if [ -d "$VENV_PATH" ]; then 
    echo "Activating virtual environment"
    source "$VENV_PATH/Scripts/activate"
else
    echo "Creating virtual environment"
    virtualenv "$VENV_PATH"
    source "$VENV_PATH/Scripts/activate"

    if [ -d "$DEPENDENCIES_PATH" ]; then 
        python -m pip install -r "$(pwd)/requirements.txt"
    else
        pip install django django-ninja-extra firebase-admin python-dotenv
    fi
    
    pip install django django-ninja-extra
fi

echo "Running server..."
python manage.py runserver
deactivate

