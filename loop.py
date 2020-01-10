#/usr/python3
# -*- coding:utf-8 -*-

import os,shutil

print('合成服务启动成功，按Ctrl+C退出')
while True:
    listfile=os.listdir('upload')
    for x in listfile:
        print('正在合成',x)
        for d in os.listdir('cache'):
            os.remove('cache/' + d)
        input = './upload/' + x
        os.system('python3 zuc.py ' + input)
        shutil.move('output.wav','static/' + x + '.wav')
        os.remove(input)
        print('完成')