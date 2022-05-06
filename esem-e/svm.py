import csv

import numpy as np
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

emotions = ['ANGER', 'LOVE', 'FEAR', 'JOY', 'SAD', 'SURPRISE']

Y_TOTAL_TRUE = []
Y_TOTAL_PRED = []
for emotion in emotions:
    emotion_train = emotion

    X_train = []
    y_train = []
    with open('dataset/GIT_' + emotion + '_TRAIN-lexicon' + '.tsv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        counter = 0
        prev = ''
        zero_count = 0
        one_count = 0
        for row in csv_reader:
            if row[0] != prev:
                prev = row[0]
                counter = 1
            else:
                counter = counter + 1

            X_train.append(row[1])
            y_train.append(int(row[2]))
            if int(row[2]) == 0:
                zero_count = zero_count + 1
            if int(row[2]) == 1:
                one_count = one_count + 1

    # class_weight = {}
    # class_weight[0] = one_count / (zero_count + one_count)
    # class_weight[1] = zero_count / (zero_count + one_count)

    X_test = []
    y_test = []
    id = []
    with open('dataset/GIT_' + emotion + '_TEST.tsv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        for row in csv_reader:
            X_test.append(row[1])
            y_test.append(int(row[2]))
            id.append(row[0])

    X_train = np.array(X_train)
    X_train = np.array(X_train).ravel()

    X_test = np.array(X_test)
    X_test = np.array(X_test).ravel()
    best_metric = 1
    f1_s = 0.0

    text_clf = Pipeline(
        [('vect', CountVectorizer(ngram_range=(1, 2))), ('clf', LinearSVC(C=best_metric, max_iter=1000000))])
    text_clf.fit(X_train, y_train)
    predicted = text_clf.predict(X_test)

    print(best_metric, len(X_train))
    print(emotion, "Precision:", round(metrics.precision_score(y_test, predicted), 3), "Recall:",
          round(metrics.recall_score(y_test, predicted), 3), "F1-score:", round(metrics.f1_score(y_test, predicted), 3))

    print(metrics.confusion_matrix(y_test, predicted, labels=[0, 1]))
    Y_TOTAL_TRUE.extend(y_test)
    Y_TOTAL_PRED.extend(predicted)

    with open('pred_' + str.lower(emotion) + '.csv', 'w+') as csv_file:
        csvwriter = csv.writer(csv_file)
        csvwriter.writerow(['id', 'predicted', 'Annotated'])
        for i in range(len(y_test)):
            row = [id[i], predicted[i], y_test[i]]
            csvwriter.writerow(row)

print("All Precision:", round(metrics.precision_score(Y_TOTAL_TRUE, Y_TOTAL_PRED), 3), "Recall:",
      round(metrics.recall_score(Y_TOTAL_TRUE, Y_TOTAL_PRED), 3), "F1-score:",
      round(metrics.f1_score(Y_TOTAL_TRUE, Y_TOTAL_PRED), 3))
print(metrics.confusion_matrix(Y_TOTAL_TRUE, Y_TOTAL_PRED, labels=[0, 1]))
