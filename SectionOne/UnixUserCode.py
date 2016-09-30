#/usr/bin python
import crypt

def testPass(cryptPass):
    salt = cryptPass[0:2]

    routeFile = open('route.txt', 'w+')
    dictFile = open('dictionary.txt', 'r')
    for word in dictFile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        routeFile.write(word + '\n' + cryptWord + '\n')

        if (cryptWord == cryptPass ):
            print('[+] Found Password :' + word)
            return
    print('[+] PassWord not found')
    return

def main():
    passFile = open('passwords.txt', 'r')
    for line in passFile.readlines():
         if ':' in line:
            user = line.split(':')[0]
            cryptPass = line.split(':')[1].strip(' ')
            print('Check password for ' + user + ' ' + cryptPass)
            testPass(cryptPass)

if __name__ == '__main__':
    main()
