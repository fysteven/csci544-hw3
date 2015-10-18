import sys
from os import listdir
from hw3_corpus_tool import get_utterances_from_file, get_utterances_from_filename

__author__ = 'Frank'


def convert_csv_into_format(path_to_file):
    file = open(path_to_file)
    output = get_utterances_from_file(file)

    for line in output:
        print(line[0], end='\t')
        pos_tag = line[2]

        if pos_tag:
            for i in range(0, len(pos_tag)):
                print('w[' + str(i) + ']=' + pos_tag[i][0] + '\tpos[' + str(i) + ']=' + pos_tag[i][1], end='\t')
        print('\n')


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


def main():
    if len(sys.argv) >= 1:
        function1(sys.argv[1])


main()
