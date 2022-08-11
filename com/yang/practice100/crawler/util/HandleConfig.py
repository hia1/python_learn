# -- coding: utf-8 --

from configparser import ConfigParser


class HandleConfig(ConfigParser):
    def __init__(self, filename):
        super().__init__()  # 调用父类init方法
        self.filename = filename
        self.read(filename,encoding="UTF-8")


    def write_data(self, section, options, value):
        """写入数据的方法"""
        self.set(section, options, value)
        self.write(fp=open(self.filename, "w"))


    #删除配置文件sectio
    def remove_section(self, section: str) -> bool:
        return super().remove_section(section)

    #删除配置文件的值
    def remove_option(self, section: str, option: str) -> bool:
        return super().remove_option(section, option)


if __name__ == '__main__':
    """Accept-Language: zh-CN,zh;q=0.9
        Connection: keep-alive"""
    handle1=HandleConfig("headers.ini")
    res=handle1.get("request","User-Agent")
    print(res)
    handle1.write_data("request","Accept-Language","zh-CN,zh;q=0.9")
    # handle1.remove_option("request2","accept-language")