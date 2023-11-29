#!/bin/bash

# creat a file to test with
echo "this is my test file" > test1.txt


# Change permissions for the file
echo "Give our test file all the permissions"
chmod 777 test1.txt

# -R= recersef anything in directory will inherit permissions 
# chmod -R