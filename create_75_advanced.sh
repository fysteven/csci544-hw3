#!/bin/bash
echo 'Split all the files. 75% for training. 25% for testing. Advanced features.'

# python3 main.py split_directory ./data/train/ 75

python3 main.py create_crf_input advanced split_75_training.txt > 75_advanced_training_file

python3 main.py create_crf_input advanced split_75_dev.txt > 75_advanced_dev_file

