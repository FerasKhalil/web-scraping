import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/wiki/History_of_Mexico'

def get_citations_needed_count(url):

    texts = requests.get(url)

    # with open("file.html",'w') as file:
    #     file.write(texts)    

    soup = BeautifulSoup(texts.content,'html.parser')
    a_result = soup.findAll('a',title='Wikipedia:Citation needed')
    return len(a_result)


print (get_citations_needed_count(url))

def get_citations_needed_report(url) -> str:
    result_list=''
    texts = requests.get(url).text
    soup = BeautifulSoup(texts,'html.parser')
    parags_result = soup.findAll('p')

    for i in parags_result:
        if i.find('span'):
            result_list+=i.text
            result_list+='\n\n'
    return str(result_list)        
print(get_citations_needed_report(url))

