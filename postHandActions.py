def compareHands(P_total, P_hand, D_total, D_hand):
    outcome = "Draw!"
    if P_total != 21 or len(P_hand) != 2:
        if P_total < D_total or P_total == 0 or (len(D_hand) == 2 and D_total == 21 and (len(P_hand) != 2 or
                                                                                         P_total != 21)):
            outcome = "Lose!"
        elif P_total > D_total:
            outcome = "Win!"
    # elif evenMoney:
    #     outcome = "Even Money!"
    elif P_total == 21 and len(P_hand) == 2 and (len(D_hand) != 2 or D_total != 21):
        outcome = "BlackJack!!!"

    return outcome


def payOut(stack, bet, outcome):
    print(outcome)
    if outcome == "Lose!":
        stack -= bet
    elif outcome == "Win!":
        stack += bet
    elif outcome == "BlackJack!!!":
        stack += 1.5 * bet
    return stack


def anotherHand(stack):
    if stack > 0:
        play = str(input("Play another hand?(Y/N)"))
        while play != "N" and play != "Y":
            play = str(input("Error!! Please input  valid response: \n'Y' to play another hand\n'N' to stop"))
    else:
        play = "N"
    return play


def goodBye(starting_stack, stack):
    if starting_stack > stack:
        print("Thanks for playing\nYou lost £{0}\nGoodbye".format(starting_stack - stack))
    elif stack > starting_stack:
        print("Thanks for playing\nYou won £{0}\nGoodbye".format(stack - starting_stack))
    else:
        print("You broke even \nGoodbye")
