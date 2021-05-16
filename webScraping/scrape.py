import requests
import bs4

link = input("Paste link: ")

res = requests.get(link)
soup = bs4.BeautifulSoup(res.text, 'lxml')

test = soup.select('div div p')

for i in range(0, len(test)):
    print(test[i].getText())