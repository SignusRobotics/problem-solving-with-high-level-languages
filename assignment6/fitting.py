import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, LinearRegression

from sklearn import metrics

import data.data as data


def initialize_models():
    classifiers = []

    knn = KNeighborsClassifier(n_neighbors=1)
    classifiers.append(knn)

    logreg = LogisticRegression(
        solver='lbfgs', multi_class='auto', max_iter=200)
    classifiers.append(logreg)

    svm = SVC(gamma='scale')
    classifiers.append(svm)

    #linreg = LinearRegression()
    # classifiers.append(linreg)

    return classifiers


def fit(train_X, train_label, features, classifier):
    trained_model = []
    for item in classifier:
        trained_model.append(item.fit(train_X[features], train_label))
    return trained_model


def predict(test_x, test_label, classifier):
    predicted_result = []
    scores = []

    for item in classifier:
        predicted = item.predict(test_x)
        predicted_result.append(predicted)
        scores.append(metrics.accuracy_score(test_label, predicted))
    return predicted_result, scores


def accuracy(target_test, target_pred):
    scores = []
    pass


def training_data(dataset, features):
    return dataset[features]


if __name__ == '__main__':
    data_read = data.read_csv("data/diabetes.csv")

    new_data = data.remove_Nan(data_read)
    new_data = data.diabetes_to_int(new_data, 'diabetes')

    train, test, target_train, target_test = data.split_data(new_data)

    # feature_plot(train, target_train, 'mass', 'glucose')

    features = ['mass', 'glucose']
    train_data = training_data(train, features)
    test_data = training_data(test, features)
    classifiers = initialize_models()
    trained_model = fit(train_data, target_train, features, classifiers)
    pred, scores = predict(test_data, target_test, trained_model)
    # print(pred)

    print(scores)
