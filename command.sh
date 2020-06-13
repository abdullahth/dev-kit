#!bin/sh

DIR = 'e:\Projects'
USERNAME = 'abdullahth' # Change this to your own username

function create(){
    cd 
    cd $DIR
    echo "Creating Online Repository"
    py create.py
    git clone https://github.com/$USERNAME/$1.git
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