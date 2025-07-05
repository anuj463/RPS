# Python project to implement Rock-Paper-Scissor game 
# Author: Anuj Savant
#Date: 5/6/25

player1=0
player2=0
while True:
    print("Menue:")
    print("1.Rock\n2.paper\n3.Scissor\n4.Exit")
    op1 = int(input("Enter option 1:"))
    op2 = int(input("Enter option 2:"))

    if op1 == 1 and op2 ==2:
        player2 = player2 +1
    elif op1 == 1 and op2 == 3:
        player1 = player1 + 1
    elif op1 == 2 and op2 == 1:
        player1 = player1 + 1
    elif op1 ==2 and op2 == 3:
        player2 = player2 +1
    elif op1 == 3 and op2 ==1:
        player2 = player2  + 1
    elif op1 == 3 and op2 == 2:
        player1 = player1 + 1
    elif op1 == 1 and op2 ==1:
        player1 = player1 + 0
        player2 = player2 +0
    elif op1 ==2 and op2 ==2 :
        player1 = player1 + 0
        player2 = player2 +0
    elif op1 == 3 and op2 == 3:
        player1 = player1 + 0
        player2 = player2 +0
    elif op1 ==4 and op2 ==4:
         print("Game Over")
         break
    else: print("Invalid Option")


    print("Player 1 score:", player1)
    print("Player 2 score:",player2)

    if player1 >player2:
        print("Player 1 wins")    
    elif player1 == player2:
        print("Match Draw")
    else:
        print("Player 2 wins")
