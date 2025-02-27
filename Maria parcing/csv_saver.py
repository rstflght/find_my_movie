import csv
from parcing import array

def return_csv(data):
    with open('movies_new.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['page_url', 'movie_title', 'description', 'image_url', 'movie_year', 'movie_origin', 'movie_alt_title', 'movie_director', 'movie_genres', 'movie_actors', 'same_movies_titles'])  # Заголовки
        writer.writerows(data)  # Данные

return_csv(array())

