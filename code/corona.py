import requests
from bs4 import BeautifulSoup

URL = 'https://www.worldometers.info/coronavirus'

def corona():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(style="color:#aaa")
    return results.string.split(">")[0]
