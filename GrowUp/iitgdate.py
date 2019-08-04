import requests
from bs4 import BeautifulSoup
import urllib3
import re
from calendar import month_name

def getDate(url):

    try:
        urllib3.disable_warnings()
        n = requests.get(url,verify=False)
        data = n.text
        bs = BeautifulSoup(data, 'lxml')
        Date = bs.body.p
        ImpDate = []


        ImpDate.append(str(Date))

        m = re.findall(r'[0-9]+', ImpDate[0])

        month = [x for x in month_name if x and x in ImpDate[0].title()]
        list=month+m
        list.insert(0,url)

    except Exception as e:
        return None
    return list

#print(getDate('http://www.iitg.ac.in/cse/summerinternship'))