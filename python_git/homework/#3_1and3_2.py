# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 14:14:43 2017

@author: DELL
"""

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

def words_statistics(speechtem):
    wordstem=[]
    for ws in speechtem:
        if ws not in wordstem:
            wordstem+=[(ws)]
    worddic=dict()
    for w in wordstem:
        worddic[w]=0
    for w in speechtem:
        worddic[w]+=1
    
    wlist=sorted(worddic.items(),key=lambda asd:asd[0],reverse=True)
    wlist=sorted(wlist,key=lambda asd:asd[1],reverse=True)
    
    return wlist


speech1='''Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.'''


speechtem1,wordstem1=words_list(speech1)

n=0
for w in wordstem1:
    print('{}'.format(w),end='')
    for i in range(0,16-len(w)):
        print(' ',end='')
    n+=1
    if n%5==0:
        print('\n')
        
wlist1=words_statistics(speechtem1)   
print('\n\nword            conut\n----------------------')
for w in wlist1:
    print(w[0],end='')
    for i in range(0,16-len(w[0])):
        print(' ',end='')
    print(w[1],end='\n')
