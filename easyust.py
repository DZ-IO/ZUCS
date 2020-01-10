# -*- coding:utf-8 -*-

import configparser
import os

def getnote(NoteNum) :
    listN = ['24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78','79','80','81','82','83','84','85','86','87','88','89','90','91','92','93','94','95','96','97','98','99','100','101','102','103','104','105','106','107']
    listY = ['C1','C#1','D1','D#1','E1','F1','F#1','G1','G#1','A1','A#1','B1','C2','C#2','D2','D#2','E2','F2','F#2','G2','G#2','A2','A#2','B2','C3','C#3','D3','D#3','E3','F3','F#3','G3','G#3','A3','A#3','B3','C4','C#4','D4','D#4','E4','F4','F#4','G4','G#4','A4','A#4','B4','C5','C#5','D5','D#5','E5','F5','F#5','G5','G#5','A5','A#5','B5','C6','C#6','D6','D#6','E6','F6','F#6','G6','G#6','A6','A#6','B6','C7','C#7','D7','D#7','E7','F7','F#7','G7','G#7','A7','A#7','B7']
    for i in range(84):
        note = listN[i]
        if note == NoteNum :
            return listY[i]

def cproject(ust, outfile = os.getcwd()+'/temp.ini', debug = 'no') :
    ust = os.path.abspath(ust)
    outfile = os.path.abspath(outfile)
    if debug == 'yes' :
        print(ust)
        print(outfile)
    try:
        with open(outfile, 'w+') as t: 
            t.write("")
    finally:
        try:
            with open(ust,'r') as f:
                rust = f.read().splitlines()
                for x in rust:
                    if x != "UST Version1.2":
                        with open(outfile, 'a+') as t: t.write(x + '\n')
        finally:
            if f:
                f.close()
                if t:
                    return (ust, outfile)
            if t:
                t.close()

def isust(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    isust = conf.sections()
    isust = '#0000' in isust
    if debug == 'yes' : 
        for x in isust : print(x)
    return isust


def rtempo(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get('#SETTING','Tempo'))
    return conf.get('#SETTING','Tempo')

def rpname(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get('#SETTING','ProjectName'))
    return conf.get('#SETTING','ProjectName')

def rdb(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get('#SETTING','VoiceDir'))
    return conf.get('#SETTING','VoiceDir')

def rof(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get('#SETTING','VoiceDir'))
    return conf.get('#SETTING','OutFile')

def rcache(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get('#SETTING','VoiceDir'))
    return conf.get('#SETTING','CacheDir')

def rwt(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get('#SETTING','Tool1'))
    return conf.get('#SETTING','Tool1')

def rres(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get('#SETTING','Tool2'))
    return conf.get('#SETTING','Tool2')

def rflags(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get('#SETTING','Flags'))
    return conf.get('#SETTING','Flags')

def rnallnote(iniust, debug = 'no') :
    allnote = rallnote(iniust)
    allnote = len(allnote)
    if debug == 'yes' : print(allnote)
    return allnote

def rallnote(iniust, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    allnote = conf.sections()
    if allnote[0] != '#VERSION':
        allnote = allnote[1:]
    else:
        allnote = allnote[2:]
    allnote = allnote[:-1]
    if debug == 'yes' : 
        for x in allnote : print(x)
    return allnote

def rlength(iniust, nnote, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get(nnote,'Length'))
    return conf.get(nnote,'Length')

def rlyric(iniust, nnote, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get(nnote,'Lyric'))
    return conf.get(nnote,'Lyric')

def rNoteNum(iniust, nnote, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get(nnote,'NoteNum'))
    return conf.get(nnote,'NoteNum')

def rPreUtterance(iniust, nnote, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get(nnote,'PreUtterance'))
    return conf.get(nnote,'PreUtterance')

def rVelocity(iniust, nnote, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get(nnote,'Velocity'))
    return conf.get(nnote,'Velocity')

def rEnvelope(iniust, nnote, debug = 'no') :
    iniust = os.path.abspath(iniust)
    conf = configparser.ConfigParser()
    conf.read(iniust)
    if debug == 'yes' : print(conf.get(nnote,'Envelope'))
    return conf.get(nnote,'Envelope')
