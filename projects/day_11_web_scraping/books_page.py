import bs4
import requests

base_url = 'https://books.toscrape.com/catalogue/page-{}.html'

page = 1

more_books = True
pages_limit = 100

print("Books with 5 star rating\n")

while more_books:
    page_response = requests.get(base_url.format(page))
    page_soup = bs4.BeautifulSoup(page_response.text, 'lxml')
    books_metadata = page_soup.select('.col-sm-8.col-md-9 form[method="get"].form-horizontal strong')
    total_books = int(books_metadata[0].getText())
    page_books_count = int(books_metadata[2].getText())

    print('Page: ', page)
    page += 1

    books = page_soup.select('.product_pod')

    for book in books:
        if book.select_one('.star-rating.Five'):
            print(f"\t- {book.select_one('h3 a')['title']}")

    print("\n")

    if page_books_count >= total_books or page >= pages_limit:
        more_books = False
