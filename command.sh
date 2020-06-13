#!bin/sh

function create(){
    cd 
    cd 'e:\Projects'
    echo "Creating Online Repository"
    python 'E:\Projects\Dev Kit\create.py' $1
    git clone https://github.com/abdullahth/$1.git
    cd $1
    git init
    # Initilize the Repository
    touch $2 $3 $4
    file $2
    file $3
    file $4
    # Opening Visual Studio Code --> Change it with the command of your text editor
    echo "Openning Visual Studio Code"
    code .
    start cmd
}

function file(){
    # Touch a new file and upload it to github current file repository
    git add $1
    git commit -m "init: Upload $1"
    git push
}

function delete(){
    # Delete the whole Repositry localy and online from github
}

function delfile(){
    # Delete One specified file localy and online on github
}