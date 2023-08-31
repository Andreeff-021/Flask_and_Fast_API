from flask import Flask, render_template

app = Flask(__name__)


@app.route('/clothes/')
def clothes():
    return render_template('clothes.html')


@app.route('/jackets/')
def jackets():
    jackets_list = [
        {'path_img': '/static/img/jacket_1.jpeg',
         'title': 'Куртка 1',
         'description': 'Женская куртка 1',
         'price': '5000 руб'
         },
        {'path_img': '/static/img/jacket_2.jpeg',
         'title': 'Куртка 2',
         'description': 'Женская куртка 2',
         'price': '5500 руб'
         },
        {'path_img': '/static/img/jacket_3.jpeg',
         'title': 'Куртка 3',
         'description': 'Женская куртка 3',
         'price': '6000 руб'
         }
    ]
    return render_template('jackets.html', jackets_list=jackets_list)


@app.route('/shoes/')
def shoes():
    shoes_list = [
        {'path_img': '/static/img/shoes_1.jpeg',
         'title': 'Обувь 1',
         'description': 'Женская обувь 1',
         'price': '5000 руб'
         },
        {'path_img': '/static/img/shoes_2.jpeg',
         'title': 'Обувь 2',
         'description': 'Женская обувь 2',
         'price': '5500 руб'
         },
        {'path_img': '/static/img/shoes_3.jpeg',
         'title': 'Обувь 3',
         'description': 'Женская обувь 3',
         'price': '6000 руб'
         }
    ]
    return render_template('shoes.html', shoes_list=shoes_list)


if __name__ == '__main__':
    app.run(debug=True)
