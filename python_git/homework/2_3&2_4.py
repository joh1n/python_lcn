# -*- coding: utf-8 -*-


'''
2_3
'''
speech='''Four score and seven years ago our fathers brought forth on this continent, a new nation, conceived in Liberty, and dedicated to the proposition that all men are created equal.
Now we are engaged in a great civil war, testing whether that nation, or any nation so conceived and so dedicated, can long endure. We are met on a great battle-field of that war. We have come to dedicate a portion of that field, as a final resting place for those who here gave their lives that that nation might live. It is altogether fitting and proper that we should do this.
But, in a larger sense, we can not dedicate -- we can not consecrate -- we can not hallow -- this ground. The brave men, living and dead, who struggled here, have consecrated it, far above our poor power to add or detract. The world will little note, nor long remember what we say here, but it can never forget what they did here. It is for us the living, rather, to be dedicated here to the unfinished work which they who fought here have thus far so nobly advanced. It is rather for us to be here dedicated to the great task remaining before us -- that from these honored dead we take increased devotion to that cause for which they gave the last full measure of devotion -- that we here highly resolve that these dead shall not have died in vain -- that this nation, under God, shall have a new birth of freedom -- and that government of the people, by the people, for the people, shall not perish from the earth.'''


allwords=speech.split()
speechtem=[]

for w in allwords:
    w=w.lower()
    for a in w:
        if a.isalpha()==False:
            w=w.replace(a,'')
    if w!='':
        speechtem+=[(w)]

print('总单词个数：',len(speechtem))

wordstem=[]

for ws in speechtem:
    if ws not in wordstem:
        wordstem+=[(ws)]

print('不同单词个数：',len(wordstem))

n=0
for w in wordstem:
    print('{}'.format(w),end='')
    for i in range(0,16-len(w)):
        print(' ',end='')
    n+=1
    if n%5==0:
        print('\n')
        
        
        
"""第二部分"""
worddic=dict()
for w in wordstem:
    worddic[w]=0
for w in speechtem:
    worddic[w]+=1

wlist=sorted(worddic.items(),key=lambda asd:asd[0],reverse=True)
wlist=sorted(wlist,key=lambda asd:asd[1],reverse=True)


print('\n\nword            conut\n----------------------')
for w in wlist:
    print(w[0],end='')
    for i in range(0,16-len(w[0])):
        print(' ',end='')
    print(w[1],end='\n')
    

'''
2_4
'''

# -*- coding: utf-8 -*-
speech2='''When, in the course of human events, it becomes necessary for one people to dissolve the political bonds which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the laws of nature and of nature's God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation.
We hold these truths to be self-evident, that all men are created equal, that they are endowed by their Creator with certain unalienable rights, that among these are life, liberty and the pursuit of happiness. That to secure these rights, governments are instituted among men, deriving their just powers from the consent of the governed. That whenever any form of government becomes destructive to these ends, it is the right of the people to alter or to abolish it, and to institute new government, laying its foundation on such principles and organizing its powers in such form, as to them shall seem most likely to effect their safety and happiness. Prudence, indeed, will dictate that governments long established should not be changed for light and transient causes; and accordingly all experience hath shown that mankind are more disposed to suffer, while evils are sufferable, than to right themselves by abolishing the forms to which they are accustomed. But when a long train of abuses and usurpations, pursuing invariably the same object evinces a design to reduce them under absolute despotism, it is their right, it is their duty, to throw off such government, and to provide new guards for their future security. --Such has been the patient sufferance of these colonies; and such is now the necessity which constrains them to alter their former systems of government. The history of the present King of Great Britain is a history of repeated injuries and usurpations, all having in direct object the establishment of an absolute tyranny over these states. To prove this, let facts be submitted to a candid world.
He has refused his assent to laws, the most wholesome and necessary for the public good.
He has forbidden his governors to pass laws of immediate and pressing importance, unless suspended in their operation till his assent should be obtained; and when so suspended, he has utterly neglected to attend to them.
He has refused to pass other laws for the accommodation of large districts of people, unless those people would relinquish the right of representation in the legislature, a right inestimable to them and formidable to tyrants only.
He has called together legislative bodies at places unusual, uncomfortable, and distant from the depository of their public records, for the sole purpose of fatiguing them into compliance with his measures.
He has dissolved representative houses repeatedly, for opposing with manly firmness his invasions on the rights of the people.
He has refused for a long time, after such dissolutions, to cause others to be elected; whereby the legislative powers, incapable of annihilation, have returned to the people at large for their exercise; the state remaining in the meantime exposed to all the dangers of invasion from without, and convulsions within.
He has endeavored to prevent the population of these states; for that purpose obstructing the laws for naturalization of foreigners; refusing to pass others to encourage their migration hither, and raising the conditions of new appropriations of lands.
He has obstructed the administration of justice, by refusing his assent to laws for establishing judiciary powers.
He has made judges dependent on his will alone, for the tenure of their offices, and the amount and payment of their salaries.
He has erected a multitude of new offices, and sent hither swarms of officers to harass our people, and eat out their substance.
He has kept among us, in times of peace, standing armies without the consent of our legislature.
He has affected to render the military independent of and superior to civil power.
He has combined with others to subject us to a jurisdiction foreign to our constitution, and unacknowledged by our laws; giving his assent to their acts of pretended legislation:
For quartering large bodies of armed troops among us:
For protecting them, by mock trial, from punishment for any murders which they should commit on the inhabitants of these states:
For cutting off our trade with all parts of the world:
For imposing taxes on us without our consent:
For depriving us in many cases, of the benefits of trial by jury:
For transporting us beyond seas to be tried for pretended offenses:
For abolishing the free system of English laws in a neighboring province, establishing therein an arbitrary government, and enlarging its boundaries so as to render it at once an example and fit instrument for introducing the same absolute rule in these colonies:
For taking away our charters, abolishing our most valuable laws, and altering fundamentally the forms of our governments:
For suspending our own legislatures, and declaring themselves invested with power to legislate for us in all cases whatsoever.
He has abdicated government here, by declaring us out of his protection and waging war against us.
He has plundered our seas, ravaged our coasts, burned our towns, and destroyed the lives of our people.
He is at this time transporting large armies of foreign mercenaries to complete the works of death, desolation and tyranny, already begun with circumstances of cruelty and perfidy scarcely paralleled in the most barbarous ages, and totally unworthy the head of a civilized nation.
He has constrained our fellow citizens taken captive on the high seas to bear arms against their country, to become the executioners of their friends and brethren, or to fall themselves by their hands.
He has excited domestic insurrections amongst us, and has endeavored to bring on the inhabitants of our frontiers, the merciless Indian savages, whose known rule of warfare, is undistinguished destruction of all ages, sexes and conditions.
In every stage of these oppressions we have petitioned for redress in the most humble terms: our repeated petitions have been answered only by repeated injury. A prince, whose character is thus marked by every act which may define a tyrant, is unfit to be the ruler of a free people.
Nor have we been wanting in attention to our British brethren. We have warned them from time to time of attempts by their legislature to extend an unwarrantable jurisdiction over us. We have reminded them of the circumstances of our emigration and settlement here. We have appealed to their native justice and magnanimity, and we have conjured them by the ties of our common kindred to disavow these usurpations, which, would inevitably interrupt our connections and correspondence. We must, therefore, acquiesce in the necessity, which denounces our separation, and hold them, as we hold the rest of mankind, enemies in war, in peace friends.
We, therefore, the representatives of the United States of America, in General Congress, assembled, appealing to the Supreme Judge of the world for the rectitude of our intentions, do, in the name, and by the authority of the good people of these colonies, solemnly publish and declare, that these united colonies are, and of right ought to be free and independent states; that they are absolved from all allegiance to the British Crown, and that all political connection between them and the state of Great Britain, is and ought to be totally dissolved; and that as free and independent states, they have full power to levy war, conclude peace, contract alliances, establish commerce, and to do all other acts and things which independent states may of right do. And for the support of this declaration, with a firm reliance on the protection of Divine Providence, we mutually pledge to each other our lives, our fortunes and our sacred honor.'''

allwords2=speech2.split()
speechtem2=[]

for w in allwords2:
    w=w.lower()
    for a in w:
        if a.isalpha()==False:
            w=w.replace(a,'')
    if w!='':
        speechtem2+=[(w)]
'''
print('总单词个数：',len(speechtem2))
'''
wordstem2=[]

for ws in speechtem2:
    if ws not in wordstem2:
        wordstem2+=[(ws)]


set1=set(wordstem)
set2=set(wordstem2)
print('所用单词数量分别为{}和{}'.format(len(wordstem),len(wordstem2)))
print('总单词数两为{}'.format(len(set1|set2)))
print('公用单词数量为{}'.format(len(set1&set2)))
print('1有2没有为{}'.format(len(set1-set2)))
print('2有1没有为{}'.format(len(set2-set1)))
print('公有单词为：')
n=0
for w in set1&set2:
    print('{}'.format(w),end='')
    for i in range(0,16-len(w)):
        print(' ',end='')
    n+=1
    if n%5==0:
        print('\n')







