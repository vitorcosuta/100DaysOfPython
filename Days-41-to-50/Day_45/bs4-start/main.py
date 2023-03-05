from bs4 import BeautifulSoup
import requests
# from lxml

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, 'html.parser')

article_titles = [span_tag.select_one('a').getText() for span_tag in soup.select('.titleline')]
article_scores = [int(tags.find(name='span', class_='score').getText().split()[0]) for tags in soup.select('.subline')]
article_links = [span_tag.select_one('a').get('href') for span_tag in soup.select('.titleline')]

largest_score = max(article_scores)
largest_index = article_scores.index(largest_score)

print(f'Most popular article: {article_titles[largest_index]} ({largest_score} upvotes)')
print(f'Link: {article_links[largest_index]}')

# with open('website.html', encoding='utf8') as file:
    # Some sites are not going to work with the html parser. In this case, we should use
    # xml parser instead: import lxml module and then replace 'html.parser' with 'xml'.
    # soup = BeautifulSoup(file, 'html.parser')

# print(soup.title)  # HTML tags are referred as attributes of the soup object
# print(soup.title.name)  # We can access a tag's attribute like this

# print(soup.prettify())  # pprint for the html soup

# all_anchor_tags = soup.find_all(name='a')  # .find_all() method returns a list of bs4.element.Tag objects

# for tag in all_anchor_tags:
#     print(tag.getText())  # Gets the name attribute of the tag
#     print(tag.get('href'))

# heading = soup.find(name='h1', id='name')  # .find() method returns a bs4.element.Tag object (the tag itself)
# print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')
# print(section_heading)

# Selects the first element with the specified css selector
# company_url = soup.select_one(selector='p a')
# print(company_url)

# Selects all elements with the specified css selector
# headings = soup.select(".heading")
# print(headings)
