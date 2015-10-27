#!/bin/bash
echo 'creating baseline features & spliting 75% of data'

python3 main.py convert ./data/train/ > train.crfsuite.baseline.txt

python3 main.py split train.crfsuite.baseline.txt 75