# Breathlyzer
# facebook puzzle challenge #4

import sys
import os
import logging

logging.basicConfig(level=logging.DEBUG)

#compare and return the diferences in a two words   
def compare_words(word1, word2):
    wrongs = 0 
    if word1 != word2:
        l = [word1, word2]
        m = map(None, *l)
        for letter in m:
            if letter[0]==letter[1]:
                continue
            else:
                wrongs += 1
    return wrongs

def load_words_list():
    file_path = './'
    #file_path = '/var/tmp/'
    file_name = file_path + 'twl06.txt'
    if os.path.exists(file_name): 
        return open(file_name)
    else: 
        logging.error('file does not exist!')
        return None
    
def main():
    if len(sys.argv) < 2 :
        print('Ops! please enter a file name')
        sys.exit()
    filename = sys.argv[1]
    logging.debug('filename is ' + filename)
    
    words_list = {}
    alphabeth = 'ABCDEFGHIJKLMNOPQRSTUVXYZW'
    for letter in alphabeth:
        words_list[letter] = []
    
    with load_words_list() as words_list_file:
        for letter in alphabeth:
            for line in words_list_file:
                if line.startswith(letter):
                    word = line.replace('\n', '').replace('\r', '')
                    words_list[letter].append(word.lower())
                else: 
                    break
    
    with open(filename) as f:
        words = f.read().split()
    
    soma = 0
    for word in words:
        possibles = words_list[word[0].upper()]
        l = []
        for p in possibles:
            l.append((compare_words(word, p), p))
        l.sort()
        print word, l[0]
        soma += l[0][0]
        
    print 'total de mudancas', soma
        
        

if __name__=='__main__':
    main()
