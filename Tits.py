import requests
from bs4 import BeautifulSoup
from random import randint

st_accept = "text/html" # говорим веб-серверу,
                        # что хотим получить html
# имитируем подключение через браузер Mozilla на macOS
st_useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
# формируем хеш заголовков
par = {
   "Accept": st_accept,
   "User-Agent": st_useragent,
}

def tits():
    z = ''
    url = f'https://35photo.pro/tags/%D0%B3%D1%80%D1%83%D0%B4%D1%8C/list_{randint(1, 6)}'
    r = requests.get(url, headers=par)
    # print(r.url)
    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html.parser')
        img = soup.find_all(class_="photos_photo")
        z = img[randint(0, 79)].get("src")
    else:
        z = 200
    return z
