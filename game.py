# snake water gun game

items = ["Snake","Water","Gun"]
import random
# print(computer_choose)

player = input("Enter Your Name ?\n")

computer_score = 0
user_score = 0

while True:
    try:
        computer_choose = random.choice(items)

        print("\nWhat is Your Choice ?")
        print("Snake\nWater\nGun")
        user_choose = input().capitalize()

        if computer_choose == "Snake" and user_choose == "Water":
            print("You Got 1 point.\n")
            user_score = user_score + 1

        elif computer_choose == "Water" and user_choose == "Snake":
            print("Computer Got 1 point.\n")
            computer_score = computer_score + 1

        elif computer_choose == "Water" and user_choose == "Gun":
            print("Computer Got 1 point.\n")
            computer_score = computer_score + 1

        elif computer_choose == "Gun" and user_choose == "Water":
            print("You Got 1 point.\n")
            user_score = user_score + 1

        elif computer_choose == "Gun" and user_choose == "Snake":
            print("Computer Got 1 point.\n")
            computer_score = computer_score + 1

        elif computer_choose == "Snake" and user_choose == "Gun":
            print("You Got 1 point.\n")
            user_score = user_score + 1

        elif computer_choose == user_choose:
            print("Both Same.\nYou and Computer both Get 1 point.\n")
            computer_score = computer_score + 1
            user_score = user_score + 1

        else:
            print("You Did't Choose anything So 1 point goes to Computer..\n")
            computer_score = computer_score + 1


    # loop break ho jayega jab user ya computer ka score 10 ho jayega

        if computer_score == 10 or user_score == 10:
            if computer_score == user_score:
                print(f"{player} Game Draw your and computer's point are same..")

            elif user_score == 10:
                print(f"Congratulations {player} You Win this Game.")
                print(f"You Got {user_score} Points, And\n Computer Got {computer_score} Points..")

            else:
                print(f"{player} You Loose the Game.")
                print(f"Computer Got {computer_score} Points, And\nYou Got {user_score} Points..")


            break
    
    except:
        print("Invaild Input.")
