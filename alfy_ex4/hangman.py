import random

from hang_man_init import logo
from hang_man_init import stages

wrong_list = []

def load_words(file='words.txt'):

    words = []
    f_words = open(file)
    for line in f_words:
        word = line.strip()
        if(word.isalpha()):
            words.append(line.strip())
    f_words.close()
    return words


def get_random_word(words_list):

    return random.choice(words_list)

def get_word_blanklist(word):
    

    blank_list=[]
    
    for word_len in range(len(word)):
        blank_list.append('__')
    
    return (word,blank_list)


def draw_hang_man(user,word,blank,counter):
    
    global wrong_list
    for index,letter in enumerate(word):
        if(user==letter):
            blank[index]=user
            
    if(word.find(user)==-1):
        wrong_list.append(user)
        print(stages[counter])
        print(wrong_list)
        counter+=1
    
    
    if(counter==6):
        print(f"Sorry you did not guess the word correctly the correct word was {word}")
        print(stages[counter])
        return(counter)
    
    final="".join(blank)
    
    if(word==final):
        print("Congratulations you have guess the word correctly")
        print('The word is ')
        print(word)
        counter=6
        return(counter)
        
    else:
       print(blank)
       return(counter)

def main():
    
    print(logo)
    print("Welcome to Hangman")
    words = load_words()
    rand_word = get_random_word(words)
    [answer,blank]=get_word_blanklist(rand_word)
    stages.reverse()
    counter=0
    
    while counter < 6:
        user_input=input("Please select the character:")
        char=user_input.lower()
        counter=draw_hang_man(char, answer, blank, counter)
        
    print("Game over ")
    
if __name__ == '__main__':
    main()
    

    