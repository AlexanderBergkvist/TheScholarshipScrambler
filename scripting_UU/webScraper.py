from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import time

LINK_LIST = []
REQUIREMENT_LIST = ["tekn", "information", "uppsala län", "uppland", "natur"]
INDEX = 0
URL_LIST = []

while INDEX < 1000:
    INDEX += 1
    SITE_ADRESS = "http://www.uu.se/hittastipendier/stipendium/?id=" + str(INDEX)
    print(SITE_ADRESS)
    with urlopen(SITE_ADRESS) as start_a:
        soup = bs(start_a, 'html.parser')
        text = soup.get_text().lower()
        if "kan inte hitta stipendium" in text:
            continue
        else:
            try:
                scholarship_requirements = text.split("stipendiekrav")[1].split("kontakt")[0]
                for requirement in REQUIREMENT_LIST:

                    if requirement.lower() in scholarship_requirements:
                        print(requirement + " was here!")
                        result_file = open("result.txt", "a")
                        result_file.write(str(INDEX) + ": " + SITE_ADRESS + "\n")
                        result_file.write(scholarship_requirements + "\n\n")
                        URL_LIST.append(SITE_ADRESS)
            except IndexError:
                print("bad site")
                continue

result_file = open("result.txt", "a")
result_file.write(SITE_ADRESS)
