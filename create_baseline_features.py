import sys
from os import listdir
from hw3_corpus_tool import get_utterances_from_file, get_utterances_from_filename

__author__ = 'Frank'


def convert_csv_into_format(path_to_file):
    file = open(path_to_file)
    output = get_utterances_from_file(file)
    first_utterance_has_past = False
    previous_speaker = ''
    for line in output:
        print(line[0], end='\t')

        if not first_utterance_has_past:
            first_utterance_has_past = True
            print('__FIRST_UTTERANCE__')

        pos_tag = line[2]

        if pos_tag:
            for i in range(0, len(pos_tag)):
                print('w[' + str(i) + ']=' + pos_tag[i][0] + '\tpos[' + str(i) + ']=' + pos_tag[i][1], end='\t')
        if previous_speaker != line[1]:
            # the speaker of the current utterance has changed
            if previous_speaker != '':
                print('__SPEAKER_CHANGED__', end='\t')
        print('\n')
        previous_speaker = line[1]


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
        convert_csv_into_format(sys.argv[1])

if __name__ == '__main__':
    main()
