
import os
import pathlib

import requests
from bs4 import BeautifulSoup

MAIN_PAGE = "http://mail-archives.apache.org/mod_mbox/maven-users/"
year = input("\n Enter year:")

def get_page(url):
    proxies = {
        "http": "16.167.28.210:8080",
        "https": "16.167.28.210:8080"
    }
    rq = requests.get(url, timeout=50, proxies=proxies)
    if not rq.ok:
        raise IOError("Failed to fetch requested url: {0}.\n Status: {1}".format(url, rq.status))
    return rq.content

def get_page_object(page_data):
    soup = BeautifulSoup(page_data, 'html.parser')
    return soup

def get_required_mail_year_table(soup):
    table_obj = None
    mail_tables_headers = soup.select("table.year > thead > tr > th")
    for thObj in mail_tables_headers:
        if year in thObj.get_text():
            table_obj = thObj.findParent("table")
            break
    else:
        raise Exception("No specific year of provided value found")
    return table_obj

def create_dir(parent_dir, new_dir_name):
    dir_name = os.path.join(parent_dir, new_dir_name)
    pathlib.Path(dir_name).mkdir(parents=True, exist_ok=True)
    return dir_name

def create_base_dir():
    cwd = os.getcwd()
    mail_path = os.path.join("Mails", str(year))
    dir_name = create_dir(cwd, mail_path)
    return dir_name

def parse_table_rows(table_obj):
    dir_name = create_base_dir()
    print(dir_name)
    table_rows = table_obj.select("tbody > tr")
    print("Downloading mails")
    for row in table_rows:
        month = row.find_all("td")[0].get_text()
        print(month)
        create_dir(dir_name, month)

if __name__ == "__main__":
    page = get_page(MAIN_PAGE)
    page_obj = get_page_object(page)
    table_obj = get_required_mail_year_table(page_obj)
    parse_table_rows(table_obj)
