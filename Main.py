import re
from os import stat
class EmptyFileError(Exception):
        pass


def removeWhitespace(line):
    line=line.split(' ')
    line=list(dict.fromkeys(line))
    if '' in line:
        line.remove('')
    return line

def main():
    CURSES={'green','yellow','orange','blue','white','black','grey','pink','red'}
    SLANGS={'sry':'sorry','pls':'please','u':'you','msg':'message','dw':"don't worry","gl":'good luck'}
    try:
        if stat('Chat.txt').st_size==0:
            raise EmptyFileError
    except EmptyFileError:
        print("The file is empty.")

    with open('Chat.txt','r+') as text:
        with open('NewChat.txt','w') as newText:
            newline=''
            for line in text.readlines():#splitting the text to lines
                for word in removeWhitespace(line):#checking words in each line
                    newline=newline+word+' '
                    firstUpper=False
                    if word[0].isupper():
                        firstUpper=True
                    word=word.lower().strip()
                    word=re.sub('[,?!@#$%^&*()-+=\']','',word)##removing marks from the word string
                    if word in CURSES :
                        newline=newline.replace(word,len(word)*'#')#replacing the word with '#'
                    elif word in SLANGS:
                        # Replacing the first letter to upper letter if it was upper
                        newWord=SLANGS[word] if not firstUpper else SLANGS[word].replace(SLANGS[word][0],SLANGS[word][0].upper())
                        newline = newline.replace(word, newWord) if not firstUpper else newline.replace(word.upper(), newWord) #replacing the slang with the word

                newText.write(newline.strip(' '))#removing excess white space from the end of the line
                newline=''

if __name__ == '__main__':
    main()