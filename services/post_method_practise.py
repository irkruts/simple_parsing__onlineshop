from requests import Session
from bs4 import BeautifulSoup
from time import sleep
from fake_useragent import UserAgent

ua = UserAgent()

headers = {"User-Agent": ua.random}

work = Session()


# work.get("http://quotes.toscrape.com/", headers=headers)
url = "https://quotes.toscrape.com/login"

response = work.get(url, headers=headers)

soup = BeautifulSoup(response.text, "lxml")

token = soup.find('form').find('input').get('value')
# print(token)
data = {"csrf_token": token, "username": "noname", "password": "password"}

result = work.post(url, headers=headers, data=data, allow_redirects=True)
# print(result)
# print(result.text)

result1 = soup.find_all('span', class_='text')
author = soup.find_all("small", class_='author')

print(result1)

