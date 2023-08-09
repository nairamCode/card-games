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

    # Please fix here later!
    # It don't show the result!
    def split_final_win(split_points, money, result):
        if split_points > 21:
            money = 0
            result = result + "The Player Lost."
        else:
            while dealer_points <= 16:
                blackjack.Dealer()
            if dealer_points == split_points:
                money = money + 0.5 * bet
                result = result + "Draw."
            elif dealer_points > split_points:
                money = 0
                result = result + "The Player Lost."
            elif split_points > dealer_points:
                money = money + bet
                result = result + "The Player won."

    def Player():
        global player_points
        # All Player Logic is here
        random_number = random.randint(0,41)
        player_cards.append(blackjack.deck[7])
        player_cards_names.append(blackjack.deck_card[7])
        player_points = player_points + blackjack.deck_value[7]
        # Blackjack hand debug
        # player_points = 21

        if player_points > 21:
            if player_cards[-1] in blackjack.aces:
                player_points = player_points - 10
            else:
                print('Bust')
                blackjack.purse = blackjack.purse + cashout
                blackjack.final_Outcome()
                blackjack.play_again()
        
    def Dealer():
        global random_number, dealer_points, fake_value, cashout, cashout1, cashout2, value
        # All Dealer logic is here
        random_number = random.randint(0,41)
        value = blackjack.deck_value[random_number]
        dealer_cards.append(blackjack.deck[random_number])
        dealer_points = dealer_points + value
        if dealer_points > 21:
            if dealer_cards[-1] in blackjack.aces:
                dealer_points = dealer_points - 10
                fake_value =+ 10
            else:
                if decision.lower() == 'split':
                    cashout1 = 2 * bet
                    cashout2 = 2 * bet
                    blackjack.split_final_Outcome()
                    blackjack.play_again()
                else:
                    print('The Player won.')
                    cashout = 2*bet
                    blackjack.purse = blackjack.purse + cashout
                    blackjack.final_Outcome()
                    blackjack.play_again()

    def Outcome():
        # We print the outcome of a action
        print(f'Player: {player_points} ', end=" ")
        for x in range(len(player_cards)):
            print(player_cards[x], end=" ")
        print("\n")

        print(f'Dealer: {dealer_points - value + fake_value} ', end=" ")
        for x in range(len(dealer_cards)-1):
            print(dealer_cards[x], end=" ")
        print("\n")
        
    def split_Outcome():
        blackjack.clear_console()
        print("Split one: ", end="")
        print(player_points_split1, end=" ")
        for x in range(len(player_cards_split1)):
            print(player_cards_split1[x], end=" ")
        print("\n")

        print("Split two: ", end="")
        print(player_points_split2, end=" ")
        for x in range(len(player_cards_split2)):
            print(player_cards_split2[x], end=" ")
        print("\n")

        print("Dealer: ", end="")
        print(dealer_points - value + fake_value, end=" ")
        for x in range(len(dealer_cards)-1):
            print(dealer_cards[x], end=" ")
        print("\n")    

    def final_Outcome():
        print(f'Player: {player_points} ', end=" ")
        for x in range(len(player_cards)):
            print(player_cards[x], end=" ")
        print("\n")

        print(f'Dealer: {dealer_points} ', end=" ")
        for x in range(len(dealer_cards)):
            print(dealer_cards[x], end=" ")
        print("\n")
        print(f'Bet: {bet}\nCashout: {cashout}\nPurse: {blackjack.purse}')

    def split_final_Outcome():
        blackjack.clear_console()
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

        print("Dealer: ", end="")
        print(dealer_points, end=" ")
        for x in range(len(dealer_cards)):
            print(dealer_cards[x], end=" ")
        print("\n")

        print("Bet:", bet)
        print("Cashout Split one:", cashout1)
        print("Cashout Split one:", cashout2)
        blackjack.purse = blackjack.purse + cashout1 + cashout2
        print("Purse:", blackjack.purse)

    def Decision():
        global cashout, bet, decision, result_split1, result_split2
        decision = str(input("What do you want to do? (Hit, Stand, Double, Split, Surrender): "))
        while decision.lower() not in Options:
            blackjack.clear_console()
            blackjack.Outcome()
            print("You're only options are: Hit, Stand, Double, Split or Surrender!")
            print("")
            decision = input("What do you want to do? (Hit, Stand, Double, Split, Surrender): ")
        if decision.lower() == 'hit':
            blackjack.clear_console()
            blackjack.Player()
            blackjack.Outcome()
            blackjack.Decision()
        if decision.lower() == 'stand':
            blackjack.clear_console()
        if decision.lower() == 'double':
            blackjack.clear_console()
            Options.remove('double')
            blackjack.purse = blackjack.purse - bet
            bet = bet*2
            blackjack.Player()
            blackjack.Outcome()
            blackjack.Decision()
        if decision.lower() == 'split':
            if len(player_cards) != 2:
                print("You can't split anymore!")
                blackjack.Decision()
            if player_cards_names[0] == player_cards_names[1]:
                blackjack.split()
                blackjack.split_final_win(player_points_split1, cashout1, result_split1)
                blackjack.split_final_win(player_points_split2, cashout2, result_split2)
                blackjack.split_final_Outcome()
                blackjack.play_again()
            else:
                print("You can't split those cards!")
                blackjack.Decision()
        if decision.lower() == 'surrender':
            blackjack.clear_console()
            cashout = bet * 0.5
            blackjack.purse = blackjack.purse + cashout
            blackjack.final_Outcome()
            blackjack.play_again()

    def split():
        global player_points_split1
        global player_points_split2
        player_cards_split1.append(player_cards[0])
        player_cards_split2.append(player_cards[1])
        player_points_split1 = player_points * 0.5
        player_points_split2 = player_points * 0.5
        blackjack.draw_split1(player_cards_split1)
        blackjack.draw_split2(player_cards_split2)
        blackjack.split_Outcome()
        if player_points_split1 > 21:
            split1 = 'no'
        else:
            split1 = input("Do you want another card on split one?: ")
        while split1.lower() not in split1_Options:
            print("You need to decide if yes or no!")
            split1 = input("Do you want another card on split one?: ")
        while split1.lower() == 'yes':
            blackjack.draw_split1(player_cards_split1)
            blackjack.split_Outcome()
            if player_points_split1 > 21:
                split1 = 'no'
            else:
                split1 = input("Do you want another card on split one?: ")
        if split1.lower() == 'no':
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
        global result_split1
        global result_split2

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
        result_split1 = ""
        result_split2 = ""
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