from flask import Flask, render_template, url_for
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'first_project_by_KA'


@app.route('/')
@app.route('/main', methods=['GET'])
def main():
    css = url_for('static', filename='css/all.css')
    return render_template('main.html')


if __name__ == '__main__':
    db_session.global_init(f'db/novak-decor.db')
    app.run(port=8080, host='127.0.0.1')