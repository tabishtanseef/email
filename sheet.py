import requests
r = requests.get('https://docs.google.com/spreadsheets/d/1wwBzbouSsyglO3acoPJj8NCCeORTGWYj8VxG01GZGOg/edit#gid=0')
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.text, 'html.parser')
results = soup.find_all('td')
a = len(results)
print(len(results))

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

