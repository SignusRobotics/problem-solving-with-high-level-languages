import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import BernoulliNB
from sklearn.linear_model import SGDClassifier

from sklearn import metrics


def initialize_models():
    """Initialize models used in this project.

    Returns:
        classifier (obj, list): all classifier object in list.
    """
    classifiers = []

    knn = KNeighborsClassifier(n_neighbors=1)
    classifiers.append(knn)

    logreg = LogisticRegression(
        solver='lbfgs', multi_class='auto', max_iter=200)
    classifiers.append(logreg)

    svm = SVC(gamma='scale')
    classifiers.append(svm)

    BN = BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
    classifiers.append(BN)

    SGD = SGDClassifier(loss="log", penalty="l2", max_iter=5)
    classifiers.append(SGD)

    return classifiers


def initialize_model():
    """Initialize models used in this project.

    Returns:
        classifier_dict (obj, dict): all classifier object in dictionary where key is model name
        and value the classifier object.
    """
    classifier_dict = {}

    knn = KNeighborsClassifier(n_neighbors=1)
    classifier_dict['knn'] = knn

    logreg = LogisticRegression(
        solver='lbfgs', multi_class='auto', max_iter=200)
    classifier_dict['logreg'] = logreg

    svm = SVC(gamma='scale')
    classifier_dict['SVM'] = svm

    BN = BernoulliNB(alpha=1.0, binarize=0.0, class_prior=None, fit_prior=True)
    classifier_dict['BN'] = BN

    SGD = SGDClassifier(loss="hinge", penalty="l2", max_iter=5)
    classifier_dict['SGD'] = SGD

    return classifier_dict


def fit(train_X, train_label, features, classifier):
    """Make a list of evry model trained in train set and given features.

    Args:
        train_X (DataFrame): train set of DataFrame.
        train_label (DataFrame): Labels of train_X.
        features (list, str): list of names of features used in training.
        classifier (list, obj): list of classifier object.

    Returns:
        trained_model (list, obj): list of evry trained model on all classifier in project for given features.
    """
    trained_model = []
    for item in classifier:
        trained_model.append(item.fit(train_X[features], train_label))
    return trained_model


def predict(test_x, test_label, classifier):
    """Predict result for classifier. 

    Args: 
        test_x (DataFrame): Given set of DataFrame to test results. 
        test_label (DataFrame): Labels of given dataset. 
        classifier (list, obj): Model used. 

    Returns: 
        predicted_result (list, int): Prediction for each element in test_x. 
        scores (list, int): Scores for all prediction based on true labels and prediction.  
    """
    predicted_result = []
    scores = []

    for item in classifier:
        predicted = item.predict(test_x)
        predicted_result.append(predicted)
        scores.append(metrics.accuracy_score(test_label, predicted))

    return predicted_result, scores[0]


def training_data(dataset, features):
    """Dataframe with only given features. 

    Args: 
        dataset (DataFrame): given dataframe with all features. 
        features (list, str): List of names of features for new DataFrame. 

    Returns: 
        dataset with only given features. 
    """
    return dataset[features]


if __name__ == '__main__':
    import data

    data_read = data.read_csv("diabetes.csv")

    new_data = data.remove_Nan(data_read)
    new_data = data.diabetes_to_int(new_data, 'diabetes')

    train, test, target_train, target_test = data.split_data(new_data)

    features = ['mass', 'glucose']
    train_data = training_data(train, features)
    test_data = training_data(test, features)
    classifiers = initialize_models()
    trained_model = fit(train_data, target_train, features, classifiers)
    pred, scores = predict(test_data, target_test, trained_model)
    print(scores)
