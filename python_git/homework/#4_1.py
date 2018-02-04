# -*- coding: utf-8 -*-

def words_list(speech):
    allwords=speech.split()
    speechtem=[]
    
    for w in allwords:
        w=w.lower()
        for a in w:
            if a.isalpha()==False:
                w=w.replace(a,'')
        if w!='':
            speechtem+=[(w)]
    
    wordstem=[]
    
    for ws in speechtem:
        if ws not in wordstem:
            wordstem+=[(ws)]
            
    return speechtem,wordstem

with open('Declaration.txt','r') as f:
    s=f.read()
    f.close()


speechtem1,wordstem1=words_list(s)
'''
n=0
for w in wordstem1:
    print('{}'.format(w),end='')
    for i in range(0,16-len(w)):
        print(' ',end='')
    n+=1
    if n%5==0:
        print('\n')
'''        
    
with open('wordslist.txt','w') as f:
    
    n=0
    for w in wordstem1:
        f.write(w)
        for i in range(0,16-len(w)):
            f.write(' ')
        n+=1
        if n%5==0:
            f.write('\n')
    f.close()
