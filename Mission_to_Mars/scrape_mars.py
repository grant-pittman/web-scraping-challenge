#importing libraries
from splinter import Browser
from bs4 import BeautifulSoup as bs
import time
import pandas as pd

#defining a funciton to use splinter and the chromedriver
def init_browser():
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

#defining scrape function which will be imported into my app
def scrape():
    browser = init_browser()   
    
    #visitimg the first website to scrape, this process will be repeated
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(1)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    #scraping the news title and the news content and storing them in variables that I will reference later
    news_title = soup.find("div",class_="content_title").text
    news_p = soup.find("div", class_="article_teaser_body").text
    
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)
    time.sleep(1)
    
    html = browser.html
    soup = bs(html, "html.parser")
    
    featured_image_url  = soup.find('article')['style'].replace('background-image: url(','').replace(');', '')[1:-1]
    base_url = 'https://www.jpl.nasa.gov'
    featured_img = base_url + featured_image_url
    
    
    #I had the below section working a few days ago, but now when I try and scrape Twitter, I am getting errors
    #ommiting this section for now so I can turn in the assignment, will revisit later
    
    ##url = 'https://twitter.com/marswxreport?lang=en'
    ##browser.visit(url)
    ##time.sleep(1)

    ##html = browser.html
    ##soup = bs(html, "html.parser")
    
    ##tweet_search = soup.find_all('article')
    ##mars_weather=tweet_search[0].find_all('span')[4].text
    
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    
    df = tables[0]
    df.columns = ['Description','Value']
    df.set_index('Description', inplace=True)
    mars_facts = df.to_html(classes='data table', index=False, header=False, border=0)
    
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    time.sleep(1)
    
    html = browser.html
    soup = bs(html, 'html.parser')
    
    hemispheres = soup.find_all('div', class_ = 'item')
    image_urls = []
    hemispheres_main_url = 'https://astrogeology.usgs.gov'
    
    #since there are multiple URLS to scrape here, I built this loop to get each image from the 4 urls
    for hemisphere in hemispheres:
        title = hemisphere.find('h3').text
        hemisphere_url = hemisphere.find('a', class_='itemLink product-item')['href']
        new_url = hemispheres_main_url + hemisphere_url
        browser.visit(new_url)
        image_html = browser.html
        soup = bs(image_html, 'html.parser')
        image_url = soup.find('img', class_= "wide-image")['src']
        total_url = hemispheres_main_url + image_url
        image_urls.append({"title" : title, "img_url" : total_url})
        
    #creating a dictionary that will be returned by calling the scrape function     
    mars_data = {
        "news_title": news_title,
        "news_p": news_p,
        "featured_img": featured_img,
        #"mars_weatherweather": mars_weather,
        "mars_facts": mars_facts,
        "image_urls": image_urls
    }
    
    browser.quit()

    return mars_data



    
    



