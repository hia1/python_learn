# -- coding: utf-8 --
import smtplib
import ssl
import unittest
from email.header import Header
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import HTMLTestRunner, os, time

def run_all_case():
    #用例之形目录
    case_dir='F:\pythonLearn\com\yang\practice100\TestSuites\case'
    testsuite=unittest.TestSuite()
    #discover返回一个pattern条件的列表
    discover=unittest.defaultTestLoader.discover(case_dir,pattern='test*.py',top_level_dir=None)

    #遍历discover列表，加入测试套件中
    for test_suite in discover:
        for test_case in test_suite:
            testsuite.addTests(test_case)
    print(testsuite)
    return testsuite

def reportFile(test_report):
    lists=os.listdir(test_report)
    #按报告时间升序
    lists.sort(key=lambda  fn: os.path.getmtime(test_report+'\\'+fn))
    #发送最新报告
    file_new=os.path.join(test_report,lists[-1])
    return file_new

def send_mail(file):
    with open(file,'rb') as fp:
        mailText=fp.read()
    mailName='yangzhenyu7353@163.com'
    mailWord='NUQIYEXROVWPXUAU'
    sender='yangzhenyu7353@163.com'

    receiver=['424484631@qq.com']
    #邮箱正文
    bodyText = MIMEText(mailText, 'html', 'utf-8')
    #邮件对象
    msg = MIMEMultipart('mixed')
    msg['Subject'] = Header("自动化测试报告", 'utf-8').encode()
    msg['From'] = Header(u'yang <%s>'%sender)
    msg['To'] = Header(u'测试负责人 <%s>'%receiver)
    msg['date'] = time.strftime("%a,%d %b %Y %H:%M:%S %z")
    #构造邮件正文内容
    text='Hi!\nHow are you?\nHere is the link you wanted:\n'
    text_plain=MIMEText(text,'plain','utf-8')
    msg.attach(text_plain)
    msg.attach(bodyText)
    #明文发送邮件，安全性低
    # smtp = smtplib.SMTP()
    # smtp.connect('smtp.163.com')  # 邮箱服务器
    #构造图片发送
    imageFile=open(r'C:\Users\ASUS\Pictures\image1.jpg','rb').read()
    image=MIMEImage(imageFile)
    image.add_header('Content-ID', '<image1>')
    image["Content-Disposition"] = 'attachment; filename="butty.png"'
    msg.attach(image)
    #添加附件
    att = MIMEText(mailText, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    # 使用ssl模块的context加载系统允许的证书，在登录时进行验证
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.163.com',465,context=context) as smtp:
        smtp.login(mailName, mailWord)  # 登录邮箱
        print("邮件正在发送")
        smtp.sendmail(sender, receiver, msg.as_string())  # 发送者和接收者
        print("邮件已发出！注意查收。")



if __name__ == '__main__':
    runner=unittest.TextTestRunner()
    #导入测试报告模块
    now=time.strftime("%Y-%m-%M-%H_%M", time.localtime(time.time()))
    report_path=r'F:\pythonLearn\com\yang\practice100\TestSuites\report'
    report_name=os.path.join(report_path,'result'+now+'.html')
    print(report_name)
    if not os.path.exists(report_path):
        os.mkdir(report_path)
    with open(report_name,'wb') as fp:
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='xxxx测试报告',description='xxxx用例执行情况')
            runner.run(run_all_case())
    fp.close()
    new_report = reportFile(report_path)
    #发送邮件
    # send_mail(new_report)