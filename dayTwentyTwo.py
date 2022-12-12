import requests
from bs4 import BeautifulSoup

'''Scrape the presidents table (https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States). 
The table is not very structured and the scrapping may take very long time.'''
url = 'https://en.wikipedia.org/wiki/List_of_presidents_of_the_United_States'
response = requests.get(url)
content = response.content 
soup = BeautifulSoup(content, 'html.parser')
tables = soup.find_all('table')
table = tables[0] 
for td in table.find('tr').find_all('td'):
    print(td.text)


'''Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) '''
url1 = 'https://archive.ics.uci.edu/ml/datasets.php'
response1 = requests.get(url1)
content1 = response1.content 
soup1 = BeautifulSoup(content1, 'html.parser')
tables1 = soup1.find_all('table')
table1 = tables1[0] 
for td in table1.find('tr').find_all('td'):
    print(td.text)
    
    
    
page = requests.get("https://en.wikipedia.org/wiki/Germany")
soup = BeautifulSoup(page.content, 'html.parser')
text = []


intro:
for element in soup.select('div'[1]):
    text.append(element.text)
History = soup.select('p')[2].text
print(History, text)

History:
History = soup.select('h2')[2].text
print(History)    

for element in soup.select('div'[1]):
    text.append(element.text)
History = soup.select('p')[7].text
print(History, text)

Geography:
for element in soup.select('div'[1]):
    text.append(element.text)
History = soup.select('p')[31].text
print(History, text)

Culture:
for element in soup.select('div'[1]):
    text.append(element.text)
History = soup.select('p')[72].text
print(History, text)