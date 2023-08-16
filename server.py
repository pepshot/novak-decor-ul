import os

from flask import Flask, render_template, url_for
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'first_project_by_KA'


@app.route('/')
@app.route('/main', methods=['GET'])
def main():
    css = url_for('static', filename='css/all.css')
    list_images = ['kgs02.png', 'kgs06.png', 'kmk04.png', 'knt03.png']
    return render_template('main.html', list_images=list_images)


@app.route('/catalog', methods=['GET'])
def catalog():
    css = url_for('static', filename='css/all.css')
    list_images = [file for file in os.listdir('static/img/catalog')]
    return render_template('catalog.html', list_images=list_images)


if __name__ == '__main__':
    db_session.global_init(f'db/novak-decor.db')
    app.run(port=8080, host='127.0.0.1')