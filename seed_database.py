"""Script to seed database. Pull in movies from json and make users."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb ratings')
os.system('createdb ratings')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/movies.json') as f:
    movie_data = json.loads(f.read())

movies_in_db = []
for movie in movie_data:
    title, overview, release_date, poster_path = (movie['title'],
                                    movie['overview'],
                                    movie['release_date'],
                                    movie['poster_path'])
    # 'release_date': '2019-09-20'
    release_date = datetime.strptime(release_date, '%Y-%m-%d') #its blueee

    movie_object = crud.create_movie(title, 
                                    overview, 
                                    release_date, 
                                    poster_path)
    movies_in_db.append(movie_object)

for n in range(10):
    email = f'user{n}@test.com'
    password = 'test'

    user_object = crud.create_user(email, password)

    for i in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1,5)

        crud.create_rating(score, user_object, random_movie)

