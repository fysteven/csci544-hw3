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
            print('_FIRST_UTTERANCE_', end='\t')

        pos_tag = line[2]

        if pos_tag:
            for i in range(0, len(pos_tag)):
                pos = pos_tag[i][1] if pos_tag[i][1] != ':' else '(colon)'
                print('TOKEN_' + pos_tag[i][0] + '\tPOS_' + pos, end='\t')
        if previous_speaker != line[1]:
            # the speaker of the current utterance has changed
            if previous_speaker != '':
                print('_SPEAKER_CHANGED_', end='\t')
        print()
        previous_speaker = line[1]
    print('')


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
