import random, sys

#Welcome message
print('!!!!!  WELCOME TO VEGAS !!!!!')
print('Lets roll some dice')
print('Your odds are: \n 2: 36:1 \n 3: 18:1 \n 4: 12:1 \n 5: 9:1 \n 6: 7:1 \n 7: 6:1 \n 8: 7:1 \n 9: 9:1 \n 10: 12:1 \n 11: 18:1 \n 12: 36:1')

#Initial pot:
starting_pot = 1000
print('Your starting pot is' + ' ' + '$' + str(starting_pot))

#Money remaining:
money_remaining = 1000

#roll combination payouts:
roll_combo_payouts = {2: 36, 3: 18, 4: 12, 5: 9, 6: 7, 7: 6, 8: 7, 9: 9, 10: 12, 11: 18, 12: 36}


#start the program loop:
while True:
    print('Do you want to (p)lay or (q)uit?')
    play = input()
    if play == 'q':
        sys.exit()
    else:
        print('Great!!!')

    #establish the betting loop:
    while True:
        #pick a number to bet on
        print('What number are you betting on? (valid input is 2-12)')
        guess = int(input())
        if guess in range(2, 13):
            #ask for a wager
            print('Please make your wager. Min wager is $50')
            bet = int(input())
            money_remaining = money_remaining - bet
            #evaluate the bet against the min required bet
            if bet < 50:
                print("I'm sorry, please bet at least $50 to roll")
                money_remaining += bet
                continue
            elif bet >= 50 and money_remaining > 0:
                print('Lets roll! You have' + ' ' + '$' + str(money_remaining) + ' ' + 'remaining')
                break
            elif bet >= 50 and money_remaining < 0:
                money_remaining += bet
                print('I am sorry, you do not have enough money to make that bet')
                print('Would you like to (b)et again or (q)uit? You have {} remaining'.format(money_remaining))
                respawn = input()
                if respawn == 'b':
                    continue
                else:
                    sys.exit()
        else:
            print('Guess again')
            continue

    # establish the game play loop
    while True:
        print('Thank you and good luck! press (r) to roll the die or (q) to quit')
        player_rolls = input()

        if player_rolls == 'r':
            # create the dice roll for the player
            die_one = random.randint(1, 6)
            die_two = random.randint(1, 6)
            roll_total = die_one + die_two

            # evaluate roll against bet:
            if guess == roll_total:
                print('Its a hit!! You rolled a {} and {}, total roll is {}'.format(die_one, die_two, roll_total))
                for key in roll_combo_payouts:
                    if key == roll_total:
                        win_total = roll_combo_payouts[key] * bet
                        money_remaining += win_total
                        print('You won ${}, you have ${} remaining'.format(win_total, money_remaining))
                break
            #condition to end the game if player;s money goes to $0
            else:
                print('You rolled a {} and {}, total roll is {}, sorry... better luck next time'.format(die_one, die_two, roll_total))
                break
        else:
            print('See ya!')
            sys.exit()




