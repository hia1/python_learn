# -- coding: utf-8 --
import ddddocr
"""开源ddddocr库，用于验证码解析，图片识别"""
# img_path验证码存储路径
def recognize(img_path,length):
    ocr = ddddocr.DdddOcr()
    with open(img_path, 'rb') as f:
        img_bytes = f.read()
    verify_res = ocr.classification(img_bytes)
    #判断识别的长度是否正确
    if len(verify_res)<length:
        recognize(img_path,length)
        print(verify_res)
    print(verify_res)
    return verify_res

if __name__ == '__main__':
    recognize("../picLibs/codeLib/code.jpg",4)
