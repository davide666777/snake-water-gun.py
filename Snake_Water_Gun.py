import random, playsound

def winning_music(): #plays with music
    win_music = ["anime wow.mp3","bruhh.mp3"]
    try:
        playsound.playsound(random.choice(win_music))
    except Exception as e:
        print(e)

def losing_music(): #plays with lossing music
    lose_music = ["Nope.mp3","fart.mp3"]
    try:
        playsound.playsound(random.choice(lose_music))
    except Exception as e:
        print(e)

def tie_music():
    try:
        playsound.playsound(random.choice("Awkward Cricket.mp3"))
    except Exception as e:
        print(e)

if __name__ == "__main__":
    print("Welcome to the Snake Water Gun game\n\n")

    attempts = 1
    your_point = 0
    computer_point = 0

    while (attempts <= 10):

        lst = ["snake","water","gun"]
        ran = random.choice(lst)

        inp = input("Enter your choice(snake/water/gun):")
        inp = inp.lower()

        if inp == ran:
            print("Tie")
            print(f"you chose {inp} and computer guess is {ran}")
            print("No body gets point\n")
            tie_music()

        elif inp == "snake" and ran == "water":
            your_point = your_point+1
            print(f"you chosed {inp} and computer guess is {ran}")
            print("the snake drank watr\n")
            print("you win this round")
            print("you got 1 point\n")
            winning_music()

        elif inp == "water" and ran == "snake":
            computer_point = computer_point + 1
            print(f"you choosed {inp} and computer guess is {ran}")
            print("the snake drank water\n")
            print("you lost this round")
            print("computer gets 1 point\n")
            losing_music()

        elif inp == "water" and ran == "gun":
            print(f"you chose {inp} and computer guess is {ran}")
            your_point = your_point + 1
            print("the gun snak in water\n")
            print("you win this round")
            print("you got 1 point\n")
            winning_music()

        elif inp == "gun" and ran == "water":
            print(f"you choosed{inp} and computer guess is {ran}")
            computer_point = computer_point + 1
            print("the gun snak in water\n")
            print("you lost this round")
            print("computer gets 1 point\n")
            losing_music()

        elif inp == "gun" and ran == "snake":
            print(f"you choosed {inp} and computer guess is {ran}")
            your_point = your_point + 1
            print("the snake was shot and ir dies\n")
            print("you won this round")
            print("you get 1 point\n")
            winning_music()

        elif inp == "snake" and ran == "gun":
            print(f"you choosed{inp} and computer guess is {ran}")
            computer_point = computer_point+1
            print("the snake was shoot and he died\n")
            print("you lost this round")
            print("computer gets 1 point\n")

        else:
            print("Invalid input\n")
            continue

        print("No. of guess left:{}".format(10 - attempts))
        attempts = attempts + 1

        if attempts>10:
            print("game over")


    print(f"your score:{your_point}\nComputer's score:{computer_point}")

    if computer_point > your_point:
        print("Computer won and you lost")

    elif computer_point < your_point:
        print("you won and computer lost")

    else:

        print("It was a tie")
        print("invalid")

    print(10 - attempts, "no. of guesses left")
    attemps = attempts + 1

    if attempts>10:
        print("game over")

if computer_point > your_point:
    print("Computer wins and you loose")

if computer_point < your_point:
    print("you win and the computer losses")

print(f"your point is {your_point} and computer point is {computer_point}")




