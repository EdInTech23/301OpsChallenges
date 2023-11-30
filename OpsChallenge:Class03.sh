#!/bin/bash

# Get input from the user - a directory to change permissions for
read -p "what direcroty do you want to change permissions for?" input_dir

# Get permissions that user want to use 
read -p "What permissions do you want to give folder?" input_perm

# Changing permissions
chmod -R $input_perm $input_dir

# Shows the permissions 
ls -al $input_dir
