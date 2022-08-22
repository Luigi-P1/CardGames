import random


def makeDeck():
    suits = ["C", "H", "S", "D"]
    values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck = []
    for suit in suits:
        for value in values:
            card = value + suit
            deck.extend([card])
    return deck


def addCardToHand(deck, hand, handTotal, aceTotal):
    cardIndex = int(random.randint(0, len(deck) - 1))
    card = deck[cardIndex]
    hand.extend([card])
    deck.remove(card)
    handTotal, aceTotal = handValueUpdate(card, handTotal, aceTotal)
    [handTotal, aceTotal] = AceCheck(handTotal, aceTotal)
    return deck, hand, handTotal, aceTotal


def handValueUpdate(card, handTotal, aceTotal):
    value = str(card[0])
    if value in ["K", "Q", "J", "1"]:
        handTotal += 10
    elif value == "A":
        handTotal += 11
        aceTotal += 1
    else:
        handTotal += int(value)
    return handTotal, aceTotal


def AceCheck(total, ace_count):
    if total >= 22 and ace_count >= 1:
        total -= 10
        ace_count -= 1
    return [total, ace_count]


def resetVariables():
    P_hand = []
    D_hand = []
    P_total = 0
    D_total = 0
    P_ace_count = 0
    D_ace_count = 0
    action = "H"
    deck = makeDeck()
    return [P_hand, D_hand, P_total, D_total, P_ace_count, D_ace_count, action, deck]


def betPlacement(stack):
    print("Your stack is £", stack)
    bet = input("Place your bet!(£1 min)")
    bet = float(bet)
    while bet < 1 or bet > stack:
        print("You have £", stack, "remaining")
        bet = int(input("Error!! Your bet has to be at least £1 and less then the amount of money remaining"))
    return bet
def eggs():
    print('eggs')