from flask import Flask, render_template, request

import data.data as data
import data.fitting as fitting
import data.visualize as visualize

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def image():

    features = list(new_data.columns.values)
    features = features[1:9]

    if request.method == 'GET':

        return render_template("web2.html",
                               list_features=features,
                               show_statistics=False)
        # message="accuracy score, test: ",
        # score_test=0,
        # message2="accuracy score, train: ",
        # score_train=0)
    if request.method == 'POST':

        model = request.form.get('classifier')
        selected_features = request.form.getlist('features')
        score1, score2 = main_test(new_data, model, selected_features)
        score1 = (int)(score1*1000)/10
        score2 = (int)(score2*1000)/10

        return render_template("web2.html",
                               list_features=features,
                               selected_features=selected_features,
                               model=model,
                               show_statistics=len(selected_features) > 0,
                               show_image=len(selected_features) == 2,
                               message="accuracy score, test: ",
                               score_test=score1,
                               message2="accuracy score, train: ",
                               score_train=score2)


def main_test(new_data, model, selected_features):
    """test

    Args: 
        new_data (DataFrame): DataFrame
    """
    train, test, target_train, target_test = data.split_data(new_data)

    features = selected_features  # ['mass', 'glucose']
    train_data = fitting.training_data(train, selected_features)
    test_data = fitting.training_data(test, selected_features)
    classifiers = fitting.initialize_model()
    cl = []
    cl.append(classifiers[model])
    trained_model = fitting.fit(
        train_data, target_train, features, cl)

    if len(selected_features) == 2:
        visualize.plot_model(classifiers[model],
                             train_data[features], target_train, 'static/images/plot.png')
    _, score1 = fitting.predict(test_data, target_test, trained_model)
    _, score2 = fitting.predict(train_data, target_train, trained_model)
    return score1, score2


# http://localhost:5000
if __name__ == '__main__':
    data_read = data.read_csv("data/diabetes.csv")

    new_data = data.remove_Nan(data_read)
    new_data = data.diabetes_to_int(new_data, 'diabetes')

    app.run(debug=True)
