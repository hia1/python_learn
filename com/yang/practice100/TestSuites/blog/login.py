# -- coding: utf-8 --
import re

import requests
import  urllib3
urllib3.disable_warnings()
import warnings
warnings.simplefilter('ignore',ResourceWarning)



class Blog():
    def __init__(self,s) -> None:
        s = requests.session()
        self.s=s

    def login(self):
        login_url="https://account.cnblogs.com/signin"
        headers={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
        login_data={"j_username": "admin",
         "j_password": "123456",
         "from": "/",
         "Submit": u"登录",
         "remember_me": "on"}
        s = requests.session()
        r = s.post(login_url,headers=headers,data=login_data)
        t = re.findall(r'<b>(.+?)</b>', r.content.decode('utf-8'))  # 用python3的这里r.content需要解码
        print(t[0])
        print(t[1])

    def get_postid(self,r2_url):
        postid=re.findall(r'postid=(.+?)&',r2_url)
        print(postid)
        return postid[0]
    def save(self,title,body):
        url2 = "https://i.cnblogs.com/api/posts"
        d = {"id":"null","postType":1,"accessPermission":0,"title":title,"url":"null","postBody":body,"categoryIds":"null","inSiteCandidate":"false","inSiteHome":"false","siteCategoryId":"null","blogTeamIds":"null","isPublished":"false","displayOnHomePage":"true","isAllowComments":"true","includeInMainSyndication":"true","isPinned":"false","isOnlyForRegisterUser":"false","isUpdateDateAdded":"false","entryName":"null","description":"null","featuredImage":"null","tags":"null","password":"null","datePublished":"2022-12-20T06:33:40.763Z","dateUpdated":"null","isMarkdown":"false","isDraft":"true","autoDesc":'null',"changePostType":"false","blogId":'0',"author":'null',"removeScript":'false',"clientInfo":'null',"changeCreatedTime":'false',"canChangeCreatedTime":'false',"isContributeToImpressiveBugActivity":'false',"usingEditorId":3,"sourceUrl":'null'}
        r2 = self.s.post(url2, data=d, verify=False)  # 保存草稿箱
        print(r2.url)
        return r2.url

    def delete(self,postid):
        del_json = {"postId": postid}
        del_url = "https://i.cnblogs.com/post/delete"
        r3 = self.s.post(del_url, json=del_json, verify=False)
        print(r3.json()["isSuccess"])
        return r3.json()

if __name__ == '__main__':
    s = requests.session()
    Blog(s).login()
    Blog(s).save(title='qqqqqqqqqqqq demo',body="vvvvvvvvvvvv body")