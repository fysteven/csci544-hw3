import sys
import random
from create_baseline_features import convert_csv_into_format
from create_advanced_features import create_features
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


def function2(directory):
    files = get_all_files_in_directory(directory)

    for file in files:
        create_features(file)

    return


def function3_baseline(file):
    training = open(file)
    files_to_open_for_training = []
    for line in training:
        words = line.split()
        files_to_open_for_training.append(words[0])
    training.close()

    for file in files_to_open_for_training:
        convert_csv_into_format(file)
    return


def function4_advanced(file):
    training = open(file)
    files_to_open_for_training = []
    for line in training:
        words = line.split()
        files_to_open_for_training.append(words[0])
    training.close()

    for file in files_to_open_for_training:
        create_features(file)
    return


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


def split_data2(input_file_name, percentage):
    input_file = open(input_file_name)
    lines = []
    for line in input_file:
        if line == '\n':
            pass
        else:
            lines.append(line)
    line_count = len(lines)

    training_line_numbers = random.sample(range(0, line_count), int(line_count * float(percentage) / 100))
    set_training_line_numbers = set(training_line_numbers)
    set_dev_line_numbers = {i for i in range(0, line_count)} - set_training_line_numbers
    training_lines = ''
    dev_lines = ''

    for line in training_line_numbers:
        training_lines += lines[line] + '\n'

    output_training_file = open(input_file_name + '_' + percentage + '_training', 'w')
    output_training_file.write(training_lines)
    output_training_file.close()

    for line in set_dev_line_numbers:
        dev_lines += lines[line] + '\n'

    output_dev_file = open(input_file_name + '_' + percentage + '_development', 'w')
    output_dev_file.write(dev_lines)
    output_dev_file.close()


def split_files_in_directory(path, percentage):
    files = get_all_files_in_directory(path)
    number_of_files = len(files)
    indices_training_files = random.sample(range(0, number_of_files), int(number_of_files * float(percentage) / 100))
    set_index_training_files = set(indices_training_files)
    set_index_dev_files = {i for i in range(0, number_of_files)} - set_index_training_files

    training = ''
    dev = ''
    for line in indices_training_files:
        training += files[line] + '\n'

    for line in set_index_dev_files:
        dev += files[line] + '\n'

    temp_file_training = open('split_' + str(percentage) + '_training.txt', 'w')
    temp_file_training.write(training)
    temp_file_training.close()
    print(temp_file_training.name + ' created.')

    temp_file_dev = open('split_' + str(percentage) + '_dev.txt', 'w')
    temp_file_dev.write(dev)
    temp_file_dev.close()
    print(temp_file_dev.name + ' created.')


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
    print('Accuracy of file ' + file_name + ' is ' + str(accuracy * 100) + '%')
    return accuracy


def show_different_labels(file_name):
    file = open(file_name)
    for line in file:
        if line == '\n':
            pass
        else:
            words = line.split()
            if words[0] != words[1]:
                print(line)
    return


def main():
    if len(sys.argv) == 1:
        program = 'python3 '
        current_script = sys.argv[0]
        print('how to use this program?')
        print(program + current_script + ' convert path_to_a_directory_of_csv_files')
        print(program + current_script + ' convert_advanced path_to_a_directory_of_csv_files')
        print(program + current_script + ' split train.crfsuite.txt 75')
        print(program + current_script + ' split_directory path_to_directory 75')
        print(program + current_script + ' create_crf_input baseline file_name')
        print(program + current_script + ' create_crf_input advanced file_name')
        print(program + current_script + ' calculate one_output_file_generated_by_CRFsuite')
        print(program + current_script + ' diff output_by_CRFsuite')
    if len(sys.argv) >= 3:
        if sys.argv[1] == 'convert':
            function1(sys.argv[2])
        elif sys.argv[1] == 'convert_advanced':
            function2(sys.argv[2])
        elif sys.argv[1] == 'calculate':
            calculate_accuracy(sys.argv[2])
        elif sys.argv[1] == 'diff':
            show_different_labels(sys.argv[2])
    if len(sys.argv) >= 4:
        if sys.argv[1] == 'split':
            split_data2(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == 'split_directory':
            split_files_in_directory(sys.argv[2], sys.argv[3])
        elif sys.argv[1] == 'create_crf_input':
            if sys.argv[2] == 'baseline':
                function3_baseline(sys.argv[3])
            elif sys.argv[2] == 'advanced':
                function4_advanced(sys.argv[3])


main()
