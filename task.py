import requests
from bs4 import BeautifulSoup

def webscraping():
    li =[]
    l = input("Enter your country:")
    strs = "https://en.wikipedia.org/wiki/"
    url = strs + l
     
    if "wikipedia" in url: 
        try:
            page = requests.get(url)
        except:
            raise Exception("Sorry file not found")
        
        try:
            if page.content != None:
                soup = BeautifulSoup(page.content, 'html.parser')
        except:
            raise Exception("No text found!!!")
        
        text = " "

        #intro:
        intro = soup.find('h1').text
        li.append(intro)    
        for element in soup.select('div'[1]):
            text += element.text
        intros = soup.select('p')[2].text
        li.append(intros)
        
        #History:
        History = soup.select('h2')[2].text
        li.append(History)    
        for element in soup.select('div'[1]):
            text += element.text
        Histories = soup.select('p')[7].text
        li.append(Histories)
        
        #Geography:
        geo = soup.select('h2')[3].text
        li.append(geo) 
        for element in soup.select('div'[1]):
            text += element.text
        geog = soup.select('p')[31].text
        li.append(geog)
        #Culture:
        cult = soup.select('h2')[7].text
        li.append(cult) 
        for element in soup.select('div'[1]):
            text += element.text
        culture = soup.select('p')[72].text
        li.append(culture)
        with open('output.txt', 'w+', encoding='utf-8') as f:
            for items in li:
                f.write('%s\n' %items)
        print("File written successfully")
        
    else:   
       print("Enter wikipedia url!!!")
        
webscraping()

        