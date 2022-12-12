import json
o = open("C:/Users/SAKSHI JAIN/pythonLearning/countries.json", mode = 'r',encoding = 'UTF-8')
def populated(json_file):
    li = []
    data = json.load(json_file)
    for i in range (len(data)):
        dic = dict()
        country = data[i]['name']
        dic['country'] = country
        population = data[i]['population']
        dic['population'] = population
        li.append(dic)
    sorted_list = sorted(li, key=lambda i: i['population'], reverse = True)
    final_list = sorted_list[:10]
    return final_list
     
print(populated(o))
                                                                      