import sys
from hw3_corpus_tool import get_utterances_from_file, get_utterances_from_filename

__author__ = 'Frank'


def need_to_filter(pos):
    to_be_filtered = {'UH', ',', 'CC'}
    if pos in to_be_filtered:
        return True
    else:
        return False


def check_statement_opinion(line):

    text = line[3]
    subjective_keywords = {'i think', 'i believe', 'it seems', 'it\'s my opinion that', 'i mean', 'suppose',
                           'of course', 'in my opinion'}

    for word in subjective_keywords:
        if word in text.lower():
            print('__subjective__', end='\t')

    return


def check(length, pos_tag):

    for i in range(0, length):
        if pos_tag[i][0] == 'I' and pos_tag[i][1] == 'PRP':
            for j in range(i + 1, length):
                if pos_tag[j][1] == 'VBP':
                    if pos_tag[j - 1][1] == 'RB':
                        print('__subj__')
                        break
            break

    if pos_tag[length - 1][1] == 'JJ' or pos_tag[length - 2][1] == 'JJ':
        print('__adj_ending_', end='\t')


def is_backchannel_word(word):
    backchannel_words = {'uh-uh', 'uh-huh', 'yes', 'right', 'correct', 'yeah', 'yep', 'uh', 'huh', 'oh', 'um',
                         'really', 'sure'}
    if word.lower() in backchannel_words:
        return True
    else:
        return False


def is_yes_answer_word(word):
    keywords = {'yeah', 'yes', 'uh-huh', 'right', 'correct', 'really', 'exactly', 'sure'}
    if word.lower() in keywords:
        return True
    else:
        return False


def is_no_answer_word(word):
    keywords = {'no', 'nope'}
    if word.lower() in keywords:
        return True
    else:
        return False


def check_questions(pos_tag, length, line):
    if pos_tag[length - 1][0] == '?':
        print('_question_:10', end='\t')
        keywords = {'am', 'is', 'are', 'do', 'does', 'did', 'have', 'has', 'had',
                    'can', 'could', 'may', 'might', 'shall', 'should', 'will', 'would', 'must', 'ought'}
        if pos_tag[0][0].lower() in keywords:
            print('_qy_yes_no_:10', end='\t')
        else:
            open_question_keywords = {'how do you think', 'what do you think', 'how about you', 'what do you feel'
                                      ,'what about yourself', 'what do you', 'what about', 'how about'}
            for keyword in open_question_keywords:
                if keyword in line[3]:
                    print('_qo_open_:7', end='\t')
                    break
        return True
    else:
        return False


def check_abandoned(pos_tag, length, line):
    if length >= 5:
        keywords = {'VBP', 'VBD', 'BES', 'VB'}
        for i in range(0, length):
            if pos_tag[i][1] in keywords:
                return
        print('_%_no_verb_:5', end='\t')
    return


def check_or_clause(pos_tag, length):
    if pos_tag[0][0].lower() == 'or' or length >= 2 and pos_tag[1][0].lower() == 'or':
        print('_qrr_or_clause_:5', end='\t')
    return


def check_repeat_phrase(pos_tag, length, index, output):
    if index != 0:
        if length == len(output[index - 1][2]):
            pass


def check_uninterpretable(pos_tag, length):
    if pos_tag[length - 1][1] == ',':
        if length >= 2 and pos_tag[length - 2][1] == 'XX':
            print('_%_uninterpretable_:7', end='\t')
    return


def create_features(file_name):
    file = open(file_name)
    output = get_utterances_from_file(file)
    first_utterance_has_past = False
    p_previous_speaker = ''
    previous_speaker = ''
    previous_is_question = False

    for index in range(0, len(output)):
        line = output[index]
        print(line[0], end='\t')

        if not first_utterance_has_past:
            first_utterance_has_past = True
            print('_FIRST_UTTERANCE_', end='\t')

        # check_statement_opinion(line)

        pos_tag = line[2]

        if not pos_tag:
            print('_x_one_:15', end='\t')

        if pos_tag:
            length = len(pos_tag)
            # check(length, pos_tag)

            for i in range(0, length):
                # filter some words
                if False:
                    pass
                else:
                    print('w[' + str(i) + ']=' + pos_tag[i][0] + '\tpos[' + str(i) + ']=' + pos_tag[i][1], end='\t')

            if length <= 3 and False:
                pair = pos_tag[length - 1]
                if pair[1] == '.' or pair[1] == ',':
                    if length - 2 >= 0:
                        pair = pos_tag[length - 2]
                if pair[1] == 'PRP' or pair[1] == 'BES' or pair[1] == 'RB' or pair[1] == 'VBP' \
                        or pair[1] == 'UH' and not is_backchannel_word(pair[0]):
                    print('_%_short_\t_%_incomplete_\t_%_no_meaning_', end='\t')

            if length <= 4:
                pair = pos_tag[length - 1]
                if pair[1] == '.' or pair[1] == ',':
                    if length - 2 >= 0:
                        pair = pos_tag[length - 2]

                if is_yes_answer_word(pair[0]) and previous_is_question:
                    print('_ny_yes_:10', end='\t')

                elif is_no_answer_word(pair[0]) and previous_is_question:
                    print('_nn_no_:5', end='\t')

                elif is_no_answer_word(pair[0]) and not previous_is_question:
                    print('_aa_agree_:5', end='\t')

                elif is_yes_answer_word(pair[0]) and not previous_is_question:
                    print('_aa_agree_:6', end='\t')

                elif is_backchannel_word(pair[0]):
                    if not previous_is_question:
                        # backchannel
                        print('_b_this_:4', end='\t')
                        pass

            check_uninterpretable(pos_tag, length)
            check_abandoned(pos_tag, length, line)
            check_or_clause(pos_tag, length)
            # check_repeat_phrase(pos_tag, length, index, output)

            if check_questions(pos_tag, length, line):
                previous_is_question = True
            else:
                previous_is_question = False

        if previous_speaker != line[1]:
            # the speaker of the current utterance has changed
            if previous_speaker != '':
                print('_SPEAKER_CHANGED_', end='\t')
            if p_previous_speaker == line[1] and len(output[index - 1][2]) <= 2:
                # p_p is current, but previous is not current
                print('_+_p_:3', end='\t')

        print('\n')
        previous_speaker = line[1]
        p_previous_speaker = previous_speaker


def main():
    if len(sys.argv) >= 1:
        create_features(sys.argv[1])


if __name__ == '__main__':
    main()
