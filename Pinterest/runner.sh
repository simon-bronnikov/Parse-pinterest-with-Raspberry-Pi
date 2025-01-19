#!/bin/bash

source ./venv/bin/activate

while true; do
    python3 ./Scripts/parser.py
    fbi -t 15 -a --noverbose --once ./Pictures/*.png
    rm ./Pictures/*.png
done