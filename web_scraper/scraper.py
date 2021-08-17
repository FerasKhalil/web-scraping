import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url) -> int:

    texts = requests.get(url).text
    with open("file.html",'w') as file:
        file.write(texts)    

    soup = BeautifulSoup(texts,'html.parser')
    li_result = soup.findAll('li')
    return len(li_result)


print(get_citations_needed_count(url))

def get_citations_needed_report(url) -> str:
    result_list=[]
    texts = requests.get(url).text
    soup = BeautifulSoup(texts,'html.parser')
    parags_result = soup.findAll('p')
    for i in parags_result:
        if i.find(title = 'Americas'):
            result_list.append(i)
    return str(result_list)        
print(get_citations_needed_report(url))

