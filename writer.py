from bs4 import BeautifulSoup as bs
import re
import os


def check_dir_exists(path):
    if not os.path.exists(path):
        os.mkdir(path)


def write_html(path, list):
    check_dir_exists(path+"/Html")
    try:
        for page in list["html"]:
            title = get_title(page)
            file_path = f"{path}/Html/{title}.html"
            with open(file_path, "w", encoding="utf-8") as writer:
                writer.write(str(page))
    except Exception as e:
        print(e)


def write_content(path, list):
    check_dir_exists(path+"/Words")
    for page in list["html"]:
        page_content = get_words_from_page(page)
        title = get_title(page)
        file_path = f"{path}/Words/{title}.txt"
        try:
            with open(file_path, "w", encoding="utf-8") as writer:
                writer.write(page_content["content"])
                writer.close()
        except Exception as e:
            print(e)


def write_links(path, list):
    check_dir_exists(path + "/Links")
    for page in list["html"]:
        page_links = get_links_from_page(page)
        title = get_title(page)
        file_path = f"{path}/Links/{title}.txt"
        try:
            with open(file_path, "w", encoding="utf-8") as writer:
                for link in page_links["links"]:
                    row = (str(link).split('"')[1].split('"')[0]) + "\n"
                    if row.startswith("/wiki/"):
                        writer.write(row)
            writer.close()
        except Exception as e:
            print(e)


def get_title(page):
    return str(bs.get_text(page.find(id="firstHeading")).lower()
        .replace('/', "_")
        .replace(":","_")
        .replace('"', "_"))


def get_words_from_page(page):
    content = re.sub('[!@#$%^&*(){[]}]|\;:"<>?/.,]', "", bs.get_text(
        page.find(id="bodyContent"))).replace("[", "").replace("edit]", "")
    return {"title": get_title(page), "content": content}


def get_links_from_page(page):
    return {"title": get_title(page), "links": page.find(id="bodyContent").find_all("a")}
