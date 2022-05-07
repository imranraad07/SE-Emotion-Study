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

# All: Precision: 0.706 Recall: 0.301 F1-score: 0.422
# [[1996   45]
#  [ 251  108]]
#               precision    recall  f1-score   support
#
#            0      0.888     0.978     0.931      2041
#            1      0.706     0.301     0.422       359
#
#     accuracy                          0.877      2400
#    macro avg      0.797     0.639     0.676      2400
# weighted avg      0.861     0.877     0.855      2400
#
# mcc 0.407
# acc 0.877
