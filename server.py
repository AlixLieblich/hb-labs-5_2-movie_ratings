"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session, redirect)

from model import connect_to_db

import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')

@app.route('/movies')
def movie_list():
    """View movie list."""
    
    all_movies = crud.get_all_movies()

    return render_template('movie.html',
                            all_movies=all_movies)

@app.route('/movies/<movie_id>')
def movie_detail(movie_id):
    """Show individual movie details."""

    movie_details = crud.get_movie_by_id(movie_id)

    return render_template('movie_details.html',
                            movie=movie_details)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)
