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
        new_data (DataFrame): source without lines containing NaN.s
    """
    new_data = data.dropna()
    return new_data


def split_data(dataset):
    """Split data in test and train set.

    Args:
        dataset (DataFrame): DataFrame to use.

    Returns:
        train ():
        test ():
        target_train ():
        target_test ():
    """
    train, test, target_train, target_test = train_test_split(
        dataset, dataset['diabetes'], train_size=0.8, random_state=42)
    return train, test, target_train, target_test


def feature_plot(dataset, feature_one, feature_two):
    """Scatter plot of target with respect to two features.

    Args:
        dataset (DataFrame): DataFrame to use.
        feature_one (str): name of choosen column one in DataFrame
        feature_two (str): name o column two choosen from DataFrame. 
    """
    plt.scatter(dataset[feature_one], dataset[feature_two],
                c=dataset['diabetes'], cmap=plt.cm.get_cmap('coolwarm', 2))
    plt.show()


def diabetes_to_int(dataset, target):
    """Convert target from string to int values. 

    Args: 
        dataset (DataFrame): DataFrame to use. 
        target (str): name of target column. 

    Returns: 
        dataset (DataFrame): modified dataframe. 
    """
    dataset[target] = np.where(dataset[target] == 'pos', 1, 0)
    return dataset


if __name__ == '__main__':
    data_read = read_csv("diabetes.csv")
    new_data = remove_Nan(data_read)
    new_data = diabetes_to_int(new_data, 'diabetes')
    train, test, target_train, target_test = split_data(new_data)
    feature_plot(train, 'mass', 'glucose')
