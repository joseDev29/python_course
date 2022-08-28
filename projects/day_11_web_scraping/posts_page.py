import bs4
import requests

posts_page_url = 'https://escueladirecta-blog.blogspot.com/'

posts_page_response = requests.get(posts_page_url)

# print(type(posts_page_response))
# print(posts_page_response.text)

posts_page_soup = bs4.BeautifulSoup(posts_page_response.text, 'lxml')

# print(posts_page_soup)

# print(posts_page_soup.select('title'))  # out: [ Tags ]
# print(posts_page_soup.select('title')[0].getText())
# print(posts_page_soup.select('h1')[0])
# print(posts_page_soup.select('h1')[0].getText())
# print(posts_page_soup.select('h1')[0].select('a')[0].get('href'))
# print(posts_page_soup.select('.header-image-wrapper')[0].select_one('img').get('alt'))

print("Posts: ")

for post in posts_page_soup.select('.blog-posts .post-outer-container'):
    post_title = post.select_one('.post-title.entry-title').select_one('.r-snippetized').getText().strip()
    print(f"\t- {post_title}\n")
