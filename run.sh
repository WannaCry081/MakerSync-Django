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
        `$1` install -r "$DEPENDENCIES_PATH"
    else 
        `$1` install django django-ninja-extra
        `$1` install firebase-admin python-dotenv
    fi
}

run_server() {
    echo "Running Server..."
    python manage.py runserver
    `$1`
}


if [ "$1" = "lib" ]; then 

    if [ ! -d "$VENV_PATH" ]; then 
        # Creating the python virtual environment 
        virtualenv "$VENV_PATH"

        # Installing the python dependencies
        install_dependencies pip
    fi
    
    echo "Activating virtual environment"

    # Activating python virtual environment
    source "$VENV_PATH/Scripts/activate"

    # Running django local server 
    run_server deactivate
else

    # Initializing pip virtual environment
    pipenv shell

    if [ ! -f "$PIPENV_PATH" ]; then 
        # Installing the python dependencies
        install_dependencies pipenv
    fi

    # Running django local server 
    run_server exit
fi 