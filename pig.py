# Nathan Chau
# 2/5/2021
# Pig game

import random

if __name__ == "__main__":
    # players name
    player1, player2, target_score = input("").split()

    # players score
    player1_score = 0
    player2_score = 0
    target_score = int(target_score)

    print("Competitors: " + player1 + " vs " + player2)

    print("....................")
    print(str(player1) + ": " + str(player1_score) + ", " + str(player2) + ": " + str(player2_score))
    print("....................")

    player1_score = 0
    player2_score = 0

    choicedict = dict()
    choicedict["Side"] = 0
    choicedict["Razorback"] = 5
    choicedict["Trotter"] = 5
    choicedict["Snouter"] = 10
    choicedict["Leaning Jowler"] = 15

    # player 1 turn
    print("Your turn, " + player1)
    print('')
    choice = str(input("    Roll or Pass? "))

    while choice != "PASS" and choice != "pass" and choice != "Pass":
        # 3% to mount
        # 7% to touch

        # side(no dot) = 35
        # side(dot) = 30
        # razorback = 22
        # trotter = 9
        # snouter = 3
        # leaning jowler = 1

        # check for touching
        roll_check = random.randint(1, 100)
        if roll_check <= 3:
            print("     You rolled a Piggyback!")
            exit(0)
        elif roll_check <= 10:
            print("     You rolled an Oinker!")
            player1_score = 0
        else:
            choiceList = ["Side", "Razorback", "Trotter", "Snouter", "Leaning Jowler"]
            choice_pair = random.choices(choiceList, weights=(65, 22, 9, 3, 1), k=2)
            # TODO pairs
            if choice_pair[0] == choice_pair[1]:
                if choice_pair[0] == "Side":
                    print("     You rolled a Double Sider")
                    print("     You earned 1 point")
                    player1_score += 1
                elif choice_pair[0] == "Razorback":
                    print("     You rolled a Double Razorback")
                    print("     You earned 20 points")
                    player1_score += 20
                elif choice_pair[0] == "Trotter":
                    print("     You rolled a Double Trotter")
                    print("     You earned 20 points")
                    player1_score += 20
                elif choice_pair[0] == "Snouter":
                    print("     You rolled a Double Snouter")
                    print("     You earned 40 points")
                    player1_score += 40
                elif choice_pair[0] == "Leaning Jowler":
                    print("     You rolled a Double Leaning Jowler")
                    print("     You earned 20 points")
                    player1_score += 60

            # TODO mixed combo
            else:
                print("     You rolled a Mixed Combo: {} and {}".format(choice_pair[0], choice_pair[1]))
                player1_score += choicedict[choice_pair[0]]
                player1_score += choicedict[choice_pair[1]]

        if player1_score > target_score:
            print("Player 1 passed the score.")
            break
        print("     You earned " + str(player1_score) + " points")
        choice = str(input("        Roll or Pass? "))

    # player 2 turn
    print("Your turn, " + player2)
    print('')
    choice = str(input("Roll or Pass? "))

    while choice != "PASS" and choice != "pass" and choice != "Pass":
        # check for touching
        roll_check = random.randint(1, 100)
        if roll_check <= 3:
            print("     You rolled a Piggyback!")
            exit(0)
        elif roll_check <= 10:
            print("     You rolled an Oinker!")
            print("     You lose all of your points")
            player2_score = 0
        else:
            choiceList = ["Side", "Razorback", "Trotter", "Snouter", "Leaning Jowler"]
            choice_pair = random.choices(choiceList, weights=(65, 22, 9, 3, 1), k=2)
            # TODO pairs
            if choice_pair[0] == choice_pair[1]:
                if choice_pair[0] == "Side":
                    print("     You rolled a Double Sider")
                    print("     You earned 1 point")
                    player2_score += 1
                elif choice_pair[0] == "Razorback":
                    print("     You rolled a Double Razorback")
                    print("     You earned 20 points")
                    player2_score += 20
                elif choice_pair[0] == "Trotter":
                    print("     You rolled a Double Trotter")
                    print("     You earned 20 points")
                    player2_score += 20
                elif choice_pair[0] == "Snouter":
                    print("     You rolled a Double Snouter")
                    print("     You earned 40 points")
                    player2_score += 40
                elif choice_pair[0] == "Leaning Jowler":
                    print("     You rolled a Double Leaning Jowler")
                    print("     You earned 20 points")
                    player2_score += 60

            # TODO mixed combo
            else:
                print("     You rolled a Mixed Combo: {} and {}".format(choice_pair[0], choice_pair[1]))
                player2_score += choicedict[choice_pair[0]]
                player2_score += choicedict[choice_pair[1]]

        if player2_score > target_score:
            print("Player 2 passed the score.")
            break
        print("     You earned " + str(player2_score) + " points")
        choice = str(input("        Roll or Pass? "))

    # result screen
    print("....................")
    print("GAME OVER")
    print(str(player1) + ": " + str(player1_score) + ", " + str(player2) + ": " + str(player2_score))

    # if player 1 has the higher score
    if player1_score > player2_score:
        print(player1 + " wins!")

    # if player 2 has the higher score
    elif player1_score < player2_score:
        print(player2 + " wins!")

    # if tie
    elif player1_score == player2_score:
        print("Tie!")