import requests
import bs4
request = requests.get('http://quotes.toscrape.com/')
print(request)
soup = bs4.BeautifulSoup(request.text, 'lxml')
print(len(soup))

# GET THE NAME OF ALL AUTHORS
authors_name = set()
authors = soup.select('.author')
for author in authors:
    get_name = author.getText()
    authors_name.add(get_name)

print(authors_name)
for name in authors_name:
    print(name)

# CREATE A LIST OF ALL THE QUOTES

quotes = []
qt = soup.select('.text')
for quote in qt:
    get_quotes = quote.getText()
    quotes.append(get_quotes)
print('\n\n************The list of the all the quotes in first page************/n')
for quote in quotes:
    print(quote)

# LIST A TOOP 10 TAG IN THE RIGHT SIDE OF THE WEBSITE
tag_list = []
tags = soup.select('.tag-item')
for tag in tags:
    get_tag = tag.getText()
    tag_list.append(get_tag)

print('\n\n********** This is all the Top 10 tags in the first page***********\n')
for tag in tag_list:
    print(tag)

url = 'http://quotes.toscrape.com/page/'

authors = set()

for page in range(1, 10):
    url_pages = url + str(page)
    res = requests.get(url_pages)
    soup = bs4.BeautifulSoup(res.text, 'lxml')

    for name in soup.select('.author'):
        authors.add(name.text)

print('\n\n************** This author name are from all pages****************\n')
for author_name in authors:
    print(author_name)
print('\n****** OR *****\n')
page_still_valid = True
page = 1
authors = set()

while page_still_valid:
    page_url = url+str(page)
    res = requests.get(page_url)

    if 'No quotes found!' in res.text:
        break
    soup = bs4.BeautifulSoup(res.text, 'lxml')
    for name in soup.select('.author'):
        authors.add(name.text)
    page = page + 1
for author_name in authors:
    print(author_name)


