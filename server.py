import os

from flask import Flask, render_template, url_for
from data import db_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'first_project_by_KA'


@app.route('/')
@app.route('/main', methods=['GET'])
def main():
    list_images_flexible_stone = ['kgs02.png', 'kgs06.png', 'kmk04.png', 'knt03.png']
    list_images_thermal_panels = ['tgs04.png', 'tmk02.png', 'tmk05.png', 'tnt01.png']
    return render_template('main.html',
                           list_images_flexible_stone=list_images_flexible_stone,
                           list_images_thermal_panels=list_images_thermal_panels,
                           title='Главная страница')


@app.route('/catalog_flexible_stone', methods=['GET'])
def catalog_flexible_stone():
    list_images_flexible_stone = [file for file in os.listdir('static/img/catalog_flexible_stone')]
    return render_template('catalog_flexible_stone.html', list_images_flexible_stone=list_images_flexible_stone,
                           title='Каталог Гибкого камня')


@app.route('/catalog_thermal_panels', methods=['GET'])
def catalog_thermal_panels():
    list_images_thermal_panels = [file for file in os.listdir('static/img/catalog_thermal_panels')]
    return render_template('catalog_thermal_panels.html', list_images_thermal_panels=list_images_thermal_panels,
                           title='Каталог Термопанелей')


@app.route('/certificates', methods=['GET'])
def certificates():
    list_certificates = [file for file in os.listdir('static/img/certificates')]
    return render_template('certificates.html', list_certificates=list_certificates,
                           title='Сертификаты')


if __name__ == '__main__':
    db_session.global_init(f'db/novak-decor.db')
    app.run(port=8080, host='127.0.0.1')