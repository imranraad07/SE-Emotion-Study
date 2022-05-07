import csv

from sklearn import metrics

path = 'pred'
y_pred = []
y_true = []

with open(path + '_anger.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

with open(path + '_sad.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

with open(path + '_fear.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))
from sklearn.metrics import recall_score, precision_score, f1_score

with open(path + '_love.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

with open(path + '_joy.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

with open(path + '_surprise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

from sklearn.metrics import classification_report, confusion_matrix

print("All: Precision:", round(precision_score(y_true, y_pred), 3), "Recall:", round(recall_score(y_true, y_pred), 3),
      "F1-score:", round(f1_score(y_true, y_pred), 3))
print(confusion_matrix(y_true, y_pred, labels=[0, 1]))
print(classification_report(y_true, y_pred, digits=3))
print("mcc", round(metrics.matthews_corrcoef(y_true, y_pred), 3))
print("acc", round(metrics.accuracy_score(y_true, y_pred), 3))


