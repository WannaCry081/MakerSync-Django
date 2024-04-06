#!/usr/bin/bash


VENV_PATH="$(pwd)/venv"
PIPENV_PATH="$(pwd)/Pipfile.lock"
DEPENDENCIES_PATH="$(pwd)/requirements.txt"


install_dependencies() {
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
}



if [ "$1" = "lib" ]; then 

    echo "Activating virtual environment"

    if [ ! -d "$VENV_PATH" ]; then 
        virtualenv "$VENV_PATH"
        install_dependencies pip
    fi
    
    source "$VENV_PATH/Scripts/activate"

    run_server 
    deactivate

else

    pipenv shell

    if [ ! -f "$PIPENV_PATH" ]; then 
        install_dependencies pipenv
    fi

    run_server
    exit
fi 