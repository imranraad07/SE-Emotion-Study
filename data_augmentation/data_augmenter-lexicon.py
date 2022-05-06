import csv

import nltk
import torch
from nrclex import NRCLex
from sentence_transformers import SentenceTransformer

nltk.download('punkt')
from torch import nn

import random
import time

from nltk.corpus import sentiwordnet as swn

swn.senti_synset('breakdown.n.03')

import pandas as pd
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

filepath = "data/SE_Arousal_Lexicon_Public.csv"
emolex_df = pd.read_csv(filepath, sep=';')
vad_words = emolex_df['Word']

emotion_dict = {}
count = 0
for word in vad_words:
    emotion = NRCLex(word)
    for top_emotion in emotion.top_emotions:
        if top_emotion[1] > 0.0:
            count = count + 1
            print(word, ': ', top_emotion[0])
            if top_emotion[0] not in emotion_dict.keys():
                emotion_dict[top_emotion[0]] = []
            emotion_dict[top_emotion[0]].append(word)
emotion_dict['anger'].extend(emotion_dict['disgust'])

import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--output_file', type=str, required=True)
parser.add_argument('--input_file', type=str, required=True)
parser.add_argument('--model_path', type=str, required=True)
args = parser.parse_args()

output_file = args.output_file
input_file = args.input_file
model_path = args.model_path

csv_file = open(output_file, 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Id', 'Augmented Comment', 'Anger', 'Love', 'Fear', 'Joy', 'Sadness', 'Surprise'])

input_files = [input_file]
model = SentenceTransformer('jeniya/BERTOverflow')

for input_file in input_files:
    counter1 = 0
    total = 0
    with open(input_file) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)
        current_id = '-1'
        current_base_utter = None
        augments = []
        for row in csv_reader:
            start = time.time()
            sentence = row[1]
            if row[0] != current_id:
                current_id = row[0]
                current_base_utter = sentence.split()
                positive_words = 0
                negative_words = 0

            cos = nn.CosineSimilarity(dim=0, eps=1e-6)
            embedding_org = model.encode(sentence)
            embedding_org = torch.FloatTensor(embedding_org)

            if row[2] == '1':
                emotion = 'anger'
            elif row[3] == '1':
                emotion = 'positive'
            elif row[4] == '1':
                emotion = 'fear'
            elif row[5] == '1':
                emotion = 'joy'
            elif row[6] == '1':
                emotion = 'sadness'
            elif row[7] == '1':
                emotion = 'surprise'

            tmp = int(row[2]) + int(row[3]) + int(row[4]) + int(row[5]) + int(row[6]) + int(row[7])
            sentence = row[1]
            augmented_senctence = ''
            if tmp > 0:
                for word in sentence.split():
                    emotion1 = NRCLex(word)
                    if word not in current_base_utter and word not in emotion_dict[emotion] and \
                            emotion1.top_emotions[0][1] > 0.0:
                        augmented_senctence = augmented_senctence + ' ' + random.choice(emotion_dict[emotion])
                        counter1 = counter1 + 1
                    else:
                        augmented_senctence = augmented_senctence + ' ' + word
            else:
                augmented_senctence = sentence
            end = time.time()
            embedding_aug = model.encode(augmented_senctence)
            out = cos(embedding_org, torch.FloatTensor(embedding_aug))
            if out >= 0.9:
                write_row = [row[0], augmented_senctence, row[2], row[3], row[4], row[5], row[6], row[7]]
                csv_writer.writerow(write_row)
csv_file.close()
