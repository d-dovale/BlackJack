from p1_random import P1Random

# Random card generator for zybooks

rng = P1Random()
game = True

# Intializes game variables

card = 0
game_counter = 0
player_wins = 0
dealer_wins = 0
tie_games = 0

while game:
    player_hand = 0

    # Intial Start Message
    print("START GAME #" + str(game_counter + 1) + "\n")

    card = rng.next_int(13) + 1

    if card == 1:

        print("Your card is a ACE!")

    elif 2 <= card <= 10:
        card_num = 2

        # Loops through all numbers between 2 to 10 to find which card the player has

        while card_num != card:

            card_num += 1

        card = card_num
        print("Your card is a " + str(card) + "!")


    # Sets all face cards equal to 10 due to the rules of blackjack

    elif card == 11:

        print("Your card is a JACK!")
        card = 10

    elif card == 12:

        print("Your card is a QUEEN!")
        card = 10

    elif card == 13:

        print("Your card is a KING!")
        card = 10

    player_hand += card
    print("Your hand is: " + str(card) + "\n")

    # Keep asking users to choose the menu
    no_winners = True

    while no_winners:

        # Print Menu
        menu = input("1. Get another card\n2. Hold hand\n3. Print statistics\n4. Exit\n\nChoose an option: ")

        # Get another card
        if menu == "1":
            second_card = rng.next_int(13) + 1

            if second_card == 1:

                player_hand += second_card

                print("Your card is a ACE!")
                print("Your hand is: " + str(player_hand))
            elif 2 <= second_card <= 10:
                card_num = 2

                # Loops through all numbers between 2 to 10 to find which card the player has

                while card_num != second_card:
                    card_num += 1

                second_card = card_num
                player_hand += card_num

                print("Your card is a " + str(second_card) + "!")
                print("Your hand is: " + str(player_hand) + "\n")

            # Does the same thing as the previous face card if statements just for the second card

            elif second_card == 11:

                second_card = 10
                player_hand += second_card

                print("Your card is a JACK!")
                print("Your hand is: " + str(player_hand))

            elif second_card == 12:

                second_card = 10
                player_hand += second_card

                print("Your card is a QUEEN!")
                print("Your hand is: " + str(player_hand))

            elif second_card == 13:

                second_card = 10
                player_hand += second_card       # Used to add the second card to the player hand

                print("Your card is a KING!")
                print("Your hand is: " + str(player_hand))

            # Checks if the player got blackjack

            if player_hand == 21:
                print("BLACKJACK! You win!\n")

                player_hand = 0
                player_wins += 1
                game_counter += 1
                no_winners = False

            # Checks if the player's hand surpassed 21 after getting a new card

            elif player_hand > 21:
                print("\nYou exceeded 21! You lose.\n")

                player_hand = 0
                dealer_wins += 1
                game_counter += 1
                no_winners = False

        # Holds Hand

        elif menu == "2":
            dealer_hand = rng.next_int(11) + 16

            print("Dealer's hand:", dealer_hand)
            print("Your hand is:", player_hand)

            # Checks if the player hand after holding is greater than the dealer hand

            if player_hand > dealer_hand:
                print("\nYou win!\n")

                player_hand = 0
                player_wins += 1
                game_counter += 1
                no_winners = False

            # Checks if the dealer hand after holding is over 21 thus the player automatically wins

            elif dealer_hand > 21:
                print("\nYou win!\n")

                player_hand = 0
                player_wins += 1
                game_counter += 1
                no_winners = False

            # Checks if the dealer hand is greater than the players hand

            elif player_hand < dealer_hand:
                print("\nDealer wins!\n")

                player_hand = 0
                game_counter += 1
                dealer_wins += 1
                no_winners = False

            # Checks if the game is a tie

            elif player_hand == dealer_hand:
                print("It's a tie! No one wins!\n")

                player_hand = 0
                game_counter += 1
                tie_games += 1
                no_winners = False

        # Print Statistics of Game

        elif menu == "3":

            # Makes sure the percentage calculator does not divide by 0 and checks if player has won every game so far

            if (player_wins > 0 and dealer_wins == 0 and tie_games == 0):
                print("\nNumber of Player wins: " + str(player_wins))
                print ("Number of Dealer wins: " + str(dealer_wins))
                print("Number of tie games: " + str(tie_games))
                print("Total # of games played is: " + str(game_counter))
                print("Percentage of Player wins: 100.0%\n")

            elif (dealer_wins == 0 and tie_games == 0):
                print("\nNumber of Player wins: " + str(player_wins))
                print ("Number of Dealer wins: " + str(dealer_wins))
                print("Number of tie games: " + str(tie_games))
                print("Total # of games played is: " + str(game_counter))
                print("Percentage of Player wins: 0.0%\n")

            else:
                # Calculates player winning percentage

                percentage = (player_wins / game_counter) * 100

                print("\nNumber of Player wins: " + str(player_wins))
                print ("Number of Dealer wins: " + str(dealer_wins))
                print("Number of tie games: " + str(tie_games))
                print("Total # of games played is: " + str(game_counter))

                # Tounds percentage variable to two decimal places

                print("Percentage of Player wins: " + str(round(percentage, 2)) + "%\n")

        # Exits out of the program entirely

        elif menu == "4":
            exit()

        # Invalid input by the user, resets while loop

        else:
            print("\nInvalid input!\nPlease enter an integer value between 1 and 4.\n")
