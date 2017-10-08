from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("https://www.ddengle.com")
bsObj = BeautifulSoup(html.read(),"html.parser")
print(bsObj.h1)
