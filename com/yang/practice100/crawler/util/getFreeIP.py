# -- coding: utf-8 --
import requests
import json


#
class FreeIP():
    def __init__(self):
        self.url = "http://proxylist.fatezero.org/proxy.list"
        self.headers ={'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}

    def check_ip(self, ip_list):
        correct_ip = []
        for ip in ip_list:
            # if len(correct_ip) > 20: # 可以根据自己的需求进行更改或者注释掉
            #     break
            ip_port = "{}:{}".format("https//",ip["host_port"])
            proxies = {'https': ip_port}
            try:
                response = requests.get('https://icanhazip.com/', proxies=proxies,
                                        timeout=3).text  # 如果请求该网址，返回的IP地址与代理IP一致，则认为代理成功
                                                        # 可以更改timeout时间

                if response.strip() == ip["exort_port"]:
                    print("可用的IP地址为：{}".format(ip_port))
                    correct_ip.append(ip_port)
            except:
                print("不可用的IP地址为：{}".format(ip_port))

        return correct_ip


    def run(self):
        response =  requests.get(url=self.url).content.decode()

        ip_list = []
        proxies_list = response.split('\n')

        for proxy_str in proxies_list:
            try:
                proxy = {}
                proxy_json = json.loads(proxy_str)
                if proxy_json["anonymity"] == "high_anonymous" and proxy_json["type"] == "https" and proxy_json["response_time"] <= 4:
                    host=proxy_json['host']
                    port=proxy_json['port']
                    host_port = "{}:{}".format(host,port)
                    exort_port = proxy_json['export_address'][0]
                    proxy["host_port"] = host_port
                    proxy["exort_port"] = exort_port
                    # print(proxy)
                    ip_list.append(proxy)
                    print("{}符合https和高匿条件".format(host_port))
            except:
                print(proxy_str)
        # print(ip_list)
        correct_ip = self.check_ip(ip_list)
        print("可用的IP地址有{}个".format(len(correct_ip)))
        print(correct_ip)


if __name__ == '__main__':
    ip = FreeIP()
    ip.run()

    """验证某些IP是否能用"""
    # ip_port='https://170.83.79.13:999'  #可用的https代理IP
    # # ip_port='https//:190.97.225.41:999'
    # proxies={'https': ip_port}
    # response = requests.get('https://icanhazip.com/', proxies=proxies).text
    # print(response)
