import random
#this is a basic rock,paper,scissor game
#functions and parameters used
#if else condition is used
count1 =0
count2= 0
#WINNING CONDITIONSā
def option(c, d, player1, player2, count2=None, count1=None):
        if player1 == player2:
            print("its a tie")
        elif player1 =="rock" and player2=="paper":
            count2 +=1
        elif player1 =="rock" and player2=="scissor":
            count1 +=1
        elif player1 =="scissor" and player2=="rock":
            count2 +=1
        elif player1 =="scissor" and player2 =="paper":
            count1 +=1
        elif player1=="paper" and player2=="scissor":
            count2 +=1
        elif player1 =="paper" and player2=="rock":
            count1 +=1
        else:
            print("enter a valid option")
        return count1,count2

#if both selected  players are users
def bothplayers(a,b):
    print("player vs player")
    options = ('rock', 'paper', 'scissor')
    print("options: rock , paper , scissor")
    print("player1 enter options")
    value1 = input()
    print("player 2 enter from options")
    value2 = input()
    option(a,b,value1,value2,count1,count2)
    return count1,count2
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
round =int(input("enter number of rounds"))

#depending upon selected players user input pattern changes
if (player1=="player") and (player2 =="player"):
    name1 = input("Enter your name: ")
    print("You entered:", name1)
    name2 = input("Enter your name: ")
    print("You entered:", name2)
    for x in range(round):
     bothplayers(name1,name2)
     if count1>count2:
         print(f"{name1} wins")
     else:
         print(f"{name2} wins")
elif (player1 =="player") or (player2 =="player"):
    if player1=="player":
        name1 = input("Enter your name: ")
        print("You entered:", name1)
        playervscomp(name1,"computer")
    else:
        name1 = input("Enter your name: ")
        print("You entered:", name1)
        playervscomp("computer",name1)
elif (player1=="computer") and (player2=="computer"):
 compvscomp("computer1","computer2")
else:
 print("enter valid options")






