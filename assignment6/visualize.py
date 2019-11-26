import pylab as pl
import numpy as np
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
    print(X.shape)
    print(y.shape)

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

    pl.savefig('static/test2.png')


if __name__ == '__main__':

    plot_model(classifiers[1], train_data[features], target_train,)
