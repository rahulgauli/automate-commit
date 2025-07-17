#!/bin/bash

read -p "Enter the number of commits to add (1-100): " num_commits
if ! [[ "$num_commits" =~ ^[0-9]+$ ]] || [ "$num_commits" -lt 1 ] || [ "$num_commits" -gt 100 ]; then
    echo "Error: Please enter a valid number between 1 and 100."
    exit 1
fi

for ((i=1; i<=num_commits; i++))
do
    echo "Running python script: iteration $i"
    pipenv install
    pipenv install --dev
    pipenv run python3 -m scripts.main
done
