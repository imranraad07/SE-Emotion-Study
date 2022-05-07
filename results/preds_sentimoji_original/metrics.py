import csv

from sklearn import metrics
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import recall_score, precision_score, f1_score

y_true = []
y_pred = []

ids = []

with open('pred_anger.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

print("ANGER: Precision:", round(precision_score(y_true, y_pred), 3), "Recall:", round(recall_score(y_true, y_pred), 3),
      "F1-score:", round(f1_score(y_true, y_pred), 3))
print(confusion_matrix(y_true, y_pred))
print(classification_report(y_true, y_pred, digits=3))
print("mcc", round(metrics.matthews_corrcoef(y_true, y_pred), 3))
print("acc", round(metrics.accuracy_score(y_true, y_pred), 3))

y_true = []
y_pred = []

ids = []

with open('pred_love.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

print("LOVE: Precision:", round(precision_score(y_true, y_pred), 3), "Recall:", round(recall_score(y_true, y_pred), 3),
      "F1-score:", round(f1_score(y_true, y_pred), 3))
print(confusion_matrix(y_true, y_pred))
print(classification_report(y_true, y_pred, digits=3))
print("mcc", round(metrics.matthews_corrcoef(y_true, y_pred), 3))
print("acc", round(metrics.accuracy_score(y_true, y_pred), 3))

y_true = []
y_pred = []

ids = []

with open('pred_joy.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

print("JOY: Precision:", round(precision_score(y_true, y_pred), 3), "Recall:", round(recall_score(y_true, y_pred), 3),
      "F1-score:", round(f1_score(y_true, y_pred), 3))
print(confusion_matrix(y_true, y_pred))
print(classification_report(y_true, y_pred, digits=3))
print("mcc", round(metrics.matthews_corrcoef(y_true, y_pred), 3))
print("acc", round(metrics.accuracy_score(y_true, y_pred), 3))

y_true = []
y_pred = []

ids = []

with open('pred_sad.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

print("SAD: Precision:", round(precision_score(y_true, y_pred), 3), "Recall:", round(recall_score(y_true, y_pred), 3),
      "F1-score:", round(f1_score(y_true, y_pred), 3))
print(confusion_matrix(y_true, y_pred))
print(classification_report(y_true, y_pred, digits=3))
print("mcc", round(metrics.matthews_corrcoef(y_true, y_pred), 3))
print("acc", round(metrics.accuracy_score(y_true, y_pred), 3))

y_true = []
y_pred = []

ids = []

with open('pred_surprise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

print("SURPRISE: Precision:", round(precision_score(y_true, y_pred), 3), "Recall:",
      round(recall_score(y_true, y_pred), 3), "F1-score:", round(f1_score(y_true, y_pred), 3))
print(confusion_matrix(y_true, y_pred))
print(classification_report(y_true, y_pred, digits=3))
print("mcc", round(metrics.matthews_corrcoef(y_true, y_pred), 3))
print("acc", round(metrics.accuracy_score(y_true, y_pred), 3))

y_true = []
y_pred = []

ids = []

with open('pred_fear.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    next(csv_reader)
    for row in csv_reader:
        y_pred.append(int(row[1]))
        y_true.append(int(row[2]))

print("FEAR: Precision:", round(precision_score(y_true, y_pred), 3), "Recall:", round(recall_score(y_true, y_pred), 3),
      "F1-score:", round(f1_score(y_true, y_pred), 3))
print(confusion_matrix(y_true, y_pred))
print(classification_report(y_true, y_pred, digits=3))
print("mcc", round(metrics.matthews_corrcoef(y_true, y_pred), 3))
print("acc", round(metrics.accuracy_score(y_true, y_pred), 3))
