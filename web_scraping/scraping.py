import requests
import bs4 # it is a beautifult soup library and it allow us to grab and easily obtain information

result = requests.get("http://www.example.com")
print(type(result))
print(result.text)

soup = bs4.BeautifulSoup(result.text, "lxml")
print(soup)

# GRABBING A TITLE
print(soup.select('title')[0].getText())
print(soup.select('p'))

# GRABBING A CLASS

result_wiki = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')
soup = bs4.BeautifulSoup(result_wiki.text, "lxml")
print(soup.select('.vector-toc-text'))
for item in soup.select('.vector-toc-text'):
    print(item.getText())

first_item = soup.select('.vector-toc-text')[0]
print(first_item.get_text())

# GRABBING AN IMAGE

result_wiki_image = requests.get('https://en.wikipedia.org/wiki/Tennis')
soup = bs4.BeautifulSoup(result_wiki_image.text, 'lxml')
first_image_item = soup.select('.mw-file-element')
print(first_image_item)
# print(first_image_item['src'])

# working with different pages and items
# GOAL: get a title of every book with a 2 star rating
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'
# print(base_url.format('20'))
# res = requests.get(base_url.format(1))
# soup = bs4.BeautifulSoup(res.text, 'lxml')
# products = soup.select(".product_pod")
# print(len(products))

two_star_titles = []
for n in range(1, 51):
    scrape_url = base_url.format(n)
    res = requests.get(scrape_url)

    soup = bs4.BeautifulSoup(res.text, 'lxml')
    books = soup.select(".product_pod")

    for book in books:
        # if 'star-rating Two' in str(book)
        if len(book.select('.star-rating.Two')) != 0:
            book_title = book.select('a')[1]['title']
            two_star_titles.append(book_title)

print(two_star_titles)