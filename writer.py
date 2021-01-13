from bs4 import BeautifulSoup as bs
import re


def write_html(path, list):
    with open(path + "/raw_html.txt", "w", encoding="utf-8") as writer:
        try:
            for page in list["html"]:
                writer.write("<!-- Start of new file -->")
                writer.write(str(page))
        except Exception as e:
            print(e)

    print("Finished printing")


def write_content(path, list):
    for page in list["html"]:
        page_content = get_words_from_page(page)
        local_path = f"{path}/Words/{page_content['title']}.txt"
        try:
            with open(local_path, "w", encoding="utf-8") as writer:
                writer.write(page_content["content"])
                writer.close()
        except Exception as e:
            print(e)


def write_links(path, list):
    for page in list["html"]:
        page_links = get_links_from_page(page)
        local_path = f"{path}/Links/{page_links['title']}.txt"
        try:
            with open(local_path, "w", encoding="utf-8") as writer:
                for link in page_links["links"]:
                    row = (str(link).split('"')[1].split('"')[0]) + "\n"
                    if row.startswith("/wiki/"):
                        writer.write(row)
            writer.close()
        except:
            print(
                "Something went wrong with printing the file, does the directory exist?")


def get_title(page):
    return str(bs.get_text(page.find(id="firstHeading")).lower().replace("/", "_").replace(" ", "_").replace(":", "_"))


def get_words_from_page(page):
    content = re.sub('[!@#$%^&*(){[]}]|\;:"<>?/.,]', "", bs.get_text(
        page.find(id="bodyContent"))).replace("[", "").replace("edit]", "")
    return {"title": get_title(page), "content": content}


def get_links_from_page(page):
    return {"title": get_title(page), "links": page.find(id="bodyContent").find_all("a")}