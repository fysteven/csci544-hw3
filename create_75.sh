#!/bin/bash
echo 'creating advanced features & spliting 75% of data'

python3 main.py convert_advanced ./data/train/ > train.crfsuite.advanced.txt

python3 main.py split train.crfsuite.advanced.txt 75