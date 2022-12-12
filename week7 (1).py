import re
import os

try: 
    b = os.listdir(input("enter file path:"))
except Exception as e:
    print(e)
                                                          
def funct(files):
    li =[]
    for i in files: 
        number = re.findall(r'([\d+/]+)\s*[.txt]', i)
        filess = re.findall(r'^[a-zA-Z]*[-][a-zA-Z]*[-][0-9]*[-]',i)
        for j in number:
            no = int(j)
            for w in number:
                    num = str(w)
            for s in filess:
                    filesss = str(s)
            if no % 2 == 0:
                file_name = list(b) + filesss + num + '.txt'
                f = open(file_name, mode='r')
                for k in f :
                    music_geners = re.findall(r'<mus><music>.*?<mus><music>', k)
                    for resultss in music_geners:
                        geners = resultss.split('<mus><music>') 
                        li.append(geners)
            
    return(li)     