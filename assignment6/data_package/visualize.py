import pylab as pl
import numpy as np
from matplotlib.colors import ListedColormap


def plot_model(classifier, X, y, filename):
    """Plot and saves figure with given dataframe and model. 

    Args: 
        classifier (obj): model to use. 
        X (DataFrame): given dataset to use. 
        y (DataFrame): given labels for X. 
        filename (filepath): save filepath
    """
    cmap_light = ListedColormap(['#AAAAFF', '#FFAAAA'])
    cmap_bold = ListedColormap(['#0000FF', '#FF0000'])
    classifier.fit(X, y)

    x_min, x_max = X.iloc[:, 0].min() - .1, X.iloc[:, 0].max() + .1
    y_min, y_max = X.iloc[:, 1].min() - .1, X.iloc[:, 1].max() + .1
    xx, yy = np.meshgrid(np.linspace(x_min, x_max, 100),
                         np.linspace(y_min, y_max, 100))
    Z = classifier.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    pl.show()
    pl.figure()
    pl.pcolormesh(xx, yy, Z, cmap=cmap_light)

    # Plot also the training points
    pl.scatter(X.iloc[:, 0],
               X.iloc[:, 1],
               c=y,
               label='neg',
               cmap=cmap_bold)
    features = list(X.columns.values)

    pl.xlabel(features[0])
    pl.ylabel(features[1])
    pl.axis('tight')
    pl.gca().legend()

    pl.savefig(filename)


if __name__ == '__main__':
    import fitting
    import data

    data_read = data.read_csv("diabetes.csv")

    new_data = data.remove_Nan(data_read)
    new_data = data.diabetes_to_int(new_data, 'diabetes')

    train, test, target_train, target_test = data.split_data(new_data)
    features = ['mass', 'glucose']
    train_data = fitting.training_data(train, features)
    test_data = fitting.training_data(test, features)
    classifiers = fitting.initialize_models()
    trained_model = fitting.fit(
        train_data, target_train, features, classifiers)
    pred, scores = fitting.predict(test_data, target_test, trained_model)

    plot_model(classifiers[1], train_data[features],
               target_train, '../static/images/plot')
