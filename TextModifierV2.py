
import re
from os import stat


class EmptyFileError(Exception):
        pass
    
    
COLORS={'green','yellow','orange','blue','white','black','grey','pink','red'}
SLANGS={'sry':'sorry','pls':'please','u':'you','msg':'message','dw':"don't worry","gl":'good luck'}

def fix(word):  #A fucntion that modifies or replaces the word.
    clean_word=re.sub('[,?!@#$%^&*()-+=\']','',word)#the word without marks
    if clean_word in COLORS :
        return word.replace(clean_word,len(clean_word)*'#')  #replaces only the word itself
    elif clean_word in SLANGS:
        return  word.replace(clean_word,SLANGS[clean_word])
    return Normal(word)
    

def Normal(word):  #Replaces all excess upper letters with lower letters
    clean_word=re.sub('[,?!@#$%^&*()-+=\']','',word)
    firstUpper=True if word[0].isupper() else False
    Nword=clean_word.lower() if not firstUpper else clean_word[0]+clean_word[1:].lower()
    return word.replace(clean_word,Nword)

def removeWhitespace(line):  #removes all the white space from a line
    line=line.split(' ')
    line=list(dict.fromkeys(line))
    if '' in line:
        line.remove('')
    return ' '.join(line)

def main():
    try:
        if stat('Chat.txt').st_size==0:  #check if the file is empty or not
            raise EmptyFileError
    except EmptyFileError:
        print("The file is empty.")
    
    
    with open('NewChat.txt','r') as text:
        with open('NewChat.txt','w') as newText:
            lines=(removeWhitespace(line) for line in text)  #Remove white space from the text
            for line in lines:
                words=line.split(' ')
                words=list(map(fix,words))  #create a list of the fixed words
                line=' '.join(words)  #gather the words to a line with ' ' between each word.
                newText.write(line)   #add the line to the new file.
if __name__ == '__main__':
    main()
