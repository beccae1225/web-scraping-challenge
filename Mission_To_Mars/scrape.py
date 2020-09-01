from splinter import Browser
from bs4 import BeautifulSoup as bs
import time

def init_browser():
    executable_path = {"executable_path": "/chromedriver.exe"}
    return Browser("chrome", **executable_path), headless=False)

def scrape_info():
    browser = init_browser()

    #Visit URL
    url = "https://mars.nasa.gov/news/"
    browser.visit(url)

    time.sleep(1)

    html = browser.html
    soup = bs(html, "html.parser")

    #news_title
    news_titles = soup.find("div", class_="content_title")

    #news paragraph
    news_p = soup.find("div", class_="article_teaser_body").text


    



    browser.quit()


