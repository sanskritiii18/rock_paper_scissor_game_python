import random
#this is a basic rock,paper,scissor game
#functions and parameters used
#if else condition is used

#WINNING CONDITIONS
def option(c,d,player1,player2):
    if player1 == player2:
        print("its a tie")
    elif player1 =="rock" and player2=="paper":
        print(f"{c} wins")
    elif player1 =="rock" and player2=="scissor":
        print(f"{c} wins")
    elif player1 =="scissor" and player2=="rock":
        print(f"{d} wins")
    elif player1 =="scissor" and player2 =="paper":
        print(f"{c} wins")
    elif player1=="paper" and player2=="scissor":
        print(f"{d} wins")
    elif player1 =="paper" and player2=="rock":
        print(f"{c} wins")
    else:
        print("enter a valid option")


#if both selected  players are users
def bothplayers(a,b):
    print("player vs player")
    options = ('rock', 'paper', 'scissor')
    print("options: rock , paper , scissor")
    print("player1 enter options")
    value1 = input()
    print("player 2 enter from options")
    value2 = input()
    option(a,b,value1,value2)
#if its computer vs player
def playervscomp(a,b):
      if player1 == "player":
            options = ('rock', 'paper', 'scissor')
            print("options: rock , paper , scissor")
            print("player1 enter options")
            value1 = input()
            computer = random.choice(options)
            print(computer)
            value2 = computer
            option(a,b,value1,value2)
      else:
            options = ('rock', 'paper', 'scissor')
            computer = random.choice(options)
            print(f"computer:{computer}")
            value1 = computer
            options = ('rock', 'paper', 'scissor')
            print("options: rock , paper , scissor")
            print("player2 enter options:")
            value2 = input()
            option(a,b,value1,value2)



#if both selected players are computer
def compvscomp(a,b):
    print("computer vs computer")
    options = ('rock', 'paper', 'scissor')
    value1 = random.choice(options)
    value2 = random.choice(options)
    print(value1)
    print(value2)
    option(a,b,value1,value2)


#number of players can be two
print("Welcome to the game")
print("choose player 1 ")
print("1.player"
       "\n2.computer")
player1= str(input())
print("choose player 2 ")
print("1. player"
      "\n2. computer")
player2= str(input())

#depending upon selected players user input pattern changes
if (player1=="player") and (player2 =="player"):
 bothplayers("player1","player2")
elif (player1 =="player") or (player2 =="player"):
    if player1=="player":
        playervscomp("player","computer")
    else:
        playervscomp("computer","player")
elif (player1=="computer") and (player2=="computer"):
 compvscomp("computer1","computer2")
else:
 print("enter valid options")






