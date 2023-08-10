import random
import os

class blackjack:
    # Creating the Deck to Draw from
    deck = ["clubs_two","clubs_three","clubs_four","clubs_five","clubs_six","clubs_seven","clubs_eight","clubs_nine","clubs_ten","clubs_jack","clubs_queen","clubs_king","clubs_ace","diamonds_two","diamonds_three","diamonds_four","diamonds_five","diamonds_six","diamonds_seven","diamonds_eight","diamonds_nine","diamonds_ten","diamonds_jack","diamonds_queen","diamonds_king","diamonds_ace","hearts_two","hearts_three","hearts_four","hearts_five","hearts_six","hearts_seven","hearts_eight","hearts_nine","hearts_ten","hearts_jack","hearts_queen","hearts_king","hearts_ace","spades_two","spades_three","spades_four","spades_five","spades_six","spades_seven","spades_eight","spades_nine","spades_ten","spades_jack","spades_queen","spades_king","spades_ace"]
    deck_value = [2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11,2,3,4,5,6,7,8,9,10,10,10,10,11]
    deck_card = ["two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace","two","three","four","five","six","seven","eight","nine","ten","jack","queen","king","ace"]
    # The aces to later check if it should count as 11 or 1
    aces = ['clubs_ace', 'diamonds_ace', 'hearts_ace', 'shades_ace']
    
    # We ask for Purse
    os.system('cls')
    purse = float(input('How Much do you have to play with?: '))
    
    # Well it just clears the console to look better
    def clear_console():
        os.system('cls')
    
    def play_again():
            # We check if the player got money left
            if blackjack.purse <= 0:
                print('Your Broke.')
                exit()
            # Let Him choose if he wants to play again
            play_again_options = ['yes', 'no']
            play_again = input(f'Do You wanna play again, you have {blackjack.purse}?: ')
            while play_again.lower() not in play_again_options:
                print("Please deside yes or no!")
                play_again = input('Do You wanna play again?: ')
            if play_again.lower() == 'yes':
                blackjack.run()
            elif play_again.lower() == 'no':
                exit()

    def blackjack_win(P_points, D_points):
        global cashout
        # Checking if someone got an blackjack (21) on the first 2 cards
        # Both got an blackjack -> Draw
        if P_points == 21 & D_points == 21: 
            print('Draw')
            cashout = bet
            blackjack.purse = blackjack.purse + cashout
            blackjack.final_Outcome()
            blackjack.play_again()
        # The Player got an blackjack -> Win
        elif P_points == 21:
            print('Player Wins')
            cashout = cashout + bet*2.5
            blackjack.purse = blackjack.purse + cashout
            blackjack.final_Outcome()
            blackjack.play_again()
        # The Dealer got an blackjack -> Lose
        elif D_points == 21:
            print('Dealer Wins Player Lost')
            cashout = 0
            blackjack.purse = blackjack.purse + cashout
            blackjack.final_Outcome()
            blackjack.play_again()

    def final_win():
        global cashout
        # Here we check who won at the end
        # The Dealer draws till 16 points
        while dealer_points <= 16:
            blackjack.Dealer()
        # Both got the same -> Draw
        if dealer_points == player_points:
            print('Draw')
            cashout = cashout + bet
        # Dealer got more than Player -> Lose
        elif dealer_points > player_points:
            print('Dealer Wins')
            cashout = 0
        # Player got more than Dealer -> Win
        elif player_points > dealer_points:
            print('Player Wins')
            cashout = cashout + bet*2

    def split_final_win1():
        global cashout1
        global result_split1
        # Is the Players split over 21 -> Lose (on this split)
        if player_points_split1 > 21:
            cashout1 = 0
            result_split1 = 'The Player Lost.'
        else:
            while dealer_points <= 16:
                blackjack.Dealer()
            # Both got the same points -> Draw (on this split)
            if dealer_points == player_points_split1:
                cashout1 = cashout1 + 0.5 * bet
                result_split1 = 'Draw.'
            # Dealer got more points -> Lose (on this split)
            elif dealer_points > player_points_split1:
                cashout1 = 0
                result_split1 = 'The Player Lost.'
            # Player got more points -> Win (on this split)
            elif player_points_split1 > dealer_points:
                cashout1 = cashout1 + bet
                result_split1 = 'The Player won.'

    def split_final_win2():
        global cashout2
        global result_split2
        # Is the Players split over 21 -> Lose (on this split)
        if player_points_split2 > 21:
            cashout2 = 0
            result_split2 = 'The Player Lost.'
        else:
            while dealer_points <= 16:
                blackjack.Dealer()
            # Both got the same points -> Draw (on this split)
            if dealer_points == player_points_split2:
                cashout2 = cashout2 + 0.5 * bet
                result_split2 = 'Draw.'
            # Dealer got more points -> Lose (on this split)
            elif dealer_points > player_points_split2:
                cashout2 = 0
                result_split2 = 'The PLayer Lost.'
            # Player got more points -> Win (on this split)
            elif player_points_split2 > dealer_points:
                cashout2 = cashout2 + bet
                result_split2 = 'The Player won.'

    def Player():
        global player_points
        # Draws the Player a random Card
        random_number = random.randint(0,41)
        player_cards.append(blackjack.deck[random_number])
        player_cards_names.append(blackjack.deck_card[random_number])
        player_points = player_points + blackjack.deck_value[random_number]

        # Ace check to either be 11 or 1
        if player_points > 21:
            if player_cards[-1] in blackjack.aces:
                player_points = player_points - 10
            else:
                # Bust the Player if he got over 21
                print('Bust')
                blackjack.purse = blackjack.purse + cashout
                blackjack.final_Outcome()
                blackjack.play_again()
        
    def Dealer():
        global random_number, dealer_points, fake_value, cashout, cashout1, cashout2, value
        # Draws the Dealer a random Card
        random_number = random.randint(0,41)
        value = blackjack.deck_value[random_number]
        dealer_cards.append(blackjack.deck[random_number])
        dealer_points = dealer_points + value
        # Ace check to either be 11 or 1
        if dealer_points > 21:
            if dealer_cards[-1] in blackjack.aces:
                dealer_points = dealer_points - 10
                fake_value =+ 10
            else:
                # If the Player Decision was split the split outcome takes place
                if decision.lower() == 'split':
                    cashout1 = 2 * bet
                    cashout2 = 2 * bet
                    blackjack.split_final_Outcome()
                    blackjack.play_again()
                # The Dealer loses if he got over 21
                else:
                    print('The Player won.')
                    cashout = 2*bet
                    blackjack.purse = blackjack.purse + cashout
                    blackjack.final_Outcome()
                    blackjack.play_again()

    def Outcome():
        # We print the outcome of the Player
        print(f'Player: {player_points} ', end=" ")
        for x in range(len(player_cards)):
            print(player_cards[x], end=" ")
        print("\n")
        
        # We print the outcome of the Dealer
        # The last card and thier value is hidden
        print(f'Dealer: {dealer_points - value + fake_value} ', end=" ")
        for x in range(len(dealer_cards)-1):
            print(dealer_cards[x], end=" ")
        print("\n")
        
    def split_Outcome():
        blackjack.clear_console()
        # Its the outcome of the first split
        print("Split one: ", end="")
        print(player_points_split1, end=" ")
        for x in range(len(player_cards_split1)):
            print(player_cards_split1[x], end=" ")
        print("\n")

        # Its the outcome of the second split
        print("Split two: ", end="")
        print(player_points_split2, end=" ")
        for x in range(len(player_cards_split2)):
            print(player_cards_split2[x], end=" ")
        print("\n")
        
        # We print the outcome of the Dealer
        # The last card and thier value is hidden
        print("Dealer: ", end="")
        print(dealer_points - value + fake_value, end=" ")
        for x in range(len(dealer_cards)-1):
            print(dealer_cards[x], end=" ")
        print("\n")    

    def final_Outcome():
        # Printing the final outcome of the game
        # The Player points and cards
        print(f'Player: {player_points} ', end=" ")
        for x in range(len(player_cards)):
            print(player_cards[x], end=" ")
        print("\n")

        # The Dealer points and cards
        print(f'Dealer: {dealer_points} ', end=" ")
        for x in range(len(dealer_cards)):
            print(dealer_cards[x], end=" ")
        print("\n")
        # Printing the money and stuff
        print(f'Bet: {bet}\nCashout: {cashout}\nPurse: {blackjack.purse}')

    def split_final_Outcome():
        blackjack.clear_console()
        # Printing the final outcomes of each split
        print(result_split1)
        print("Split one: ", end="")
        print(player_points_split1, end=" ")
        for x in range(len(player_cards_split1)):
            print(player_cards_split1[x], end=" ")
        print("\n")

        print(result_split2)
        print("Split two: ", end="")
        print(player_points_split2, end=" ")
        for x in range(len(player_cards_split2)):
            print(player_cards_split2[x], end=" ")
        print("\n") 

        # Printing the Dealers cards and points
        print("Dealer: ", end="")
        print(dealer_points, end=" ")
        for x in range(len(dealer_cards)):
            print(dealer_cards[x], end=" ")
        print("\n")

        # Printing the money and stuff
        print("Bet:", bet)
        print("Cashout Split one:", cashout1)
        print("Cashout Split one:", cashout2)
        blackjack.purse = blackjack.purse + cashout1 + cashout2
        print("Purse:", blackjack.purse)

    def Decision():
        global cashout, bet, decision
        # Asking the Player what he wants to do
        decision = str(input("What do you want to do? (Hit, Stand, Double, Split, Surrender): "))
        # While the Player don't give a valid answer he will get ask again
        while decision.lower() not in Options:
            blackjack.clear_console()
            blackjack.Outcome()
            print("You're only options are: Hit, Stand, Double, Split or Surrender!")
            print("")
            decision = input("What do you want to do? (Hit, Stand, Double, Split, Surrender): ")
        # If he Hits he will get another card
        if decision.lower() == 'hit':
            blackjack.clear_console()
            blackjack.Player()
            blackjack.Outcome()
            blackjack.Decision()
        # If he Stands he will not get another card and we check for the winner
        if decision.lower() == 'stand':
            blackjack.clear_console()
        # If he Doubles he will get another card and his bet gets doubled (you can only do this once)
        if decision.lower() == 'double':
            blackjack.clear_console()
            Options.remove('double')
            blackjack.purse = blackjack.purse - bet
            bet = bet*2
            blackjack.Player()
            blackjack.Outcome()
            blackjack.Decision()
        # If he Splits he will get two seperate decks to play with (He can then only Hit or Stand)
        if decision.lower() == 'split':
            if len(player_cards) != 2:
                print("You can't split anymore!")
                blackjack.Decision()
            if player_cards_names[0] == player_cards_names[1]:
                blackjack.split()
                blackjack.split_final_win1()
                blackjack.split_final_win2()
                blackjack.split_final_Outcome()
                blackjack.play_again()
            else:
                print("You can't split those cards!")
                blackjack.Decision()
        # If he Surrenders he will get half of his money back and the game ends
        if decision.lower() == 'surrender':
            blackjack.clear_console()
            cashout = bet * 0.5
            blackjack.purse = blackjack.purse + cashout
            blackjack.final_Outcome()
            blackjack.play_again()

    def split():
        global player_points_split1
        global player_points_split2
        # Here we Split both decks and player points
        player_cards_split1.append(player_cards[0])
        player_cards_split2.append(player_cards[1])
        player_points_split1 = player_points * 0.5
        player_points_split2 = player_points * 0.5
        # We draw an aditional card to each split deck
        blackjack.draw_split1(player_cards_split1)
        blackjack.draw_split2(player_cards_split2)
        blackjack.split_Outcome()
        # We ask the Player if he wants aditional cards
        # If he has over 21 in the first split he can't get another card
        if player_points_split1 > 21:
            split1 = 'no'
        else:
            split1 = input("Do you want another card on split one?: ")
        # If his answer is unvalid he will get ask again
        while split1.lower() not in split1_Options:
            print("You need to decide if yes or no!")
            split1 = input("Do you want another card on split one?: ")
        # If he agrees to another card he gets one
        while split1.lower() == 'yes':
            blackjack.draw_split1(player_cards_split1)
            blackjack.split_Outcome()
            # If he has over 21 in the first split he can't get another card
            if player_points_split1 > 21:
                split1 = 'no'
            else:
                split1 = input("Do you want another card on split one?: ")
        # If he don't wants a card on the first split he will get asked for the second split
        if split1.lower() == 'no':
            # If he has over 21 in the second split he can't get another card
            if player_points_split2 > 21:
                split2 = 'no'
            else:
                split2 = input("Do you want another card on split two?: ")
            while split2.lower() not in split2_Options:
                print("You need to decide if yes or no!")
                split2 = input("Do you want another card on split two?: ")
            while split2.lower() == 'yes':
                blackjack.draw_split2(player_cards_split2)
                blackjack.split_Outcome()
                if player_points_split2 > 21:
                    split2 = 'no'
                else:
                    split2 = input("Do you want another card on split two?: ")
            if split2.lower() == 'no':
                blackjack.clear_console()

    def draw_split1(split_cards):
        global player_points_split1
        random_number = random.randint(0,41)
        split_cards.append(blackjack.deck[random_number])
        player_points_split1 = player_points_split1 + blackjack.deck_value[random_number]
        if player_points_split1 > 21:
            if split_cards[-1] in blackjack.aces:
                player_points_split1 = player_points_split1 - 10
    
    def draw_split2(split_cards):
        global player_points_split2
        random_number = random.randint(0,41)
        split_cards.append(blackjack.deck[random_number])
        player_points_split2 = player_points_split2 + blackjack.deck_value[random_number]
        if player_points_split2 > 21:
            if split_cards[-1] in blackjack.aces:
                player_points_split2 = player_points_split2 - 10

    def run():
        global player_cards
        global dealer_cards
        global player_cards_split1
        global player_cards_split2
        global player_cards_names
        global player_points
        global player_points_split1
        global player_points_split2
        global dealer_points
        global bet
        global cashout
        global cashout1
        global cashout2
        global fake_value
        global Options
        global split1_Options
        global split2_Options

        Options = ['hit', 'stand', 'double', 'split', 'surrender']
        split1_Options = ['yes', 'no']
        split2_Options = ['yes', 'no']
        player_cards = []
        player_cards_split1 = []
        player_cards_split2 = []
        player_cards_names = []
        dealer_cards = []
        player_points = 0
        player_points_split1 = 0
        player_points_split2 = 0
        dealer_points = 0
        cashout = 0
        cashout1 = 0
        cashout2 = 0
        fake_value = 0
        # We ask Bet
        if blackjack.purse <= 0:
                print('Your Broke.')
                exit()
        bet = float(input('How much of a bet do you want to place?: '))
        while bet <= 0:
            blackjack.clear_console()
            print(f"You have to set a bet over 0, you have {blackjack.purse} to play with.")
            bet = float(input('How much of a bet do you want to place?: '))
        while bet > blackjack.purse:
            print(f'Invalid amount you dont have enough money, you have {blackjack.purse} to play with.')
            if blackjack.purse < 0:
                print('Your Broke.')
                exit()
            else:
                bet = float(input('How much of a bet do you want to place?: '))
        if blackjack.purse < 0:
            print('Your Broke.')
            exit()
        # Takes the money from the purse   
        blackjack.purse = blackjack.purse - bet
        # Run each function at correct times
        blackjack.clear_console()
        blackjack.Player()
        blackjack.Player()
        blackjack.Dealer()
        blackjack.Dealer()
        blackjack.blackjack_win(player_points, dealer_points)
        blackjack.Outcome()
        blackjack.Decision()
        blackjack.final_win()
        blackjack.purse = blackjack.purse + cashout
        blackjack.final_Outcome()
        blackjack.play_again()

blackjack.run()