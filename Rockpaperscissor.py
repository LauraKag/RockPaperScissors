# -*- coding: utf-8 -*-

#%%

#Rock paper scissors: Implement a function that checks who from
#two players won a rock paper scissors game. The function should take
#two parameters, the first for what player 1 used, the second for what
#player 2 used, and return who won the match, either player 1 or player two.

#Create tests for this function too!

def rockpaperscissors(Playerone,Playertwo):
    
    if Playerone == "Scissors" and Playertwo == "Paper":
        return "Player one won"
    elif Playerone == "Scissors" and Playertwo == "Rock":
        return "Player two won"
    elif Playerone == "Rock" and Playertwo == "Scissors":
        return "Player one won"
    elif Playerone == "Rock" and Playertwo == "Paper":
        return "Player two won"
    elif Playerone == "Paper" and Playertwo == "Rock":
        return "Player one won"
    elif Playerone == "Paper" and Playertwo == "Scissors":
        return "Player two won"
    elif Playerone==Playertwo:
        return "No one wins, try again!"
    
    
