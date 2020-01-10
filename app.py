#/usr/python3
# -*- coding:utf-8 -*-

from flask import Flask, render_template, redirect, url_for, request
from werkzeug import secure_filename
import random, os, easyust
app = Flask(__name__)

@app.route('/')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['POST'])
def uploader():
   if request.method == 'POST':
      f = request.files['file']
      number = str(random.randint(0,1024000))
      upload_project = 'upload/' + number + '.ust'
      f.save(number + '.ust')
      easyust.cproject(number + '.ust',upload_project)
      os.remove(number + '.ust')
      isust = easyust.isust(upload_project)
      if isust != True:
         os.remove(upload_project)
         return '读取工程失败！您上传的不是有效的UST！'
      else:
         pname = easyust.rpname(upload_project)
         return '您上传的工程为：' + pname + ' 您的随机提取码为：' + number

@app.route('/get',methods = ['GET'])
def get():
   argv = request.args.get('num')
   if os.path.exists('static/' + argv + '.ust.wav') == True and os.path.exists('upload/' + argv + '.ust') != True :
      return render_template('ok.html',file = argv,name = argv)
   else :
      return '您的工程可能没有合成完成，或您未上传此文件'
	
if __name__ == '__main__':
   app.run(debug = True)