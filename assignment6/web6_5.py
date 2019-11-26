from flask import Flask, render_template, request

import data.data as data
import fitting
import visualize

app = Flask(__name__)


@app.route('/')
def image():
    _, score1 = fitting.predict(test_data, target_test, trained_model)
    _, score2 = fitting.predict(train_data, target_train, trained_model)
    features = list(new_data.columns.values)
    features = features[1:9]
    print(features)

    return render_template("web2.html",
                           list_features=features,
                           message="accuracy score, test: ",
                           score_test=score1,
                           message2="accuracy score, train: ",
                           score_train=score2)


@app.route('/user_defined', methods=['POST'])
def submit():
    print(request.form.get('classifier'))
    print(request.form.getlist('features'))
    return request.form.get('classifier')
    # return request.form.getlist('features')


# http://localhost:5000
if __name__ == '__main__':

    data_read = data.read_csv("data/diabetes.csv")

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

    visualize.plot_model(classifiers[1], train_data[features], target_train,)

    app.run(debug=True)
