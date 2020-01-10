#'/usr/python3
# -*- coding:utf-8 -*-

import sys,configparser,os,easyust

if len(sys.argv) == 1:
    print('[INFO] 用法：python3 zuc.py <UST> [Singer] [output]')
else:
    conf = configparser.ConfigParser()
    conf.read('cfg.ini')
    if len(sys.argv) == 3:
        oto = os.path.abspath(sys.argv[2])
    else:
        oto = os.path.abspath(conf.get('zuc','oto'))
    tool = os.path.abspath(conf.get('zuc','tool'))
    resamp = os.path.abspath(conf.get('zuc','resamp'))
    cachedir = os.path.abspath(conf.get('zuc','cachedir'))
    if len(sys.argv) == 4:
        output = os.path.abspath(sys.argv[3])
    else:
        output = os.path.abspath(conf.get('zuc','output'))
    print('[INFO] 系统信息：')
    print('[INFO] 音源路径：',oto)
    print('[INFO] wavtool路径：',tool)
    print('[INFO] 引擎路径：',resamp)
    print('[INFO] 缓存路径：',cachedir)
    print('[INFO] 输出路径：',output)
    print('[INFO] 正在转码。。。')
    cproject = easyust.cproject(os.path.abspath(sys.argv[1]),cachedir + '/temp.ini')
    print('[INFO] UST信息：')
    print('[INFO] 路径：',cproject[0])
    print('[INFO] 临时文件：',cproject[1])
    tempo = easyust.rtempo(cproject[1])
    print('[INFO] 节奏：',tempo)
    print('[INFO] 工程名：', easyust.rpname(cproject[1]))
    nallnote = easyust.rnallnote(cproject[1])
    print('[INFO] 音符个数：', nallnote)
    allnote = easyust.rallnote(cproject[1])
    for x in allnote:
        nownote = str(allnote.index(x)+1)
        print('[INFO] 当前进度：',nownote,'/',nallnote)
        length = easyust.rlength(cproject[1],x)
        print('[INFO] 长度：',length)
        lyric = easyust.rlyric(cproject[1],x)
        print('[INFO] 歌词：',lyric)
        if lyric == 'R':
            execcmd = tool + ' ' + output + ' ' + oto + "/R.wav 0 " + length + '@' + tempo + '+.0 0 0'
            print('[INFO] 执行:',execcmd)
            os.system(execcmd)
        else:
            note = easyust.getnote(easyust.rNoteNum(cproject[1],x))
            print('[INFO] 音符：',note)
            vel = easyust.rVelocity(cproject[1],x)
            print('[INFO] 速度：',vel)
            temp = cachedir + '/' + nownote + '_' + lyric +'_' + note + '.wav'
            tempin = oto + '/' + lyric +'.wav'
            execcmd = resamp + ' ' + tempin + ' ' + temp + ' ' + note + ' ' + vel
            print('[INFO] 执行:',execcmd)
            os.system(execcmd)
            stp = '0'
            note_length = length + '@' + tempo + '+.0'
            p = '10 139 35 101 101 101 0 0 0'
            execcmd = tool + ' ' + output + ' ' + temp + ' ' + stp + ' ' + note_length + ' ' + p
            print('[INFO] 执行:',execcmd)
            os.system(execcmd)