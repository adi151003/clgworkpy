###Write a guessing game program -
###Input an integer number from the user. If the number is odd and lies between 10 and 20 then
###display the user - “You won the game!” and don’t ask for the number again. Users should get a
###maximum of 3 chances to win. If in all three attempts, the user fails, display the user - “You lost
###the game!”
###Don’t use exit(), break, continue keyword in the program.
lives = 0
while lives <3:
    a = int(input("enter a number"))

    if (a%2 != 0 and 10< a <20):
        lives = 5
        print("You won the game!")
    else:
        lives +=1
        if lives == 3:
            print("You lost the game")
