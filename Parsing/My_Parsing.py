import urllib.request
from bs4 import BeautifulSoup 

class Scraper:
    def __init__(self, site):
        self.site=site

    def scrape(self):
        r=urllib.request.urlopen(self.site) #функция urlopen отправляет запрос на сайт и возвращает объект Response, в котором сохранен HTML-код сайта вместе с доп.данными
        html=r.read()                       #функция read возвращает весь HTML-код из объекта Response
        parser="html.parser"
        sp=BeautifulSoup(html, parser)      #объект BeautifulSoup выполняет парсинг (синтаксический анализ) HTML-кода
        for tag in sp.find_all("a"):        #найти в html-коде тег "a"
            url=tag.get("href")             #считать значение, присвоенное "href"
            if url is None:                 
                continue
            else:
                f=open("sitehrefs.txt","a") #открыть для записи/создать файл с расширением .txt для добавления текста в конец файла (-a)
                f.write("\n"+url)           #записать в файл найденные на сайте ссылки 
                f.close()                   #закрыть файл

mysite="https://pypi.org"
Scraper(mysite).scrape()                    #вызвать метод scrape() для объекта mysite класса Scraper
    
