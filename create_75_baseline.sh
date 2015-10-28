#!/bin/bash
echo 'Creating files. 75% for training. 25% for testing. Baseline features.'

# python3 main.py split_directory ./data/train/ 75

python3 main.py create_crf_input baseline split_75_training.txt > 75_baseline_training_file

python3 main.py create_crf_input baseline split_75_dev.txt > 75_baseline_dev_file

