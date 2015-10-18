import sys
import random
from create_baseline_features import convert_csv_into_format
from os import listdir
from hw3_corpus_tool import get_utterances_from_file, get_utterances_from_filename

__author__ = 'Frank'


def get_all_files_in_directory(directory):
    files = []
    for name in listdir(directory):
        if name == '.DS_Store':
            pass
        else:
            files.append(directory + name)
    return files


def function1(directory):
    files = get_all_files_in_directory(directory)

    for file in files:
        convert_csv_into_format(file)


def split_data(input_file_name, percentage):
    input_file = open(input_file_name)
    lines = []
    for line in input_file:
        if line == '\n':
            pass
        else:
            lines.append(line)
    line_count = len(lines)

    training_line_numbers = random.sample(range(0, line_count), int(line_count * float(percentage) / 100))
    training_lines = ''
    dev_lines = ''

    for line in training_line_numbers:
        training_lines += lines[line] + '\n'

    output_training_file = open(input_file_name + '_' + percentage + '_training', 'w')
    output_training_file.write(training_lines)
    output_training_file.close()

    for i in range(0, line_count):
        if i not in training_line_numbers:
            dev_lines += lines[i] + '\n'

    output_dev_file = open(input_file_name + '_' + percentage + '_development', 'w')
    output_dev_file.write(dev_lines)
    output_dev_file.close()


def calculate_accuracy(file_name):
    file = open(file_name)
    count_accurate = 0
    total_line_number = 0
    for line in file:
        if line == '\n':
            pass
        else:
            total_line_number += 1
            words = line.split()
            if words[0] == words[1]:
                count_accurate += 1

    accuracy = count_accurate / total_line_number
    print('Accuracy of file' + file_name + ' is ' + str(accuracy))
    return accuracy


def main():
    if len(sys.argv) == 1:
        program = 'python3 '
        current_script = sys.argv[0]
        print('how to use this program?')
        print(program + current_script + ' convert path_to_a_directory_of_csv_files')
        print(program + current_script + ' split train.crfsuite.txt 75')
        print(program + current_script + ' calculate one_output_file_generated_by_CRFsuite')
    if len(sys.argv) >= 3:
        if sys.argv[1] == 'convert':
            function1(sys.argv[2])
        elif sys.argv[1] == 'calculate':
            calculate_accuracy(sys.argv[2])
    if len(sys.argv) >= 4:
        if sys.argv[1] == 'split':
            split_data(sys.argv[2], sys.argv[3])


main()
