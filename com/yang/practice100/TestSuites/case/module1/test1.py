# -- coding: utf-8 --

import unittest
import requests

class TestModule1(unittest.TestCase):
    def setUp(self) -> None:
        print("start")

    def tearDown(self) -> None:
        print('teardown')

    def test01(self):
        print("1")
        s=requests.session()
        url='https://www.baidu.com/'
        headers={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}
        r=s.post(url,headers=headers)
        print(r.cookies)
        cookies_login={
    'BDUSS':"BDUSS=DBXbEJ1RkVZNGZKZlBWZWFlY2tzQ1U4N3I4N1A0cjIyTkFSQjBmZ3ptZjllOU5qSUFBQUFBJCQAAAAAAAAAAAEAAAB~XMgpaGlhaGlhaGlhQmFpRHUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAP3uq2P97qtjS",
            'BAIDUID':'8936AFA4DC63F3FF017DEB0EBBD93B34:FG=1',
            'BD_HOME':1,'H_PS_PSSID':'36550_37971_37559_37689_38011_36921_37990_37802_36804_37934_38002_37993_37903_26350_37957_37881',
            'baikeVisitId':'73ad4e2a-e596-4154-a637-2ad3bc407406',
            'PSTM':'1672209828',
            'PSINO':7,
            'BD_UPN':12314753,
            'BA_HECTOR':'200k8181002h040k2ga1018l1hqnpd51i',
            'BDORZ':'B490B5EBF6F3CD402E515D22BCDA1598',
            'channel':"localhost:63342"

        }
        # 添加登录所携带的cookies
        c = requests.cookies.RequestsCookieJar()
        c.set("BDUSS", cookies_login["BDUSS"])
        c.set("BAIDUID", cookies_login["BAIDUID"])
        s.cookies.update(c)
        # 判断是否登录成功
        r2 = s.get(url, headers=headers)
        resp=r2.content.decode('utf-8')
        # print(resp)
        with open('baidu.html','w',encoding='utf-8') as f:
            f.write(resp)
        f.close()
        if 'hiahiahiaBaiDu' in resp:
            print('登录成功')
        else:
            print("登录失败")
    def test02(self):
        print("2")
if __name__ == '__main__':
    unittest.main()