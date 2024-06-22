import requests
from bs4 import BeautifulSoup
 
def rec(qry) :
    url = f'https://www.google.com/search?q={qry}+recomendations'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    urls = []
    for link in soup.find_all('a'):
        urls.append(link.get('href'))
    return urls