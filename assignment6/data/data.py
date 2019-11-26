import pandas as pd
import sklearn
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np


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

    print(dataset[target])

    return dataset


if __name__ == '__main__':
    data = read_csv("diabetes.csv")

    new_data = remove_Nan(data)
    new_data = diabetes_to_int(new_data, 'diabetes')

    # print(type(data))

    print(new_data.head())
    train, test, target_train, target_test = split_data(new_data)

    feature_plot(train, target_train, 'mass', 'glucose')
