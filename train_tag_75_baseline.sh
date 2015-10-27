#!/bin/bash

echo 'training 75 baseline data & tagging & calculating accuracy'

# ./crfsuite-0.12/bin/crfsuite learn -m my_75.model train.crfsuite.txt_75_training 

./crfsuite-0.12/bin/crfsuite learn -m my_75.model 75_baseline_training_file

./crfsuite-0.12/bin/crfsuite tag -r -m my_75.model 75_baseline_dev_file > 75_baseline.out

python3 main.py calculate 75_baseline.out

python3 main.py diff 75_baseline.out > 75_baseline.out.diff