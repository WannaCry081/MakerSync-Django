#!/usr/bin/bash

VENV_PATH="$(pwd)/venv"


if [ -d "$VENV_PATH" ]; then 
    echo "Activating virtual environment"
    source "$VENV_PATH/Scripts/activate"
else
    echo "Creating virtual environment"
    virtualenv "$VENV_PATH"
    source "$VENV_PATH/Scripts/activate"
    python -m pip install -r "$(pwd)/requirements.txt"
    pip install django django-ninja-extra
fi

echo "Running server..."
python manage.py runserver
deactivate

