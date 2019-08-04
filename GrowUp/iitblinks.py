import requests
from bs4 import BeautifulSoup
import urllib3
from iitgdate import getDate
from iitgtitle import getTitle


def get_links(url):
    try :
        urllib3.disable_warnings()
        response = requests.get(url,verify=False)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        links = []
        listIntern = []

        for link in soup.find_all('a'):
            link_url = link.get('href')
            if link_url is not None and link_url.startswith('http'):
                '''if link_url.find("internship")!=-1:
                    listIntern.append(link_url)
                else:'''

                links.append(link_url)

    except Exception :
        pass

    return links
def get_net_liks(url):
    try :
        urllib3.disable_warnings()
        response = requests.get(url,verify=False)
        data = response.text
        soup = BeautifulSoup(data, 'lxml')

        links = []

        for link in soup.find_all('a'):
            link_url = link.get('href')
            if link_url is not None and link_url.startswith('http'):
                if link_url.find("summer")!=-1:
                    links.append(link_url)
    except Exception as e :
        pass

    return links
get_links('https://www.it.iitb.ac.in/')