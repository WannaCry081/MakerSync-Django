#!/usr/bin/bash


# Python virtual environment 
VENV_PATH="$(pwd)/venv"

# Pip virtual environment
PIPENV_PATH="$(pwd)/Pipfile.lock"

# List of dependencies
DEPENDENCIES_PATH="$(pwd)/requirements.txt"


install_dependencies() {
    # Check if requirements.txt exists
    if [ -f "$DEPENDENCIES_PATH" ]; then 
        pip install -r "$DEPENDENCIES_PATH"
    else 
        pip install python-dotenv
        pip install django django-ninja-extra
        pip install firebase-admin psycopg2-binary
        pip install pydantic[email]

        pip freeze > requirements.txt
    fi
}

run_server() {
    echo "Running Server..."

    python manage.py makemigrations v2
    python manage.py migrate
    python manage.py runserver
    `$1`
}


if [ "$#" -eq 0 ] || [ "$1" = "venv" ]; then 
    echo "Activating virtual environment"

    if [ ! -d "$VENV_PATH" ]; then 
        # Creating the python virtual environment 
        virtualenv "$VENV_PATH"

        # Activating python virtual environment
        source "$VENV_PATH/Scripts/activate"

        # Installing the python dependencies
        install_dependencies
    else 
        # Activating python virtual environment
        source "$VENV_PATH/Scripts/activate"
    fi

    # Running django local server 
    run_server deactivate

elif [ "$1" = "pipenv" ]; then 
    # Initializing pip virtual environment
    pipenv shell

    if [ ! -f "$PIPENV_PATH" ]; then 
        # Installing the python dependencies
        install_dependencies pipenv
    fi

    # Running django local server 
    run_server exit
fi 
