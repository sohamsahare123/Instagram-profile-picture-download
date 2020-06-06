import requests
from bs4 import BeautifulSoup

username = input("Enter username : ")
URL = 'https://www.instagram.com/{}/'.format(username)

r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')
u = soup.find('meta', property = 'og:image')

url = u.attrs['content']

with open(username+'.jpg','wb') as pic:
    binary = requests.get(url).content
    pic.write(binary)