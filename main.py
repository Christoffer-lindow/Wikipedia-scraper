import scraper
import writer
import time
import sys
import colors
REQUEST_URL = "https://en.wikipedia.org/wiki/Computer_programming"
PARSER = "html.parser"
PAGES_TO_PARSE = 250
BASE_PATH = "./output/"


def crawl(request_url, pages_to_parse, scraped_list):
    start = time.localtime()
    start_clock = time.time()
    print(f"{colors.OKCYAN}Crawling started at {start.tm_hour}:{start.tm_min}{colors.ENDC}")
    scraped_list = scraper.scrape_html(
        request_url, PARSER, scraped_list, pages_to_parse)
    end = time.localtime()
    end_clock = time.time()
    print(
        f"{colors.OKCYAN}Crawling ended at {end.tm_hour}:{end.tm_min} \nEplased time: {((end_clock-start_clock)) /60} minutes {colors.ENDC} ")
    return scraped_list


def create_raw_html(list):
    print(f"{colors.OKCYAN}Creating raw html...{colors.ENDC}")
    writer.write_html(BASE_PATH, list)
    print(f"{colors.OKGREEN}Raw html created successfuly{colors.ENDC}")


def create_content_pages(list):
    print(f"{colors.OKCYAN}Creating Word pages...{colors.ENDC}")
    writer.write_content(BASE_PATH, list)
    print(f"{colors.OKGREEN}Word pages created successfuly{colors.ENDC}")


def create_links_pages(list):
    print(f"{colors.OKCYAN}Creating Link Pages...{colors.ENDC}")
    writer.write_links(BASE_PATH, list)
    print(f"{colors.OKGREEN}Link pages created successfuly{colors.ENDC}")


def main(args):
    scraped_list = {"url": [], "html": []}
    try:
        if len(args) == 3:
            print(f"{colors.OKCYAN}Running from cli arguments {colors.ENDC}")
            cralwed_list = crawl(args[1], int(args[2]), scraped_list)
        else:
            print(f"{colors.OKCYAN}Running from cli arguments {colors.ENDC}")
            cralwed_list = crawl(REQUEST_URL, PAGES_TO_PARSE, scraped_list)
        create_raw_html(cralwed_list)
        create_content_pages(cralwed_list)
        create_links_pages(cralwed_list)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main(sys.argv)
