#!/bin/bash

echo '100% data / baseline features'

echo 'producing training file'

python3 main.py convert ./data/train/ > train.crfsuite.baseline.txt

echo 'producing test file'

python3 main.py convert ./data/test/ > test.crfsuite.baseline.txt

echo 'creating model file'

./crfsuite-0.12/bin/crfsuite learn -m swbdDAMSL.crfsuite.baseline.model train.crfsuite.baseline.txt

echo 'developing on test file using model'

./crfsuite-0.12/bin/crfsuite tag -m swbdDAMSL.crfsuite.baseline.model test.crfsuite.baseline.txt > swbdDAMSL.crfsuite.baseline.out
