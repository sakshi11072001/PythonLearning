import re
import os
b = os.listdir("C:/Users/SAKSHI JAIN/pythonLearning/backup2")

def funct(files):
    li =[]
    regx = r'[a-bA-B][_][0-9]{4}[_][0-9]{3}[.txt]'
    for i in files: 
        if regx:
            filess = str(i)[0:13]
            number = str(i)[-7:-3]
            files_even = int(number.replace('.', ''))
            # finding even numbered files
            if files_even % 2 == 0:
                files_even = str(files_even)
                file_name = "C:/Users/SAKSHI JAIN/pythonLearning/backup2/" + filess + files_even + '.txt' 
                f = open(file_name, mode='r')
                for j in f:
                    music_geners = re.findall(r'<mus><music>.*?<mus><music>', j)
                for resultss in music_geners:
                        geners = resultss.split('<mus><music>') 
                        li.append(geners)
                print(li) 
                     #print(resultss)
                                                  
print(funct(b))
