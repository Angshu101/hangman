import random
def print_design(tries,word):
    if(tries==0):
        print("______\n"
               "|    |\n"
               "|\n"
               "|\n"
               "|\n"
               "|\n"
               "|_______\n")
    elif(tries==1):
        print("______\n"
               "|    |\n"
               "|    O \n" 
               "|\n"
               "|\n"
               "|\n"
               "|_______\n")
    elif(tries==2):
        print("______\n"
               "|    |\n"
               "|    O \n" 
               "|    |  \n"
               "|\n"
               "|\n"    
               "|_______\n")
    elif(tries==3):
        print("______\n"
               "|    |\n"
               "|    O \n" 
               "|   \| \n"
               "|    |  \n"
               "|\n"
               "|_______\n")
    elif(tries==4):
        print("______\n"
               "|    |\n"
               "|    O \n" 
               "|   \|/ \n"  
               "|    |   \ n"
               "|\n"    
               "|_______\n")
    elif(tries==5):
        print("______\n"
               "|    |\n"
               "|    O \n" 
               "|   \|/ \n"
               "|    |   \n"
               "    /|    \n"
               "|_______\n")
    elif(tries==6):
        print("______\n"
               "|    |\n"
               "|    O \n" 
               "|   \|/\n"
               "|    |    \n"
               "|   / \    \n"
               "|_______\n")
        print("\n")
        print("The correct word is %s.\n" %word)
        print("\n YOu Lost")
        print("press 1 if you like to continue")
        again=input("> ")
        again=again.lower
        if again == "yes":
            hangman()
        return()
    
def randomword():
   
    file=open('jum.txt','r')
    words=file.readlines()
    
    myword=random.choice(words)
   
    myword=str(myword).strip("")
    myword=str(myword).strip("''")
    myword=str(myword).strip("\n")
    myword=str(myword).strip("\r")
    myword=myword.lower()
    print(myword)
    return myword
def hangman():
        tries=0
        word=randomword()
        wordlist=list(word)
        blanks="-" * len(word)
        blanks_list=list(blanks)
        new_blankslist=list(blanks)
        guess_list=[]
        print('Lets play hangman !\n')
        print_design(tries,word)
        print(" ".join(blanks_list))
        print('Guess a letter:')
        while tries < 6:
            guess=input("> ")
            guess=guess.lower()
            if len(guess)>1:
                print(" Please Enter one letter at a time")
            elif guess ==" ":
                print("Enter a Letter")
            elif guess in guess_list:
                 print("Already guessed! here is what you have guessed")
                 print(' '.join(guess_list))
            else:
                guess_list.append(guess)
                i=0
                while i<len(word):
                  if guess==word[i]:
                     new_blankslist[i]=wordlist[i]
                  i=i+1
                


                if new_blankslist == blanks_list:
                    print("oops letter is in here")
                    tries=tries+1
                    print_design(tries,word)


                    if tries < 6:
                     print(" Guess again")
                     print(' '.join(blanks_list))
                       
                        
                elif wordlist!=blanks_list:
                     blanks_list=new_blankslist[:]
                     print(' '.join(blanks_list))
                     if wordlist==blanks_list:
                         print("\n YOU Win \n")
                         print("Do you want to play again,press 1 for yes 2 for no ")
                         again=input(">")
                         if again== "yes":
                             hangman()
                         quit()
                     else:
                         print(" Great guess")
hangman()  