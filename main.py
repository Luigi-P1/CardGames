import beforeHandAction
import duringHand
import postHandActions

stack: int = int(input('What is your starting stack? '))
starting_stack = stack
play = "Y"
while stack > 0 and play == "Y":
    [P_hand, D_hand, P_total, D_total, P_ace_count, D_ace_count, action, deck] = beforeHandAction.resetVariables()
    bet = beforeHandAction.betPlacement(stack)
    [deck, P_hand, P_total, P_ace_count, D_hand, D_total, D_ace_count] = duringHand.setInitialHand(deck, P_hand,
                                                                                                   P_total, P_ace_count,
                                                                                                   D_hand, D_total,
                                                                                                   D_ace_count)
    print("Your hand is ", P_hand, "   (", P_total, ") \nDealer's hand is", D_hand)
    if P_total == 21 and len(P_hand) == 2:
        if str(D_hand[0][0]) == "A":
            evenMoney = duringHand.evenMoneyOffer()
    else:
        double = duringHand.doubleDownQuestion(stack, bet)
        if double:
            [deck, P_hand, P_total, P_ace_count, bet] = duringHand.doubleDown(bet, deck, P_hand, P_total, P_ace_count)
            action = "S"
        [deck, P_hand, P_total, P_ace_count, D_hand, action] = duringHand.handAction(deck, P_hand, P_total, P_ace_count,
                                                                                     D_hand, action)
        if P_total > 21:
            P_total = 0
            print("Bust!!")
    print("Dealer's hand:")
    while D_total <= 16:
        [deck, D_hand, D_total, D_ace_count] = beforeHandAction.addCardToHand(deck, D_hand, D_total, D_ace_count)
        print(D_hand, D_total)
    if D_total > 21:
        D_total = 0
    outcome = postHandActions.compareHands(P_total, P_hand, D_total, D_hand)
    stack = postHandActions.payOut(stack, bet, outcome)
    print("Money in £", stack)
    play = postHandActions.anotherHand(stack)
postHandActions.goodBye(starting_stack, stack)
