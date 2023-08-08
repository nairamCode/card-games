### Order
# Ask for Purse
# Ask for Bet
# Draw 2 Player cards
    # Ace check
# Draw 2 Dealer Cards
    # Ace Check
    # Fake Value added if 2 Aces
# Winner Check for black jacks (21)
# Outcome
    # Hides 2nd Dealer_Card
# Hit Stand Double Split Surrender
# draw dealer till 16
# Winner Check
# Final Outcome
# Play Again
import random
import os

class blackjack:
    # Var
    
    
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
        pass
    
    def play_again():
            if blackjack.purse <= 0:
                print('Your Broke.')
                exit()
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
        if P_points == 21 & D_points == 21: 
            print('Draw')
            cashout = bet
            blackjack.purse = blackjack.purse + cashout
            blackjack.final_Outcome()
            blackjack.play_again()
        elif P_points == 21:
            print('\nPlayer Wins')
            cashout =+ bet*2.5
            blackjack.purse = blackjack.purse + cashout
            blackjack.final_Outcome()
            blackjack.play_again()
        elif D_points == 21:
            print('Dealer Wins Player Lost')
            cashout = 0
            blackjack.purse = blackjack.purse + cashout
            blackjack.final_Outcome()
            blackjack.play_again()

    def final_win():
        global cashout
        while dealer_points <= 16:
            blackjack.Dealer()
        if dealer_points == player_points:
            print('Draw')
            cashout =+ bet
        elif dealer_points > player_points:
            print('Dealer Wins')
            cashout = 0
        elif player_points > dealer_points:
            print('Player Wins')
            cashout =+ bet*2
            
    def Player():
        global player_points
        # All Player Logic is here
        random_number = random.randint(0,41)
        player_cards.append(blackjack.deck[random_number])
        player_points = player_points + blackjack.deck_value[random_number]
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
        global random_number, dealer_points, fake_value, cashout
        # All Dealer logic is here
        random_number = random.randint(0,41)
        dealer_cards.append(blackjack.deck[random_number])
        dealer_points = dealer_points + blackjack.deck_value[random_number]
        if dealer_points > 21:
            if dealer_cards[-1] in blackjack.aces:
                dealer_points = dealer_points - 10
                fake_value =+ 10
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

        print(f'Dealer: {dealer_points - blackjack.deck_value[random_number] + fake_value} ', end=" ")
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

    def Decision():
        global cashout, bet
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
            # need to be added
            blackjack.clear_console()
            blackjack.Decision
        if decision.lower() == 'surrender':
            blackjack.clear_console()
            cashout = bet * 0.5
            blackjack.purse = blackjack.purse + cashout
            blackjack.final_Outcome()
            blackjack.play_again()
            
    def run():
        global player_cards
        global dealer_cards
        global player_points
        global dealer_points
        global bet
        global cashout
        global fake_value
        global Options
        Options = ['hit', 'stand', 'double', 'split', 'surrender']
        player_cards = []
        dealer_cards = []
        player_points = 0
        dealer_points = 0
        cashout = 0
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