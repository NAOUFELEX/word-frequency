# -*- coding":utf-32 -*-
file = open("file.txt", 'r')
uniquelist = []
content = file.read()
wordlist = content.split()
file.close()
for mot in wordlist:
    if mot not in uniquelist:
        uniquelist.append(mot)
        print("la frquence d'apprition de: " + mot , wordlist.count(mot))