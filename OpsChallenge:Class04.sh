#!/bin/bash

while true; do
    # Display the menu
    echo "Menu:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    # Request user input
    read -p "Enter your choice (1-4): " choice

    # Evaluate user input using a conditional statement
    case $choice in
        1)
            echo "Hello world!"
            ;;
        2)
            ping -c 4 127.0.0.1
            ;;
        3)
            ifconfig
            ;;
        4)
            echo "Exiting the program. Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid choice. Please enter a number between 1 and 4."
            ;;
    esac

    # Add a newline for better readability
    echo

done