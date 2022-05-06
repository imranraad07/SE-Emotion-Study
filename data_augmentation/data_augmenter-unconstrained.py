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
list1 = [1, 2]


def remove_all_extra_spaces(string):
    return " ".join(string.split())


pattern = r'\[.*?\]'
model = SentenceTransformer('jeniya/BERTOverflow')
aug_insert = naw.ContextualWordEmbsAug(model_path=model_path, action="insert", aug_max=1)
aug_substitute = naw.ContextualWordEmbsAug(model_path=model_path, action="substitute", aug_max=1)

csv_file = open(output_file, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Id', 'Augmented Comment', 'Anger', 'Love', 'Fear', 'Joy', 'Sadness', 'Surprise'])


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

        max_try = 0
        while counter < 10:
            if max_try >= 1000:
                break
            try:
                max_try = max_try + 1
                k = int(len(sentence.split() * 2) / 10)
                if k < 2:
                    k = 2

                augmented_text = sentence
                for operations in range(k):
                    choice_1 = random.choice(list2)
                    if choice_1 == 1:
                        augmented_text = aug_insert.augment(augmented_text)
                    elif choice_1 == 2:
                        augmented_text = aug_substitute.augment(augmented_text)
                    elif choice_1 == 3:
                        choice_1 = random.choice(list1)
                        if choice_1 == 2:
                            words = augmented_text.split()
                            num1 = random.randint(0, len(words))
                            augmented_text = ""
                            idx = 0
                            for word in words:
                                if idx == num1:
                                    continue
                                augmented_text = augmented_text + " " + str(word) + " "
                        else:
                            choice_1 = random.choice(list1)
                            if choice_1 == 1:
                                augmented_text = aug_insert.augment(augmented_text)
                            elif choice_1 == 2:
                                augmented_text = aug_substitute.augment(augmented_text)

                augmented_text = remove_all_extra_spaces(augmented_text)
                augmented_text = augmented_text.strip()
                if augmented_text in augments:
                    continue

                embedding_aug = model.encode(augmented_text)
                out = cos(embedding_org, torch.FloatTensor(embedding_aug))
                if out >= 0.9:
                    augments.append(augmented_text)
                    print(augmented_text)
                    write_row = [row[2], augmented_text, row[7], row[8], row[9], row[10], row[11], row[12]]
                    csv_writer.writerow(write_row)
                    counter = counter + 1
            except Exception as e:
                print("Exception occurred", e)
        end = time.time()
        print(end - start)
csv_file.close()
