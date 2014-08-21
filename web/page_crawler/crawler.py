from time import sleep
from bs4 import BeautifulSoup
from urllib2 import urlopen
import csv

BASE_URL = "http://www.chicagoreader.com"

def get_category_links(section_url):
    soup = make_soup(section_url)
    boccat = soup.find('dl', 'boccat')
    category_links = [BASE_URL + dd.a['href'] for dd in boccat.findAll('dd')]
    return category_links

def get_category_winner(category_url):
    soup = make_soup(category_url)
    category = soup.find('h1', 'headline').encode_contents().strip()
    winner = [h2.string for h2 in soup.findAll('h2', 'boc1')]
    return {
            'category_url': category_url,
            'category': category,
            'winner': winner,
            }

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html, "lxml")




if __name__ == '__main__':
    food_n_drinks = ("http://www.chicagoreader.com/chicago/"
                    "best-of-chicago-2011-food-drink/BestOf?oid=4106228")


    with open('data/src_food_n_drink.tsv', 'w') as f:
        output = csv.writer(f, delimiter='\t')

        category_links = get_category_links(food_n_drinks)
        for link in category_links:
            data = get_category_winner(link)
            output.writerow(data.values())

    print 'done writing to file'

