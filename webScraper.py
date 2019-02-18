from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

LINK_LIST = []
REQUIREMENT_LIST1 = []
REQUIREMENT_LIST2 = []

START_ADRESS = "https://www.aftonbladet.se/"

with urlopen(START_ADRESS) as start_a:
    soup = bs(start_a, 'html.parser')
    print(soup.a)
