# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 15:51:00 2019

@author: Niv Lifshitz
"""

import re
from os import stat


class EmptyFileError(Exception):
        pass
    
    
COLORS={'green','yellow','orange','blue','white','black','grey','pink','red'}
SLANGS={'sry':'sorry','pls':'please','u':'you','msg':'message','dw':"don't worry","gl":'good luck'}

def fix(word):#A fucntion that modifies or replaces the word.
    clean_word=re.sub('[,?!@#$%^&*()-+=\']','',word)#the word without marks
    if clean_word in COLORS :
        return word.replace(clean_word,len(clean_word)*'#')#replaces only the word itself
    elif clean_word in SLANGS:
        return  word.replace(clean_word,len(clean_word)*'#')
    return Normal(word)
    

def Normal(word):#Replaces all excess upper letters with lower letters
    clean_word=re.sub('[,?!@#$%^&*()-+=\']','',word)
    firstUpper=True if word[0].isupper() else False
    Nword=clean_word.lower() if not firstUpper else clean_word[0]+clean_word[1:].lower()
    return word.replace(clean_word,Nword)

def removeWhitespace(line):#removes all the white space from a line
    line=line.split(' ')
    line=list(dict.fromkeys(line))
    if '' in line:
        line.remove('')
    return ' '.join(line)

def create_new_line(lines):#yields a line each time
    for line in lines:
        yield ' '.join(line)

def main():
    try:
        if stat('Chat.txt').st_size==0:
            raise EmptyFileError
    except EmptyFileError:
        print("The file is empty.")
    
    
    with open('NewChat.txt','r') as text:
        with open('NewChat.txt','w') as newText:
            lines=(removeWhitespace(line) for line in text)
            for line in lines:
                words=line.split(' ')
                words=list(map(fix,words))
                line=' '.join(words)
                newText.write(line)   
if __name__ == '__main__':
    main()
