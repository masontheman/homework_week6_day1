from app import app
from flask import render_template
from flask import url_for
@app.route("/masonssports")
def hello_world():
    fav_football_players = {
        'Joe Burroww':'https://www.nfl.com/players/joe-burrow/',
        'Damar Hamlin':'https://www.nfl.com/players/damar-hamlin/',
        'Isiah Buggs':'https://www.nfl.com/players/isaiah-buggs-x8875/',
        'Tyreek \'Reek\' Hill':'https://www.nfl.com/players/tyreek-hill/',
        'Justin Herbert':'https://www.nfl.com/players/justin-herbert/',
    }
    images_of_players = ['./images/Joe Burrow.jpg',
    './images/Damar hamlin.jpg',
    './images/isiah Buiggs.jpg',
    './images/tyreek hill.jpg',
    './images/Justin Herbert hrowing.jpeg']
    img=[url_for('static', filename='JoeBurrow.jpg'),url_for('static', filename='Damarhamlin.jpg'),
    url_for('static', filename='isiahBuiggs.jpg'),url_for('static', filename='tyreekhill.jpg'),
    url_for('static', filename='jh.jpg')]
    xx = 'http://127.0.0.1:5000/'
    return (render_template('index.html',fff = fav_football_players,iop = images_of_players,i = img,link = xx))
@app.route("/")
def HomePage():
    x = 'http://127.0.0.1:5000/masonssports'
    yy = url_for('static', filename='IMG_1729.jpg')
    return (render_template('homepage.html',linkk=x,ii=yy))
