from bs4 import BeautifulSoup #import beautifulsoup4
import requests

headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36'}
url = 'https://en.wikipedia.org/wiki/Bruno_Mars'
source_code = requests.get(url, headers=headers, timeout=5)
plain_text = source_code.content #convert into plain text
soup = BeautifulSoup(plain_text,"html.parser") #convert to a bs4 object
name= soup.find('h1',{'id':'firstHeading'})
print('Name:{}'.format(name.get_text()))
