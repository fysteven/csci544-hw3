#!/bin/bash

echo 'training 75 advanced data & tagging & calculating accuracy'

# ./crfsuite-0.12/bin/crfsuite learn -m my_75.model train.crfsuite.txt_75_training 

./crfsuite-0.12/bin/crfsuite learn -m my_advanced_75.model 75_advanced_training_file

./crfsuite-0.12/bin/crfsuite tag -r -m my_advanced_75.model 75_advanced_dev_file > 75_advanced.out

python3 main.py calculate 75_advanced.out

python3 main.py diff 75_advanced.out > 75_advanced.out.diff