#!/usr/bin/bash


VENV_PATH="$(pwd)/venv"
PIPENV_PATH="$(pwd)/Pipfile"
DEPENDENCIES_PATH="$(pwd)/requirements.txt"


if [ "$1" = "lib" ]; then 

    if [ -d "$VENV_PATH" ]; then 
        echo "Activating virtual environment"
        source "$VENV_PATH/Scripts/activate"
    else
        echo "Creating virtual environment"
        virtualenv "$VENV_PATH"
        source "$VENV_PATH/Scripts/activate"
    fi
    
    if [ -f "$DEPENDENCIES_PATH" ]; then 
        python -m pip install -r "$DEPENDENCIES_PATH"
    else
        pip install django django-ninja-extra 
        pip install firebase-admin python-dotenv 
        pip install django-cors-headers

    fi
    
    echo "Running server..."
    python manage.py runserver
    deactivate

else

    if [ -f "$PIPENV_PATH" ]; then 
        pipenv shell
    else
        pipenv install -r "$DEPENDENCIES_PATH"
    fi

    echo "Running server..."
    python manage.py runserver
    exit
fi 