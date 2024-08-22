
import time

import bs4
import requests
from fake_headers import Headers


def get_headers():
    return Headers(os="win", browser="chrome").generate()


response = requests.get("https://spb.hh.ru/search/vacancy", headers=get_headers())
main_html_data = response.text

main_soup = bs4.BeautifulSoup(main_html_data, features="lxml")

tag_div_article_list = main_soup.find("input", class_="bloko-input-text")

# article_tags = tag_div_article_list.find_all('value')
print(tag_div_article_list)
# print(article_tags)

parsed_data = []