import requests
import argparse
from bs4 import BeautifulSoup

def get_html(query):
    response = requests.get("https://wiki.archlinux.org/index.php/{}".format(query))
    return response.text

def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        return soup.find("div", {"class": "mw-parser-output"}).get_text()
    except AttributeError:
        return "There were no results matching the query."

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-q', '--query', help='query')

    args = parser.parse_args()
    query = args.query

    html = get_html(query)
    parsedHtml = parse_html(html)

    print(parsedHtml)
