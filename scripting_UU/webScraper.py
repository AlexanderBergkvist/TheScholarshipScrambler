from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import time

LINK_LIST = []
REQUIREMENT_LIST = ["tekn", "information", "uppsala län", "uppland", "natur", "dator", "ingenjör", "matte"]
INDEX = 0
URL_LIST = []

def prettify_string(string):
    for i in range(int(len(string) / 60)):
        char = string[(i+1)*60] # Awkward way of indexing from 1 (instead of 0)
        counter = 0
        while char != ' ':
            counter += 1
            char = string[(i+1)*60 + counter]

        string = string[:((i+1)*60) + counter - 1] + "\n" + string[((i+1)*60) + counter + 1:]

    return string

while INDEX < 1000:
    INDEX += 1
    time.sleep(1) # Make sure we aren't ddosing
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
                        result_file.write(prettify_string(scholarship_requirements) + "\n\n")
                        URL_LIST.append(SITE_ADRESS)
            except IndexError:
                print("bad site")
                continue

result_file = open("result.txt", "a")
result_file.write(SITE_ADRESS)
