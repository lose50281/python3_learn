# -*- coding:UTF-8 -*-
import requests


if __name__ == '__main__':
    target = 'http://docs.python-requests.org/zh_CN/latest/user/quickstart.html'
    req = requests.get(url=target)
    print(req.text)
    # bf = req.text
    # texts = bf.find('div', class_ = 'link')
    # print(texts)



