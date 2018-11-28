from googlesearch import search
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import datefinder

SEARCH_TERM = 'Libya'
NUM_GOOGLE_URLS_TO_SEARCH = 15


for url in search(SEARCH_TERM, stop=NUM_GOOGLE_URLS_TO_SEARCH):
    try:
        print(url)

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html_doc = urlopen(req).read().decode('utf-8')
        soup = BeautifulSoup(html_doc, 'html.parser')

        if soup.time:
            text = soup.get_text()

            matches = datefinder.find_dates(str(soup.time).replace('.', ''))

            date = ''
            for match in matches:
                date = match

            print(date)

    except:
        print('Could not access url')
