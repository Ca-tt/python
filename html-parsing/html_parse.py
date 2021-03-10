from bs4 import BeautifulSoup
import urllib.request

file = open('../txt/parsed.txt', 'w')
url = 'https://www.babypips.com/learn/forex'

# send GET request, get html content from given url
with urllib.request.urlopen(url) as request:
    soup = BeautifulSoup(request, 'html.parser')

# grab all links
links = soup('a')

# create a new html doc
doc = BeautifulSoup("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Links</title>
</head>
<body>
</body>
</html>
""", 'html.parser')

# insert parsed links into new html doc <body> tag
doc.body.extend(links)
result = doc.prettify()
# write a result to a file: get new .html file
file.write(result)