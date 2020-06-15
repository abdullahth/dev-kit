#!bin/sh
USERNAME = 'abdullahth'
function create(){
    cd 
    cd scripts # You Can Use it or change it with your own desired directory
    echo "Creating Online Repository"
    python create.py $1
    cd 
    cd 'e:\Projects' # You Can Use it or change it with your own desired directory
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
    start cmd
}

function file(){
    # Touch a new file and upload it to github current file repository
    git add $1
    git commit -m "init: Upload $1"
    git push
}

function -his(){
    cd scripts
    py history.py
}

function open(){
    # Open an Existing Repository in vs code
    cd
    cd e:\Projects
    cd $1
    code .
}

function delete(){
    # Delete the whole Repository localy and online from github
}

function delfile(){
    # Delete One specified file localy and online on github
}