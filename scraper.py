import requests
from bs4 import BeautifulSoup as bs


def get_links(soup):
    return soup.find(id="bodyContent").find_all("a")


def contains_link(list, current_link):
    if "https://wikipedia.org" + current_link["href"] in list["url"]:
        return True
    return False


def string_contains_dot(string):
    return "." in string 


def scrape_html(url, parser, html_list, number_of_pages, count=0):
    if len(html_list["url"]) < number_of_pages:
        response = requests.get(url)
        soup = bs(response.content, parser)
        html_list["url"].append(url)
        html_list["html"].append(soup)
        list_size = len(html_list["url"])
        links_from_page = get_links(soup)
        print(f"[{list_size}] Crawling: {url}")
        for link in links_from_page:
            try:
                link_href = str(link["href"])
                if link_href.find("/wiki/") == -1:
                    continue
                elif list_size >= number_of_pages:
                    return html_list
                elif not contains_link(html_list, link) \
                        and not string_contains_dot(link_href)\
                and not link_href.endswith(".txt") \
                        and list_size <= number_of_pages:
                    scrape_html("https://wikipedia.org" +
                                link_href, parser, html_list, number_of_pages, count)
            except:
                continue
    return html_list
