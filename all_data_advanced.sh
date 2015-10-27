#!/bin/bash

echo '100% data / advanced features'

echo 'producing training file'

python3 main.py convert_advanced ./data/train/ > train.crfsuite.advanced.txt

echo 'producing test file'

python3 main.py convert_advanced ./data/test/ > test.crfsuite.advanced.txt

echo 'creating model file'

./crfsuite-0.12/bin/crfsuite learn -m swbdDAMSL.crfsuite.advanced.model train.crfsuite.advanced.txt

echo 'developing on test file using model'

./crfsuite-0.12/bin/crfsuite tag -m swbdDAMSL.crfsuite.advanced.model test.crfsuite.advanced.txt > swbdDAMSL.crfsuite.advanced.out
