#!/bin/bash
echo 'creating baseline features & spliting 75% of data'

python3 main.py convert ./data/train/ > train.crfsuite.txt

python3 main.py split train.crfsuite.txt 75