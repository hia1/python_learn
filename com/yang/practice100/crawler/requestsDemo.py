# -- coding: utf-8 --
import requests

if __name__ == '__main__':
    url="https://www.baidu.com/"
    response=requests.get(url=url)
    # res_text=response.content.decode(encoding="utf-8")
    #apparent_encoding解决请求网页内容乱码
    response.encoding=response.apparent_encoding
    res_text=response.text

    print(res_text)
    file_path="./res.html"
    with open(file_path,"w",encoding="utf-8") as f:
        f.write(res_text)


