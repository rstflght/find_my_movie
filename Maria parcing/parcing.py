import requests
from bs4 import BeautifulSoup
from time import sleep
import re

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}


def get_url():
    for count in range(137, 570): # проходимся по разным страничкам
        print(f'Страница {count}')
        url = f'https://we.lordfilm15.ru/filmy/page/{count}/' # задаём url с переменной, указывающей на страницу
        response = requests.get(url, headers=headers) # запрашиваем данные со страницы с определёнными данными нашего компьютера
        soup = BeautifulSoup(response.text, 'lxml') # задаём именно html парсер, будет извлекать текст html разметки
        data = soup.find_all('div', class_ = 'th-item') # указываем тег разметки, где лежит необходимая нам информация, и класс, к которой она принадлежит (тоже из разметки)

        for i in data:
            page_url = i.find('a').get('href') # указываем начало ссылки на сайт, с помощью find находим тег, где лежит ссылка на фильм, достаём её из определенного аргумента из разметки с помощью get
            print(f'this is page_url {page_url}')
            yield page_url # возвращаем значение url фильма без записи в какую-то переменную

def array():
    for page_url in get_url():
        response = requests.get(page_url, headers=headers) # проваливаемся в саму ссылку на фильм
        sleep(3) # 3 секунды паузы во избежание блокировки
        soup = BeautifulSoup(response.text, 'lxml') # получаем информацию по html с ссылки на фильм
        data = soup.find('div', class_='content')
        movie_info = data.find('div', class_='flists fx-row')
        if movie_info != None:
            if movie_info.find('span', itemprop='name') != None:
                movie_title = movie_info.find('span', itemprop='name').text
            else:
                movie_title = 'None'
            if movie_info.find('span', itemprop='dateCreated') != None:
                movie_year = movie_info.find('span', itemprop='dateCreated').text
            else:
                movie_year = 'None'
            if movie_info.find('span', itemprop='countryOfOrigin') != None:
                movie_origin = movie_info.find('span', itemprop='countryOfOrigin').text
            else:
                movie_origin = 'None'
            if movie_info.find('span', itemprop='alternativeHeadline') != None:
                movie_alt_title = movie_info.find('span', itemprop='alternativeHeadline').text
            else:
                movie_alt_title = 'None'
            if movie_info.find('span', itemprop='director') != None:
                movie_director = movie_info.find('span', itemprop='director').text
            else:
                movie_director = 'None'
            if movie_info.find('span', itemprop='genre') != None:
                movie_genres = movie_info.find('span', itemprop='genre').text
            else:
                movie_genres = 'None'
            if movie_info.find('span', itemprop='actors') != None:
                movie_actors = movie_info.find('span', itemprop='actors').text
            else:
                movie_actors = 'None'
        else:
            movie_info = 'None'
            movie_title = 'None'
            movie_genres = 'None'
            movie_actors = 'None'
            movie_year = 'None'
            movie_alt_title = 'None'
            movie_origin = 'None'
            movie_director = 'None'
        print(f'title {movie_title}, \nyear {movie_year}, \norigin {movie_origin}, \nalt_title {movie_alt_title}, \ndirector {movie_director}, \ngenres {movie_genres}, \nactors {movie_actors}')
        description_info = data.find('div', class_=re.compile(r'fdesc clearfix(\s+.*)?'))
        if description_info != None:
            description = description_info.find('span', id='descr', itemprop='description').text
        else:
            description = 'None'
        print(f'description {description}')
        if data.find('div', class_='fposter img-wide') != None:
            image_url = 'https://we.lordfilm15.ru/' + data.find('div', class_='fposter img-wide').find('img').get('src')
        else:
            image_url = 'None'
        print(f'image {image_url}')
        same_movies_info = data.find('div', class_='sect-cont sect-items clearfix')
        if same_movies_info != None:
            same_movies = same_movies_info.find_all('div', class_='th-title')
            same_movies_titles = ''
            for i in same_movies:
                same_movies_titles += f', {i.text}'
            same_movies_titles = same_movies_titles.replace(", ", "", 1)
        else:
            same_movies_titles = 'None'
        print(f'same movies: {same_movies_titles}')
        yield (page_url, movie_title, description, image_url, movie_year, movie_origin, movie_alt_title, movie_director, movie_genres, movie_actors, same_movies_titles)
        