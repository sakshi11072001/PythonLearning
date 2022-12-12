data = [
    ['Disqualified', 'ed-19453886', 'Rom Dino', 'http://databaseolympics.com/players/playerpage.htm?ilkid=DINOROM01'],
    ['Active', 'ew-52140008', 'Danny Scholansky', 'http://databaseolympics.com/players/playerpage.htm?ilkid=SCHODAN51'],
    ['Active', 'gt-96741850', 'Gonshu Migou', 'http://databaseolympics.com/players/playerpage.htm?ilkid=MIGOGON52'],    
    ['Active', 'ik-36528852', 'Joyin Ok', 'http://databaseolympics.com/players/playerpage.htm?ilkid=OKJOY88'],
    ['On-boarding', 'tg-14050001', 'Curly Carl', 'http://databaseolympics.com/players/playerpage.htm?ilkid=CARLCUR32'],
]
data_1 = data[0]
data_2 = data[1]
data_3 = data[2]
data_4 = data[3]
data_5 = data[4]

http_links =  'https://www.newolympics.eu?'

one_status = data_1[0]
one_identification = data_1[1]
one_oldurl = data_1[3]
ilkid_1 = one_oldurl.partition('ilkid')[-1]
urls_1 = http_links + 'status=' + one_status + '&identifiactor=' + one_identification + '&ilkid' + ilkid_1

two_status = data_2[0]
two_identification = data_2[1]
two_oldurl = data_2[3]
ilkid_2 = two_oldurl . partition('page.')[-1]
urls_2 = http_links + 'status=' + two_status + '&identifiactor=' + two_identification +  '&ilkid' + ilkid_2

three_status = data_3[0]
three_identification = data_3[1]
three_oldurl = data_3[3]
ilkid_3 = three_oldurl . partition('page.')[-1]
urls_3 = http_links + 'status=' + three_status + '&identifiactor=' + three_identification +  '&ilkid' +ilkid_3

four_status = data_4[0]
four_identification = data_4[1]
four_oldurl = data_4[3]
ilkid_4 = four_oldurl . partition('page.')[-1]
urls_4 = http_links + 'status=' + four_status + '&identifiactor=' + four_identification +  '&ilkid' +ilkid_4

five_status = data_5[0]
five_identification = data_5[1]
five_oldurl = data_5[3]
ilkid_5 = five_oldurl . partition('page.')[-1]
urls_5 = http_links + 'status=' + five_status + '&identifiactor=' + five_identification +  '&ilkid' +ilkid_5

print(urls_1)
print(urls_2)
print(urls_3)
print(urls_4)
print(urls_5)
