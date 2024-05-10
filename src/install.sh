#!/bin/bash

#help argument
print_help() {
    echo "  install      checks for virtual environment, installs and activates virtual environment, and installed dependecies"
    echo "  run          runs the program, called automatically from install"
}

#checks for virtual environemnt and installs dependecies
install() {
    #if venv already exists
    echo "Checking if virtual environment already exists..."
    if [ -d ".venv" ]; then
        echo "Virtual environment already exists in directory"
    #install venv
    else
        echo "Virtual environment not installed in directory, installing..."
        python3 -m pip install --user virtualenv
        echo "Virtual environment installed"
        #create a new venv
        echo "Creating new virtual environment in directory"
        python3 -m venv ".venv"
        echo "Virtual environment created"
    fi

    #activate venv
    echo "Activating virtual environment..."
    source ".venv/bin/activate"
    echo "Virtual environment activated"
    
    #upgrade pip installer
    echo "Checking for latest PIP version..."
    pip install -U pip

    #install dependencies
    echo "Installing any dependencies..."
    if [ -f "requirements.txt" ]; then
        pip install -r ./requirements.txt
    fi

    run
}

run(){
    #activate venv
    echo "Activating virtual environment..."
    source ".venv/bin/activate"
    echo "Virtual environment activated"
    echo "Running marketplace.py..."
    python3 marketplace.py
}

#help args
if [ "$1" = "--help" ] || [ "$1" = "-h" ]; then
    print_help
    return 0
fi

#install args
if [ "$1" = "--install" ] || [ "$1" = "-i" ]; then
    install
    return 0
fi

#run args
if [ "$1" = "--run" ] || [ "$1" = "-r" ]; then
    run
    return 0
fi