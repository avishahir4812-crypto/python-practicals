titles = ["3 Idiots", "Dangal", "Chhichhore"]
genres = ["Comedy", "Sports", "Drama"]
ratings = [8.4, 8.3, 8.0]

movies = []

for title, genre, rating in zip(titles, genres, ratings):
    movie = {
        "title": title,
        "genre": genre,
        "rating": rating
    }

    movies.append(movie)

print(movies)