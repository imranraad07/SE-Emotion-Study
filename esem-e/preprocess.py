from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

from Emoticons import EMOTICONS
from Punctuations import remove_punctuation
from WordContractions import CONTRACTION_MAP

wnl = WordNetLemmatizer()
ps = PorterStemmer()

STOPWORDS = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd",
             'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers',
             'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which',
             'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been',
             'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but',
             'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'between', 'into',
             'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on',
             'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how',
             'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so',
             'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd',
             'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn',
             "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',
             "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn',
             "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]


def word_replacement(text):
    utterance = ""
    words = text.split()
    for word in words:
        if word in EMOTICONS.keys():
            utterance = utterance + " " + EMOTICONS[word]
        elif word in CONTRACTION_MAP:
            utterance = utterance + " " + CONTRACTION_MAP[word]
        else:
            word = ps.stem(word)
            utterance = utterance + " " + word
    return utterance


def stopword_removal(text):
    utterance = ""
    words = text.split()
    for word in words:
        if word in STOPWORDS:
            continue
        else:
            utterance = utterance + " " + word
    return utterance


def clear_text(text):
    text = word_replacement(text)
    text = remove_punctuation(text)
    text = " ".join(text.split())
    text = text.strip()
    return text

# txt = "favs catfish i'll ?? !! :D I'm not sure... check after tbr :("
# print(clear_text(txt))
