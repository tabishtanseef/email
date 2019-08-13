import requests
r = requests.get('http://www.thelearningpoint.net/home/crawledinformation/a-list-of-cbse-schools-in-india/a-list-of-cbse-schools-in-west-bengal')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('tr',attrs={'style':'background-color:#f7f6fb'})
results1 = soup.find_all('tr',attrs={'style':'background-color:#fef4ea'})
a = len(results)
b = len(results1)
print(len(results))
print(len(results1))

i = 0

while i < a:
    one = results[i]
    email = one.contents[3].text
    sub_index = email.find('Website')
    email = one.contents[3].text[6:]
    print(email)
    f = open("guru.txt", "a+")
    f.write(" %s\r\n" % email)
    i += 1

j = 0
while j < b:
    one = results1[j]
    email = one.contents[3].text
    sub_index = email.find('Website')
    email = one.contents[3].text[6:]
    print(email)
    t = open("gur.txt", "a+")
    t.write(" %s\r\n" % email)
    j += 1
