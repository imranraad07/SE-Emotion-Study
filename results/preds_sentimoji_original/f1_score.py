import csv

from sklearn import metrics

path = 'pred'
y_pred = []
y_true = []

for i in range(400):
    y_pred.append([])
    y_true.append([])

with open(path + '_anger.tsv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    next(csv_reader)
    idx = 0
    for row in csv_reader:
        if int(row[1]) == 1:
            y_pred[idx].append('anger')
        if int(row[2]) == 1:
            y_true[idx].append('anger')
        idx = idx + 1

with open(path + '_sad.tsv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    next(csv_reader)
    idx = 0
    for row in csv_reader:
        if int(row[1]) == 1:
            y_pred[idx].append('sad')
        if int(row[2]) == 1:
            y_true[idx].append('sad')
        idx = idx + 1

with open(path + '_fear.tsv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    next(csv_reader)
    idx = 0
    for row in csv_reader:
        if int(row[1]) == 1:
            y_pred[idx].append('fear')
        if int(row[2]) == 1:
            y_true[idx].append('fear')
        idx = idx + 1
from sklearn.metrics import recall_score, precision_score, f1_score

with open(path + '_love.tsv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    next(csv_reader)
    idx = 0
    for row in csv_reader:
        if int(row[1]) == 1:
            y_pred[idx].append('love')
        if int(row[2]) == 1:
            y_true[idx].append('love')
        idx = idx + 1

with open(path + '_joy.tsv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    next(csv_reader)
    idx = 0
    for row in csv_reader:
        if int(row[1]) == 1:
            y_pred[idx].append('joy')
        if int(row[2]) == 1:
            y_true[idx].append('joy')
        idx = idx + 1

with open(path + '_surprise.tsv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter='\t')
    next(csv_reader)
    idx = 0
    for row in csv_reader:
        if int(row[1]) == 1:
            y_pred[idx].append('surprise')
        if int(row[2]) == 1:
            y_true[idx].append('surprise')
        idx = idx + 1

from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import MultiLabelBinarizer

mlb = MultiLabelBinarizer()
y_true = mlb.fit_transform(y_true)
y_pred = mlb.fit_transform(y_pred)

# print("All: Precision:", round(precision_score(y_true, y_pred), 3), "Recall:", round(recall_score(y_true, y_pred), 3),
#       "F1-score:", round(f1_score(y_true, y_pred), 3))

# print(confusion_matrix(y_true, y_pred, labels=[0, 1]))
print(classification_report(y_true, y_pred, digits=3))
