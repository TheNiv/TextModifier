import re
from os import stat
class EmptyFileError(Exception):
    def __init__(self):
        pass


def main():
    CURSES=['green','yellow','orange','blue','white','black','grey','pink','red']
    try:
        if stat('Chat.txt').st_size==0:
            raise EmptyFileError
    except EmptyFileError:
        print("The file is empty.")

    with open('Chat.txt','r+') as text:
        with open('NewChat.txt','w') as newText:
            newline=''
            for line in text.readlines():#splitting the text to lines
                for word in line.split(' '):#checking words in each line
                    newline=newline+word+' '
                    word=word.lower().strip()
                    word=re.sub('[,?!@#$%^&*()-+=\']','',word)#removing marks from the word string
                    if(word in CURSES):
                        newline=newline.replace(word,len(word)*'#')#replacing the word with '#'
                newText.write(newline.strip(' '))#removing excess white space from the line
                newline=''

if __name__ == '__main__':
    main()