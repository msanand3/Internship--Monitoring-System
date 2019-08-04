import requests
from bs4 import BeautifulSoup
import urllib3
import re
from calendar import month_name
def getDate1(url):
    try:
        urllib3.disable_warnings()
        response = requests.get(url, verify=False)
        data = response.text
        bs1 = BeautifulSoup(data, 'lxml')
        Date = bs1.find_all("b")
        ImpDate = []
        #print(title)

        ImpDate.append(str(Date))
        #print(paragraphs)
        m = re.findall(r'[0-9]+', ImpDate[0])
        #print(m)
        month = [x for x in month_name if x and x in ImpDate[0].title()]
        list=month+m
        print(list)
    except AttributeError as e:
        return None
    return Date

Date = getDate1('https://www.it.iitb.ac.in/summerinternship2019/')