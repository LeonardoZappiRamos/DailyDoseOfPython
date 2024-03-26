""" Scrapping The Mathematics Wikipedia Page  """

import requests
from bs4 import BeautifulSoup


PAGE_URL = "https://en.wikipedia.org/wiki/Mathematics"

# mw-content-ltr mw-parser-output
if __name__ == "__main__":
    try:
        res = requests.get(PAGE_URL)
        soup = BeautifulSoup(res.text, 'html.parser')
        div = soup.find_all("div", id="mw-content-text")
        p = div[0].select("p")
        intro = '\n'.join([para.text for para in p[0:5]])
        with open('files/text.txt', 'a', encoding='utf-8') as f:
            f.write(intro)
        print("File Created.")
    except Exception as e:
        print("Error: %s", e)