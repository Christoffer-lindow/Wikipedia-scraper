# Webscraping
Webscraping project for scraping wikipedia pages.

## How to run
* Set up a virtual enviorment in the root of the project
* pip install from the requirements.txt file
* run: python main.py
    * If you run the script without cli arguments the initial url to crawl is: https://en.wikipedia.org/wiki/Computer_programmin, 250 pages will be parsed
    * You can also run the scripts with args: python main.py YOUR_URL NUMBER_OF_PAGES
* Wait!

## Configure
As of this moment the project does not use arguments from the terminal so the only way to configure the script is to go inside main, you could:
* Change the request url in the main.py file (note that the scraper is designed to work on wikipedia pages)
* Change the parser (you should not)
* Change how many pages that will be parsed
* Change base output path


