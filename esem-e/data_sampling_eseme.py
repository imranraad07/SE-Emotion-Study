import csv
import random
import re
import emoji
from preprocess import clear_text

input_files = [
    # '../dataset/experiment_dataset/ann-test.csv',
    # '../dataset/experiment_dataset/ann-train.csv',
    '../dataset/Augmented/bart-lexicon.csv',
    # '../dataset/Augmented/bart-polarity.csv',
    # '../dataset/Augmented/bart-unconstrained.csv',
]

import nltk

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn


def penn_to_wn(tag):
    if tag.startswith('J'):
        return wn.ADJ
    elif tag.startswith('N'):
        return wn.NOUN
    elif tag.startswith('R'):
        return wn.ADV
    elif tag.startswith('V'):
        return wn.VERB
    return None


def get_sentiment_words(sentence):
    ret = [sentence]
    return ret


GIT_LOVE = []
GIT_ANGER = []
GIT_SAD = []
GIT_FEAR = []
GIT_JOY = []
GIT_SURPRISE = []

pattern = r'\[.*?\]'


def remove_all_extra_spaces(string):
    return " ".join(string.split())


id_list = []

id = 1
flag = False
for input_file in input_files:
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        next(csv_reader)
        cur_id = -1
        counter = 0
        for row in csv_reader:
            line_count = line_count + 1

            cur = 1
            # row[0] = row[2]


            if row[0] not in id_list:
                id_list.append(row[0])
                print(row[0])

            sentence = row[cur]
            sentence = emoji.demojize(sentence, delimiters=("", ""))
            sentence = re.sub(pattern, ' ', sentence)
            sentence = remove_all_extra_spaces(sentence)
            sentence = clear_text(sentence)
            sentence = sentence.strip()

            sentences = get_sentiment_words(sentence)

            id = id + 1
            # row[0] = row[2]
            # print(row[0])
            for sentence in sentences:
                if row[cur + 1] == '1':
                    GIT_ANGER.append([row[0], sentence, '1'])
                else:
                    GIT_ANGER.append([row[0], sentence, '0'])
                if row[cur + 2] == '1':
                    GIT_LOVE.append([row[0], sentence, '1'])
                else:
                    GIT_LOVE.append([row[0], sentence, '0'])
                if row[cur + 3] == '1':
                    GIT_FEAR.append([row[0], sentence, '1'])
                else:
                    GIT_FEAR.append([row[0], sentence, '0'])
                if row[cur + 4] == '1':
                    GIT_JOY.append([row[0], sentence, '1'])
                else:
                    GIT_JOY.append([row[0], sentence, '0'])
                if row[cur + 5] == '1':
                    GIT_SAD.append([row[0], sentence, '1'])
                else:
                    GIT_SAD.append([row[0], sentence, '0'])
                if row[cur + 6] == '1':
                    GIT_SURPRISE.append([row[0], sentence, '1'])
                else:
                    GIT_SURPRISE.append([row[0], sentence, '0'])
print(len(GIT_ANGER))
print(len(id_list))

with open('dataset/GIT_ANGER_TRAIN-lexicon.tsv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    # random.shuffle(GIT_ANGER)
    csvwriter.writerows(GIT_ANGER)
with open('dataset/GIT_LOVE_TRAIN-lexicon.tsv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    # random.shuffle(GIT_LOVE)
    csvwriter.writerows(GIT_LOVE)
with open('dataset/GIT_FEAR_TRAIN-lexicon.tsv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    # random.shuffle(GIT_FEAR)
    csvwriter.writerows(GIT_FEAR)
with open('dataset/GIT_JOY_TRAIN-lexicon.tsv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    # random.shuffle(GIT_JOY)
    csvwriter.writerows(GIT_JOY)
with open('dataset/GIT_SAD_TRAIN-lexicon.tsv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    # random.shuffle(GIT_SAD)
    csvwriter.writerows(GIT_SAD)
with open('dataset/GIT_SURPRISE_TRAIN-lexicon.tsv', 'w') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter='\t')
    # random.shuffle(GIT_SURPRISE)
    csvwriter.writerows(GIT_SURPRISE)

# with open('dataset/GIT_ANGER_TEST.tsv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter='\t')
#     csvwriter.writerows(GIT_ANGER)
# with open('dataset/GIT_LOVE_TEST.tsv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter='\t')
#     csvwriter.writerows(GIT_LOVE)
# with open('dataset/GIT_FEAR_TEST.tsv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter='\t')
#     csvwriter.writerows(GIT_FEAR)
# with open('dataset/GIT_JOY_TEST.tsv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter='\t')
#     csvwriter.writerows(GIT_JOY)
# with open('dataset/GIT_SAD_TEST.tsv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter='\t')
#     csvwriter.writerows(GIT_SAD)
# with open('dataset/GIT_SURPRISE_TEST.tsv', 'w') as csvfile:
#     csvwriter = csv.writer(csvfile, delimiter='\t')
#     csvwriter.writerows(GIT_SURPRISE)
