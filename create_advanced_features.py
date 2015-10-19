import sys
from hw3_corpus_tool import get_utterances_from_file, get_utterances_from_filename

__author__ = 'Frank'


def need_to_filter(pos):
    to_be_filtered = {'UH', ',', 'CC'}
    if pos in to_be_filtered:
        return True
    else:
        return False


def create_features(file_name):
    file = open(file_name)
    output = get_utterances_from_file(file)
    first_utterance_has_past = False
    previous_speaker = ''
    for line in output:
        print(line[0], end='\t')

        if not first_utterance_has_past:
            first_utterance_has_past = True
            print('__FIRST_UTTERANCE__', end='\t')

        pos_tag = line[2]

        if pos_tag:
            for i in range(0, len(pos_tag)):
                # filter some words
                if need_to_filter(pos_tag[i][1]):
                    pass
                else:
                    print('w[' + str(i) + ']=' + pos_tag[i][0] + '\tpos[' + str(i) + ']=' + pos_tag[i][1], end='\t')
        if previous_speaker != line[1]:
            # the speaker of the current utterance has changed
            if previous_speaker != '':
                print('__SPEAKER_CHANGED__', end='\t')
        print('\n')
        previous_speaker = line[1]


def main():
    if len(sys.argv) >= 1:
        create_features(sys.argv[1])


if __name__ == '__main__':
    main()
