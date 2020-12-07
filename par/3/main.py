import requests
from bs4 import BeautifulSoup
import csv


def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('cmc.csv', 'a') as f:
        writer = csv.write(f)
        pass


def get_page_data(html):
    soup = BeautifulSoup(html, 'lxml')

    trs = soup.find('table').find('tbody').find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        name = tds[2].find('p', class_='sc-1eb5slv-0 iJjGCS').text
        print(name)





def main():
    url = 'https://coinmarketcap.com/'
    get_page_data(get_html(url))


if __name__ == '__main__':
    main()
