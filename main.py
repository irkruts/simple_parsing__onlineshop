import requests
from bs4 import BeautifulSoup
from services.get_url import get_url, headers
from services.writer import json_writer

# dla 1 silki
# name = data.find('h4', class_='card-title').get_text().replace("\n", '') #Short Dress
# price = data.find('h5').get_text() #$24.99
# url_img = "https://scrapingclub.com" + data.find('img', class_="card-img-top img-fluid").get("src") #https://scrapingclub.com/static/img/90008-E.jpg
def simple_parsing():
    for card_url in get_url():
        response = requests.get(card_url, headers=headers)

        soup = BeautifulSoup(response.text, 'lxml')

        data = soup.find('div', class_="card mt-4 my-4")
        name = data.find('h3', class_='card-title').get_text()
        price = data.find('h4').get_text()
        text = data.find('p', class_='card-text').get_text()
        url_img = "https://scrapingclub.com" + data.find('img', class_='card-img-top img-fluid').get('src')

        json_writer(name, price, text, url_img)




if __name__ == '__main__':
    simple_parsing()

