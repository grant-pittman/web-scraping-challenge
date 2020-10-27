# Web Scraping Homework - Mission to Mars  <!-- omit in toc -->
 - [Overview](#overview)
- [Step 1 - Scraping](#step-1---scraping)
- [NASA Mars News](#nasa-mars-news)
- [JPL Mars Space Images - Featured Image](#jpl-mars-space-images---featured-image)
- [Mars Weather](#mars-weather)
- [Mars Facts](#mars-facts)
- [Mars Hemispheres](#mars-hemispheres)
- [Step 2 - MongoDB and Flask Application](#step-2---mongodb-and-flask-application)


## Overview

In this assignment, I built a web application that scrapes various websites for data related to the Mission to Mars and displays the information in a single HTML page. 

## Step 1 - Scraping

Using Jupyter Notebook, BeautifulSoup, Pandas, and Requests/Splinter I scraped various websites to obtain the data I would later render onto an HTML page. 

* The included Jupyter Notebook file called `mission_to_mars.ipynb` contains all of the scraping and analysis code. The following outlines what was scraped. 

### NASA Mars News

* The first scrape was from the [NASA Mars News Site](https://mars.nasa.gov/news/). I collected the latest News Title and Paragraph Text. 


### JPL Mars Space Images - Featured Image

* The following scrape obtained the JPL Featured Space Image  [here](https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars).

* I used splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called `featured_image_url`.

### Mars Weather

* Next, I scraped the Mars Weather twitter account [here](https://twitter.com/marswxreport?lang=en) and obtained the latest Mars weather tweet.


### Mars Facts

* The webpage [here](https://space-facts.com/mars/) had a table containing facts about the planet including Diameter, Mass, etc. I took the table and loaded it into a Pandas Dataframe.

* I then used Pandas to convert the data to a HTML table string.

### Mars Hemispheres

* Visit the USGS Astrogeology site [here](https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars) and obtained a high resolution image for each of Mar's hemispheres.

* Appended a dictionary with the image url string and the hemisphere title to a list. This list contains  one dictionary for each hemisphere.

- - -

## Step 2 - MongoDB and Flask Application

Used MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.

* I converted my Jupyter notebook into a Python script called `scrape_mars.py` with a function called `scrape` that will execute all of my scraping code from above and return one Python dictionary containing all of the scraped data.

* Next, I created a Flask app with a route called `/scrape` that will import my `scrape_mars.py` script and call my `scrape` function.

* Created a root route `/` that will query my Mongo database and pass the mars data into an HTML template to display the data.

* Created a template HTML file called `index.html` that will take the mars data dictionary and display all of the data in the appropriate HTML elements. 



