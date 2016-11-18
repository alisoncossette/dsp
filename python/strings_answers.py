# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
#Metis Pre-work strings
#Alison Cossette

import re

def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    countout="many"   #set variable to most common output and establish type
    if count <10:     #set if statement for variations from default value
        countout=str(count)     #convert int to string for concatenation and output
    print "Number of donuts: " + countout   #print concatenation
    
print"\n'donuts' function output"
donuts(4)
donuts(9)
donuts(10)
donuts(99)




def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    length=len(s)
    if length<2:
        print ""
    else:
        print s[0:2]+s[-2:]

print "\n'both_ends' function output"    
both_ends('spring')
both_ends('Hello')
both_ends('a')
both_ends('xyz')
 

def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """

    print s[0]+s[1:].replace(s[0],'*')

print "\n'fix_start' function output"
fix_start('babble')
fix_start('aardvark')
fix_start('google')
fix_start('donut')   

def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    newa=b[0:2]+a[2:]
    newb=a[0:2]+b[2:] 
    word_lst=(newa, newb)
    space=" "
    string=space.join(word_lst)
    print string
    
print "\n'mix_up' function output"
mix_up('mix', 'pod')
mix_up('dog', 'dinner')
mix_up('gnash', 'sport')
mix_up('pezzy', 'firm')

def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.
    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    if len(s)>3:
        if s[-3:]=='ing':
            s=s+'ly'
        else:
            s=s+'ing'
    print s
    
print "\n'verbing' function output"
verbing('hail')
verbing('swiming')
verbing('do')   


def not_bad(s):
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not") 
    "It's bad yet not"  
    """
    #wl=s.split()           # word list of string
    wl=re.findall(r"[\w']+|[.,!?;]", s )
    n='not' in wl
    b='bad' in wl
    print wl


  
    if n==True:
        ni=wl.index('not')     # index position for "NOT"
        if b==True:
            bi=wl.index('bad')+1            
            if ni<bi:
                del wl[ni:bi]
                wl.insert(ni,'good')
    news=" ".join(wl) 
    print news

print "\n'not_bad' function output"
not_bad('This movie is not so bad')
not_bad('This dinner is not that bad!')
not_bad('This tea is not hot')
not_bad("It's bad yet not")


def front_back(a, b):
    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kit ten', 'Don ut')
    'KitDontenut'
    """ 
    x=len(a)/2    #a_back length   
    x1=len(a)-x   #a_front length         
    y=len(b)/2    #b_back length
    y1=len(b)-y   #b_front length

    
    afront=a[0:x1]
    aback=a[-x:]
    bfront=b[0:y1]
    bback=b[-y:]

    string=afront+bfront+aback+bback
    
    print string
    
print "\n'front_back' function output"        
front_back('abcd', 'xy')
front_back('abcde', 'xyz')
front_back('Kitten', 'Donut')
