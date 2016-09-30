#!/usr/bin python

import zipfile

def extractFile(zFile, passWord): 
    try:
        zFile.extractall(pwd = passWord)#extractall(self, path=None, members=None, pwd=None)
        return passWord
    except Exception as e:
        return

def main():
    zFile = zipfile.ZipFile('evil.zip')
    passFile = open('dictionary.txt')
    for line in passFile.readlines():
        passWord = line.strip('\n')
        guess = extractFile(zFile, passWord)
        if guess:
            print '[+] PassWord = ' + passWord + '\n'

if __name__ == '__main__':
   main() 
