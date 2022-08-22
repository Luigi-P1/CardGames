import beforeHandAction


def setInitialHand(deck, P_hand, P_total, P_ace_count, D_hand, D_total, D_ace_count):
    for i in range(3):
        if i <= 1:
            [deck, P_hand, P_total, P_ace_count] = beforeHandAction.addCardToHand(deck, P_hand, P_total, P_ace_count)
        elif i == 2:
            [deck, D_hand, D_total, D_ace_count] = beforeHandAction.addCardToHand(deck, D_hand, D_total, D_ace_count)
    return [deck, P_hand, P_total, P_ace_count, D_hand, D_total, D_ace_count]


def handAction(deck, P_hand, P_total, P_ace_count, D_hand, action):
    while action == "H" and P_total < 21:
        action = str(input("Would you like to hit (H) or stand (S)"))
        while action != "H" and action != "S":
            action = str(input("Error!! Enter H to hit or S to stand"))
        if action == "H":
            [deck, P_hand, P_total, P_ace_count] = beforeHandAction.addCardToHand(deck, P_hand, P_total, P_ace_count)
            print("Your hand is ", P_hand, "   (", P_total, ") \nDealer's hand is", D_hand)
    return [deck, P_hand, P_total, P_ace_count, D_hand, action]


def doubleDownQuestion(stack, bet):
    doubleQuestion = str(input("do you want to double down? (Y/N)"))
    double = False
    while doubleQuestion != "Y" and doubleQuestion != "N":
        doubleQuestion = str(input("error!! If you want to double down, type 'Y' if not 'N'"))
    if doubleQuestion == "Y" and stack >= (2 * bet):
        double = True
    elif doubleQuestion == "Y" and (2 * bet) > stack:
        print("you can't double down due to in sufficient funds")
    return double


def doubleDown(bet, deck, hand, handTotal, aceTotal):
    bet *= 2
    [deck, hand, handTotal, aceTotal] = beforeHandAction.addCardToHand(deck, hand, handTotal, aceTotal)
    print("Your hand is ", hand, "   (", handTotal, ")")
    return [deck, hand, handTotal, aceTotal, bet]


def evenMoneyOffer():
    evenMoney = str(input("Would you like even money? (Y/N)"))
    while evenMoney != "Y" and evenMoney != "N":
        evenMoney = str(input("error!! If you want to take even money, type 'Y' if not 'N'"))
    if evenMoney == "Y":
        return True
    else:
        return False


def isBlackjack(hand_total, player_hand):
    return hand_total == 21 and len(player_hand)


def bust(hand_total):
    if hand_total > 21:
        hand_total = 0
    return hand_total
