# import dependencies
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager


chrome_install = ChromeDriverManager().install()
executable_path = {'executable_path': chrome_install}
browser = Browser('chrome', **executable_path, headless=False)

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)
# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title


# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images
# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')

# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url
    
import pandas as pd
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df.to_html()


# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Find and click the full image button
for i in range(0,4):
    full_image_elem = browser.find_by_css('h3')[i]
    full_image_elem.click()
    html = browser.html
    img_soup = soup(html, 'html.parser')
    img_url_rel = img_soup.findAll('a')
    img_url = img_url_rel[3].get('href')
    slide_elem = img_soup.find(class_ = 'title')
    slide_elem = str(slide_elem)
    slide_elem = slide_elem.replace('<h2 class="title">',"")
    slide_elem = slide_elem.replace('</h2>',"")
    img_url = f'https://marshemispheres.com/{img_url}'
    dict_url_pic = {}
    dict_url_pic['img_url'] = img_url
    dict_url_pic['title'] = slide_elem
    hemisphere_image_urls.append(dict_url_pic)
    browser.back()

# # 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# # 5. Quit the browser
browser.quit()

