#!bin/sh
source dataset/vars.sh

function create(){
    cd scripts # You Can Use it or change it with your own desired directory
    python create.py $1
    cd 
    cd "$DIR" # You Can Use it or change it with your own desired directory
    git clone "https://github.com/$USERNAME/$1.git"
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
    clear
    echo "Your Repository($1) Created Successfullly"
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

function delete(){
    # Delete the whole Repository localy and online from github
    cd scripts
    py delete.py $1
}

function delfile(){
    # Delete One specified file localy and online on github
}