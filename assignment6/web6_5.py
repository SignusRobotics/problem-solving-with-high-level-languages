from flask import Flask, render_template

import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression, LinearRegression

from sklearn import metrics

import pylab as pl
from matplotlib.colors import ListedColormap

# Create color maps for 3-class classification problem, as with iris
cmap_light = ListedColormap(['#AAAAFF', '#FFAAAA'])
cmap_bold = ListedColormap(['#0000FF', '#FF0000'])


def plot_model(classifier, X, y):
    #iris = datasets.load_iris()
    # X = iris.data[:, :2]  # we only take the first two features. We could
                        # avoid this ugly slicing by using a two-dim dataset
    #y = iris.target

    classifier.fit(X, y)
    # print(X.shape)
    # print(y.shape)

    x_min, x_max = X.iloc[:, 0].min() - .1, X.iloc[:, 0].max() + .1
    y_min, y_max = X.iloc[:, 1].min() - .1, X.iloc[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.figure()
    pl.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    pl.scatter(X.iloc[:, 0], X.iloc[:, 1], c=y, cmap=cmap_bold)
    pl.xlabel(features[0])
    pl.ylabel(features[1])
    pl.axis('tight')

    pl.savefig('static/test.png')


def read_csv(filename):
    """Read data from csv file.  

    Args: 
        filename (file, str): name of file to read data. 

    Returns: 
        data 
    """

    data = pd.read_csv(filename)

    return data


def remove_Nan(data):
    """Remove lines containing NaN values in data. 

    Args: 
        data (DataFrame): source of data 

    Returns: 
        new_data (DataFrame): source without lines containing NaN. 

    """
    new_data = data.dropna()
    return new_data


def split_data(dataset):
    # print(dataset['diabetes'])
    #Y = dataset['diabetes']

    train, test, target_train, target_test = train_test_split(
        dataset, dataset['diabetes'], train_size=0.8, random_state=42)
    # print(train.shape)
    # print(test.shape)
    # print(target_train.shape)
    # print(target_test.shape)

    return train, test, target_train, target_test


def dataset_with_2features(feature_one, feature_two, dataset):
    pass
    #    dataframe = pd.DataFrame({feature_one, feature_two: []})


def feature_plot(dataset, target, feature_one, feature_two):
    #data = dataset
    #colors = ('red', 'green')
    #groups = ('pos', 'neg')

    #fig = plt.figure()

    #ax = fig.add_subplot(1, 1, 1, axisbg="1.0")

    # for data, color, group in zip(data, colors, groups):
    #    x, y = data
    #    ax.scatter(x, y, alpha=0.8, c=color,
    #               edgecolors='none', s=30, label=group)

    #plt.title('Matplot scatter plot')
    # plt.legend(loc=2)
    # plt.show()

    plt.scatter(dataset[feature_one], dataset[feature_two],
                c=dataset['diabetes'], cmap=plt.cm.get_cmap('coolwarm', 2))
    #formatter = plt.FuncFormatter(lambda i, *args: iris.target_names[int(i)])
    #plt.colorbar(ticks=[0, 1, 2], format=formatter)

    #plt.clim(-0.5, 2.5)
    # plt.xlabel(dataset[feature_one])
    # plt.ylabel(dataset[feature_two])
    plt.show()


def diabetes_to_int(dataset, target):

    dataset[target] = np.where(dataset[target] == 'pos', 1, 0)
    #dataset[target] = np.where(dataset[target] == 'neg', 0)

    # print(dataset[target])

    return dataset


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


# def fit(dataset, features, classifier):
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
    #train_data = []
    # for item in features:
    #    train_data.append(dataset[item])
        # train_data[item] = dataset[item]
    #df = pd.DataFrame(train_data, columns=features)
    # print(dataset[features])
    # print(dataset[features].shape)
    # print(dataset[features].head())

    # print(df.head)
    # print(df.shape)
    return dataset[features]


app = Flask(__name__)


@app.route('/')
def image():
    _, score1 = predict(test_data, target_test, trained_model)
    _, score2 = predict(train_data, target_train, trained_model)

    return render_template("web2.html",
                           message="accuracy score, test: ",
                           score_test=score1,
                           message2="accuracy score, train: ",
                           score_train=score2)


# http://localhost:5000
if __name__ == '__main__':

    data = read_csv("diabetes.csv")

    new_data = remove_Nan(data)
    new_data = diabetes_to_int(new_data, 'diabetes')

    # print(type(data))

    # print(new_data.head())
    train, test, target_train, target_test = split_data(new_data)

    # feature_plot(train, target_train, 'mass', 'glucose')

    features = ['mass', 'glucose']
    train_data = training_data(train, features)
    test_data = training_data(test, features)

    # classifier = KNeighborsClassifier(n_neighbors=1)
    # print(classifier)
    classifiers = initialize_models()
    # print(classifiers)

    #trained_model = fit(new_data, features, classifiers)
    trained_model = fit(train_data, target_train, features, classifiers)

    # print(trained_model)
    #print(fit(new_data, features, classifier))

    pred, scores = predict(test_data, target_test, trained_model)
    #pred = predict(test_data, target_test, trained_model)
    # print(pred)
    # print(scores)

    plot_model(classifiers[1], train_data[features], target_train)

    app.run(debug=True)
