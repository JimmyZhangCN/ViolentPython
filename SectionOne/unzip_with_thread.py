#!/usr/bin python

import zipfile
import optparse
from threading import Thread


def extractFile(zFile, passWord): 
    try:
        zFile.extractall(pwd = passWord)#extractall(self, path=None, members=None, pwd=None)
        print '[+] PassWord = ' + passWord + '\n'
        return passWord
    except Exception as e:
        return

def main():
    parser = optparse.OptionParser('Usage -f <zipfile -d <dictionary>>')
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    (options, args) = parser.parse_args()
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(-1)
    else:
        zname = options.zname
        dname = options.dname

    zFile = zipfile.ZipFile(zname)
    passFile = open(dname)
    for line in passFile.readlines():
        passWord = line.strip('\n')
        t = Thread(target=extractFile, args=(zFile, passWord))
        t.start()

if __name__ == '__main__':
   main() 
