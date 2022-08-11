# -- coding: utf-8 --
import pdfkit as pdfkit
import requests
from bs4 import BeautifulSoup


def parse_url_to_html(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.content, "html.parser")
    body = soup.find_all(class_="x-wiki-content")[0]
    print(body)
    html = str(body)
    with open("a.html", 'wb') as f:
        f.write(str.encode(html,"utf-8"))


def get_url_list():
    """
    获取所有URL目录列表
    """
    response = requests.get("http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000")
    soup = BeautifulSoup(response.content, "html.parser")
    menu_tag = soup.find_all(class_="uk-nav uk-nav-side")[1]
    urls = []
    for li in menu_tag.find_all("div"):
        # url = "http://www.liaoxuefeng.com" + li.a.get('href')
        url = "http://www.liaoxuefeng.com" + li.select_one("a.x-wiki-index-item").get("href")
        urls.append(url)
    return urls


def save_pdf(htmls,file_name):
    """
    把所有html文件转换成pdf文件
    """
    options = {
        'page-size': 'Letter',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ]
    }
    pdfkit.from_file(htmls, file_name, options=options)



if __name__ == '__main__':
    c=get_url_list()
    # parse_url_to_html(c[1])
    print(c)
    parse_url_to_html(c[0])
