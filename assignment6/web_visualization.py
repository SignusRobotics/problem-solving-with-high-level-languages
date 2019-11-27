from flask import Flask, render_template, request, send_file

import data_package.data as data
import data_package.fitting as fitting
import data_package.visualize as visualize

from PIL import Image
import io
import uuid


app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def image():

    features = list(new_data.columns.values)
    features = features[1:9]

    if request.method == 'GET':

        return render_template("web.html",
                               list_features=features,
                               show_statistics=False)

    if request.method == 'POST':

        model = request.form.get('classifier')
        selected_features = request.form.getlist('features')
        score1, score2 = calculate_scores(new_data, model, selected_features)
        score1 = (int)(score1*1000)/10
        score2 = (int)(score2*1000)/10

        return render_template("web.html",
                               list_features=features,
                               selected_features=selected_features,
                               model=model,
                               show_statistics=len(selected_features) > 0,
                               show_image=len(selected_features) == 2,
                               message="accuracy score, test: ",
                               score_test=score1,
                               cache_bust=uuid.uuid4().hex[:6],
                               message2="accuracy score, train: ",
                               score_train=score2)

# inspired by https://stackoverflow.com/a/56948059s
@app.route('/image/<imagename>', methods=['GET'])
def show_image(imagename):
    img = Image.open('static/images/' + imagename)
    file_object = io.BytesIO()
    img.save(file_object, 'PNG')
    file_object.seek(0)
    return send_file(file_object, mimetype='image/png')


def calculate_scores(new_data, model, selected_features):
    """Calculate predicted scores. 

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

    data_read = data.read_csv("data_package/diabetes.csv")

    new_data = data.remove_Nan(data_read)
    new_data = data.diabetes_to_int(new_data, 'diabetes')

    app.run(debug=True)
