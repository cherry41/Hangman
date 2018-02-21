import time
class Hangman():
    def __init__(self):
        print("Welcome to Hangman!!Are you ready to be a dead man?")
        print("\n1.Yes,take me in\n 2.No,seems scary!!\n")
        choice=int(input("Choose\n"))
        if choice==1:
            print("Loading....\n")
            time.sleep(0.5)
            self.display_para()
        elif choice==2:
            print("see you later")
            exit()
        else:
            print("Uh oh!! Wrong typed!!! Try again\n\n")
            self.__init__()

    def display_para(self):
        print("Here gathers the crowd to see real justice.")
        print("The thing is ,You aren't a criminal.")
        print("You just came at a wrong place at a wrong time.")
        print("well you got a chance to live. All you have to do")
        print("is to guess the right word. But wait, SIX wrong ")
        print("guesses and you are A DEAD MAN!!\n\n")
        self.start_game()

    def start_game(self):
        guesses=0
        attempts=6
        chars_used=''
        word="admin"
        progress = ['', '', '', '', '']

        while guesses<6:
            guess=input("Guess a letter")

            if  guess in  word and guess not in chars_used:
                print("your guess was right")
                chars_used+=','+guess
                self.hangman_picture(guesses)
                print("Here's your Progresse:",self.curr_progress(guess,word,progress))
                print("letters Used:"+chars_used)
                
                
            elif guess not in word and guess not in chars_used:
                guesses+=1
                print("Your guess was wrong")
                chars_used+=','+guess
                self.hangman_picture(guesses)
                print("Here's is your progress:"+"".join(progress))
                print("letters Used:"+chars_used)
            else:
                print("thats a wrong letter")
                print("try again!")
    def hangman_picture(self,guesses):
        if guesses == 0:
            print("______     ")
            print("|    |     ")
            print("|          ")
            print("|          ")
            print("|          ")
            print("|          ")
        elif guesses == 1:
            print("______     ")
            print("|    |     ")
            print("|    0     ")
            print("|          ")
            print("|          ")
            print("|          ")
        elif guesses == 2:
            print("______     ")
            print("|    |     ")
            print("|    0     ")
            print("|   /      ")
            print("|          ")
            print("|          ")
        elif guesses == 3:
            print("______     ")
            print("|    |     ")
            print("|    0     ")
            print("|   /|     ")
            print("|          ")
            print("|          ")
        elif guesses == 4:
            print("_____      ")
            print("|    |     ")
            print("|    0     ")
            print("|   /|\    ")
            print("|          ")
            print("|          ")
        elif guesses == 5:
            print("_____      ")
            print("|    |     ")
            print("|    0     ")
            print("|   /|\    ")
            print("|   /      ")
            print("|          ")
        else:
            print("_____      ")
            print("|    |     ")
            print("|    0     ")
            print("|   /|\    ")
            print("|   / \    ")
            print("|          ")
            print("GAME OVER")
    def curr_progress(self,guess,word,progress):
        i=0
        while i<len(word):
            if guess==word[i]:
                progress[i]=guess
                i+=1

            else:
                i+=1
                
                
        

        return "".join(progress)

            
        
    
game=Hangman()
