import csv

import emoji
import nlpaug.augmenter.word as naw
import nltk
import torch
from sentence_transformers import SentenceTransformer
from torch import nn

nltk.download('punkt')
from nltk.tokenize import sent_tokenize

import random
import re
import time

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--output_file', type=str, required=True)
parser.add_argument('--input_file', type=str, required=True)
parser.add_argument('--model_path', type=str, required=True)

args = parser.parse_args()

output_file = args.output_file
input_file = args.input_file
model_path = args.model_path

list2 = [1, 2, 3]
list1 = [1, 2, 3, 4]
counter1 = 0


def remove_all_extra_spaces(string):
    return " ".join(string.split())


pattern = r'\[.*?\]'
model = SentenceTransformer('jeniya/BERTOverflow')
aug_insert = naw.ContextualWordEmbsAug(model_path=model_path, action="insert", aug_max=1)
aug_substitute = naw.ContextualWordEmbsAug(model_path=model_path, action="substitute", aug_max=1)
aug_syn = naw.SynonymAug(aug_src='wordnet', aug_max=1)

csv_file = open(output_file, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Id', 'Augmented Comment', 'Anger', 'Love', 'Fear', 'Joy', 'Sadness', 'Surprise'])

from nltk.corpus import wordnet as wn
from nltk.corpus import sentiwordnet as swn

word_syns_dict = {}


def get_synonyms(word):
    if word in word_syns_dict.keys():
        return word_syns_dict[word]

    synonyms = set()
    for syn in wn.synsets(word):
        for l in syn.lemmas():
            synonym = l.name().replace("_", " ").replace("-", " ").lower()
            synonym = "".join([char for char in synonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
            synonyms.add(synonym)
    if word in synonyms:
        synonyms.remove(word)
    word_syns_dict[word] = list(synonyms)
    return word_syns_dict[word]


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


sentiment_dict = {}


def get_sentiment(word, tag):
    if (word, tag) in sentiment_dict.keys():
        return sentiment_dict[(word, tag)]

    wn_tag = penn_to_wn(tag)
    if wn_tag not in (wn.NOUN, wn.ADJ, wn.ADV, wn.VERB):
        return []

    synsets = wn.synsets(word)
    if not synsets:
        return []

    synset = synsets[0]
    swn_synset = swn.senti_synset(synset.name(), 'breakdown.n.03')
    sentiment_dict[(word, tag)] = [swn_synset.pos_score(), swn_synset.neg_score(), swn_synset._obj_score]
    return sentiment_dict[(word, tag)]


def get_senti_score(word):
    pos_val = nltk.pos_tag([word])
    for (x, y) in pos_val:
        return get_sentiment(x, y)
    return []


def syn_replace_word(augmented_text):
    words_aug = augmented_text.split()
    pos_val = nltk.pos_tag(words_aug)
    polar_words = []
    for (x, y) in pos_val:
        senti_score = get_sentiment(x, y)
        if len(senti_score) == 0:
            continue
        if senti_score[0] > 0 or senti_score[1] > 0:
            polar_words.append(x)
    if len(polar_words) == 0:
        return augmented_text
    counter = 3
    ret_text = ''
    while counter > 0:
        counter = counter - 1
        random_word = random.choice(polar_words)

        syns = get_synonyms(random_word)
        if len(syns) < 1:
            continue
        ret_text = ''
        for word in words_aug:
            if word == random_word:
                ret_text = ret_text + ' ' + random.choice(syns)
            else:
                ret_text = ret_text + ' ' + word
        break
    if ret_text == '':
        ret_text = augmented_text
    return ret_text


def delete_word(augmented_text):
    words_aug = augmented_text.split()
    pos_val = nltk.pos_tag(words_aug)
    neutral_words = []
    for (x, y) in pos_val:
        senti_score = get_sentiment(x, y)
        if len(senti_score) == 0:
            continue
        if senti_score[2] == 1.0:
            neutral_words.append(x)
    if len(neutral_words) == 0:
        return augmented_text
    random_word = random.choice(neutral_words)
    ret_text = ''
    for word in words_aug:
        if word == random_word:
            continue
        ret_text = ret_text + ' ' + word
    return ret_text


def replace_with_neutral_check(original_text, augmented_text):
    word_list = original_text.split()
    for word in augmented_text.split():
        if word not in word_list:
            pos_val = nltk.pos_tag([word])
            for (x, y) in pos_val:
                senti_score = get_sentiment(x, y)
                if len(senti_score) < 1:
                    continue
                if senti_score[2] == 1.0:
                    return True
    return False


def sentences_count(text):
    number_of_sentences = sent_tokenize(text)
    return len(number_of_sentences)


def shuffle_sentences(text):
    sentences = sent_tokenize(text)
    random.shuffle(sentences)
    text = ''
    for sentence in sentences:
        text = text + " " + str(sentence) + " "
    return text


with open(input_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    flag_c = False
    for row in csv_reader:

        start = time.time()
        augments = []
        sentence = row[6]
        sentence = emoji.demojize(sentence, delimiters=("", ""))
        sentence = re.sub(pattern, ' ', sentence)
        sentence = remove_all_extra_spaces(sentence)
        sentence = sentence.strip()
        augments.append(sentence)
        write_row = [row[2], sentence, row[7], row[8], row[9], row[10], row[11], row[12]]
        csv_writer.writerow(write_row)

        cos = nn.CosineSimilarity(dim=0, eps=1e-6)
        embedding_org = model.encode(sentence)
        embedding_org = torch.FloatTensor(embedding_org)

        counter = 0

        if sentences_count(sentence) > 1:
            augmented_text = shuffle_sentences(sentence)
            print(augmented_text)
            write_row = [row[2], augmented_text, row[7], row[8], row[9], row[10], row[11], row[12]]
            csv_writer.writerow(write_row)
            counter = 1

        tmp = int(row[7]) + int(row[8]) + int(row[9]) + int(row[10]) + int(row[11]) + int(row[12])

        positive_words = 0
        negative_words = 0
        for word in sentence.split():
            senti_score = get_senti_score(word)
            if len(senti_score) > 0:
                if senti_score[0] > 0:
                    positive_words = positive_words + 1
                if senti_score[1] > 0:
                    negative_words = negative_words + 1

        max_try = 0
        len_sen = len(sentence.split())
        k = int(len_sen * 2 / 10)
        if k < 2:
            k = 2

        while counter < 10:
            if max_try >= 10:
                break
            max_try = max_try + 1
            augmented_text = sentence
            for operations in range(k):
                choice_1 = random.choice(list2)

                if choice_1 == 1:
                    augmented_text = aug_substitute.augment(augmented_text)
                elif choice_1 == 2:
                    augmented_text = aug_insert.augment(augmented_text)
                elif choice_1 == 3:
                    choice_1 = random.choice(list1)
                    if choice_1 % 2 == 1:
                        augmented_text = aug_substitute.augment(augmented_text)
                    else:
                        augmented_text = aug_insert.augment(augmented_text)
                else:
                    # delete neutral word
                    augmented_text1 = delete_word(augmented_text)
                    if augmented_text1 == augmented_text:
                        # insert a word if no neutral word is there
                        augmented_text = aug_insert.augment(augmented_text)
                    else:
                        augmented_text = augmented_text1
            augmented_text = remove_all_extra_spaces(augmented_text)
            augmented_text = augmented_text.strip()
            if augmented_text in augments:
                continue

            positive_words_aug = 0
            negative_words_aug = 0
            for word in augmented_text.split():
                senti_score = get_senti_score(word)
                if len(senti_score) > 0:
                    if senti_score[0] > 0:
                        positive_words_aug = positive_words_aug + 1
                    if senti_score[1] > 0:
                        negative_words_aug = negative_words_aug + 1
            if tmp > 0:
                if row[8] == '1' or row[10] == '1':
                    if positive_words_aug <= positive_words:
                        continue
                if row[7] == '1' or row[9] == '1' or row[11] == '1':
                    if negative_words_aug <= negative_words:
                        continue
                if row[12] == '1':
                    if not (positive_words_aug == positive_words and negative_words_aug == negative_words):
                        continue

            embedding_aug = model.encode(augmented_text)
            out = cos(embedding_org, torch.FloatTensor(embedding_aug))
            if out >= 0.9:
                augments.append(augmented_text)
                write_row = [row[2], augmented_text, row[7], row[8], row[9], row[10], row[11], row[12]]
                csv_writer.writerow(write_row)
                counter = counter + 1
                counter1 = counter1 + 1
                max_try = 0
                print(counter1, augmented_text)
        end = time.time()
        print(end - start)
csv_file.close()
