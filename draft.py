from bs4 import BeautifulSoup
import urllib.request

file = open('txt/parsed.txt', 'w')

print(file)

with urllib.request.urlopen('https://www.babypips.com/learn/forex') as f:
    result = f.read().decode()
    file.write(result)

print(result)
