import scraper
import writer
import time
import sys
REQUEST_URL = "https://en.wikipedia.org/wiki/Computer_programming"
PARSER = "html.parser"
PAGES_TO_PARSE = 3
BASE_PATH = "./output/"

def crawl(request_url, pages_to_parse, scraped_list):
    start = time.localtime()
    start_clock = time.time()
    print(f"Crawling started at {start.tm_hour}:{start.tm_min}")
    scraped_list = scraper.scrape_html(
        request_url, PARSER, scraped_list, pages_to_parse)
    end = time.localtime()
    end_clock = time.time()
    print(
        f"Crawling ended at {end.tm_hour}:{end.tm_min} \nEplased time: {((end_clock-start_clock)) /60} minutes ")
    return scraped_list


def create_raw_html(list):
    print(f"Creating raw html")
    writer.write_html(BASE_PATH, list)


def create_content_pages(list):
    print(f"Creating Word pages...")
    writer.write_content(BASE_PATH, list)


def create_links_pages(list):
    print(f"Creating Link Pages...")
    writer.write_links(BASE_PATH, list)

def main(args):
    scraped_list = {"url": [], "html": []}
    try:
        print(args[1])
        if len(args)==3:
            print("yes")
            cralwed_list = crawl(args[1],int(args[2]), scraped_list)
        else:
            cralwed_list = crawl(REQUEST_URL, PAGES_TO_PARSE, scraped_list)
        create_raw_html(cralwed_list)
        create_content_pages(cralwed_list)
        create_links_pages(cralwed_list)
    except Exception as e:
        print("Are you connected to internet?")


if __name__ == "__main__":
    main(sys.argv)
