import scraper
import writer
import time
REQUEST_URL = "https://en.wikipedia.org/wiki/Computer_programming"
PARSER = "html.parser"
PAGES_TO_PARSE = 250
BASE_PATH = "./output/"
scraped_list = {"url": [], "html": []}

def crawl(scraped_list):
    start = time.localtime()
    start_clock = time.time()
    print(f"Crawling started at {start.tm_hour}:{start.tm_min}")
    scraped_list  =  scraper.scrape_html(REQUEST_URL,PARSER,scraped_list,PAGES_TO_PARSE)
    end = time.localtime()
    end_clock = time.time()
    print(f"Crawling ended at {end.tm_hour}:{end.tm_min} \nEplased time: {((end_clock-start_clock)) /60} minutes ")
    return scraped_list

def create_raw_html(list):
    print(f"Creating raw html")
    writer.write_html(BASE_PATH,list)

def create_content_pages(list):
    print(f"Creating Word pages...")
    writer.write_content(BASE_PATH,list)

def create_links_pages(list):
    print(f"Creating Link Pages...")
    writer.write_links(BASE_PATH,cralwed_list)



cralwed_list = crawl(scraped_list)
create_raw_html(cralwed_list)
create_content_pages(cralwed_list)
create_links_pages(cralwed_list)



