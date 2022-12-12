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
for i in table.find_all('tr')[1:]:
    print(i.find_all('td')[1].text)'
        


'''Extract the table in this url (https://archive.ics.uci.edu/ml/datasets.php) '''
url1 = 'https://archive.ics.uci.edu/ml/datasets.php'
response1 = requests.get(url1)
content1 = response1.content 
soup1 = BeautifulSoup(content1, 'html.parser')
tables1 = soup1.find_all('table')
table1 = tables1[5] 
for i in table1.find_all('tr')[2:]:
    print(i.find_all('td')[1].text)


