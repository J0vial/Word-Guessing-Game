
def play(x):
    if x=='yes':
        guess()
    
    
def guess():
    word = input('Enter the word you want as a game: ')
    word_list = [i for i in word] 
    
    length_word = len(word)
    guess_have = 5
    print(f'You are allowed to make 5 incorrect guesses')
    hidden_word_slash =''
    for i in range(length_word):
        hidden_word_slash+='-'
    print('The current guess is ',hidden_word_slash) 
    for j in range(5000):
        if '-' in hidden_word_slash:
            guess_word = input('Please enter your guesss letter: ')
            if guess_have!=1:
                
                if guess_word in word:
                    print('Good Job!')
                    index_num_of_correct  = []
                    for m in range(len(word_list)):
                        if guess_word == word_list[m]:
                            index_num_of_correct.append(m)
                    
                    for l in index_num_of_correct:
                        
                        hidden_word_slash= hidden_word_slash[:l]+guess_word+hidden_word_slash[l+1:]
                    print(f'You are allowed to make {guess_have} incorrect guesses')       
                    print('The current guess is :', hidden_word_slash)
                else:
                    
                    guess_have-=1
                    print('Wrong guess, try again')
                    print(f'You are allowed to make {guess_have} incorrect guesses')
                    
            else:
                print('Hard Luck, the computer won.')
                x = input('Would you like to retry? (yes/no)')
                if x =='yes':
                    guess()
                    break
                else:
                    print('Thanks for playing the game')
                    break       
                    
        else:
            print('Congratulation! You Won')
            x = input('Would you like to retry? (yes/no)')
            if x =='yes':
                guess()
                break
            else:
                print('Thanks for playing the game')
                break
           
        
            
            
            
        
        
    
    
guess()
    
    
       


