import requests
from bs4 import BeautifulSoup
import urllib3
from iitgdate import getDate
from iitgtitle import getTitle
from database import MongoConnect


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

def ALLInfo():
    lists=get_links("http://www.iitg.ac.in/")
    title=getTitle('http://www.iitg.ac.in/')
    for list in lists :
        try :
            listset = get_net_liks(list)

            date=getDate(listset[0])


            break

        except Exception as e:
            pass

    dict={'College' : title, 'URL' :date[0], 'Application Last Date' :date[2]+' '+date[1]+' '+date[3]}
    lists=[title,date[0],date[2]+' '+date[1]+' '+date[3]]
    MongoConnect(dict)
    return lists


