import requests
from bs4 import BeautifulSoup
import urllib3
import re
def getTitle(url):
    try:
        urllib3.disable_warnings()
        html = requests.get(url, verify=False)
        data = html.text
        bs = BeautifulSoup(data, 'lxml')
        title = bs.title.string

    except Exception:
        return None
    return title
