#####################################
### WELCOME TO YOUR OOP PROJECT #####
#####################################

# For this project you will be using OOP to create a card game. This card game will
# be the card game "War" for two players, you an the computer. If you don't know
# how to play "War" here are the basic rules:
#
# The _deck is divided evenly, with each player receiving 26 cards, dealt one at a time,
# face down. Anyone may deal first. Each player places his stack of cards face down,
# in front of him.
#
# The Play:
#
# Each player turns up a card at the same time and the player with the higher card
# takes both cards and puts them, face down, on the bottom of his stack.
#
# If the cards are the same rank, it is War. Each player turns up three cards face
# down and one card face up. The player with the higher cards takes both piles
# (six cards). If the turned-up cards are again the same rank, each player places
# another card face down and turns another card face up. The player with the
# higher card takes all 10 cards, and so on.
#
# There are some more variations on this but we will keep it simple for now.
# Ignore "double" wars
#
# https://en.wikipedia.org/wiki/War_(card_game)

# ----------------
# IMPORTS
# -------------------------------------------------------------------
from random import shuffle


# ----------------
# GLOBAL VARIABLES
# -------------------------------------------------------------------
computer = None  # object representing the computer player
human = None  # object representing the human player
comp_play_pool = []  # cards played by the computer
man_play_pool = []  # cards played by the human


# ------------
# GAME CLASSES
# --------------------------------------------------------------------
class Deck:
    '''
    This is the _deck Class. This object will create a _deck of cards to initiate
    play. You can then use this _deck list of cards to split in half and give to
    the players. It will use _SUITE and _RANKS to create the _deck. It should also
    have a method for splitting/cutting the _deck in half and Shuffling the _deck.
    '''

    # constants to create cards
    _SUITE = 'H D S C'.split()  # _SUITE list
    _RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()  # _RANKS list

    # private _deck lists
    _deck = []    # private full _deck
    _play__deck1 = []  # private 1st 1/2 play _deck
    _play__deck2 = []  # private 2nd 1/2 play _deck

    def __init__(self):
        ''' Create a _deck of cards '''

        for rank in self._RANKS: # O(n)
            self._deck.append(rank+self._SUITE[0])
            self._deck.append(rank+self._SUITE[1])
            self._deck.append(rank+self._SUITE[2])
            self._deck.append(rank+self._SUITE[3])
# _deck = [(s, r) for s in SUITES for r in RANKS] O(n^2)

    def _shuffle__deck(self):
        ''' Shuffles the _deck '''

        shuffle(self._deck)

    def _split__deck(self):
        ''' Splits the shuffled _deck into two '''

        # call shuffle _deck
        self._shuffle__deck()
        # split _deck
        for i in range(0, 26):  # O(n)
            self._play__deck1.append(self._deck[i])

        for j in range(26, 52):
            self._play__deck2.append(self._deck[j])
# return [self.deck[:26], self._deck[26:]  O(1)

    def get_play__decks(self):
        ''' Returns two equal shuffled _decks of 26 cards each '''

        # call split _deck
        self._split__deck()
        # return split _decks
        return [self._play__deck1, self._play__deck2]
# Only needs shuffle and split methods no need for the two half deck lists

    def get_rank(self, rank_char):
        ''' Return the rank of a card char passed to it '''

        return self._RANKS.index(rank_char)


class Hand:
    '''
    This is the Hand class. Each player has a Hand, and can add or remove
    cards from that hand. There should be an add and remove card method here.
    '''
    
    hand = []  # hand list

    def __init__(self, play__deck):
        ''' Initializes a playing hand = cards _deck to play with '''

        self.hand = play__deck

    def add_hand(self, cards):
        ''' Adding cards back into the hand = winning cards back from play. Placed at the end of the hand '''

        for card in cards:  # O(n)
            self.hand.append(card)
# Or extend() > list1.extend(list2) : adds all the items in list2 to the end of list1: O(n)

    def remove_hand(self):
        ''' Removes cards from the hand = putting the cards into play. Removed from the beginning of the hand '''

        return self.hand.pop(0)


class Player:
    """
    This is the Player class, which takes in a name and an instance of a Hand
    class object. The player can then play cards and check if they still have cards.
    """
    
    player_name = ''
    hand_obj = None

    def __init__(self, name, obj):
        ''' Creates a player and allocate a hand '''

        self.player_name = name
        self.hand_obj = obj

    def play_cards(self):
        ''' Plays a card or cards '''

        return self.hand_obj.remove_hand()

    def get_hand(self):
        ''' Retrives a player's hand for checking '''

        return self.hand_obj.hand

# This to a has_cards() or cards_left() since we no longer need to return the entire hand
# You can use the __str__ magic method to pritn out the hand when using 'print(hand_obj.hand)'. This should be in the Hand class.


# -------------------
# GAME PLAY FUNCTIONS
# -------------------------------------------------------------------
def initialize_game():
    ''' Sets up the players and deals their hands '''

    # Create a _deck of cards
    cards = Deck()
    cards_list = cards.get_play__decks()

    # Create computer player and deal a hand
    global computer;
    computer = Player('Bot', Hand(cards_list[0]))
    
    # Create human player and deal a hand
    name = input("Enter your play name: ")
    global human;
    human = Player(name, Hand(cards_list[1]))

def check_win_hand():
    ''' Checks for the player who played the higher ranked card and awards them the winnings i.e        all cards played so far. The last card played is used for comparison in determining the         winner.
    '''

    # Initialize the _deck class to check card rank
    deck_obj = Deck();

    # Check play card to fetch the correct card rank
    comp_play = ''
    man_play = ''

    if len(''.join(comp_play_pool[-1])) > 2:
        comp_play = ''.join(comp_play_pool[-1])[:2]

    elif len(''.join(comp_play_pool[-1])) == 2:
        comp_play = ''.join(comp_play_pool[-1])[0]

    if len(''.join(man_play_pool[-1])) > 2:
        man_play = ''.join(man_play_pool[-1])[:2]

    elif len(''.join(man_play_pool[-1])) == 2:
        man_play = ''.join(man_play_pool[-1])[0]

    # Check winning card
    if deck_obj.get_rank(comp_play) > deck_obj.get_rank(man_play):
        # Comp wins
        return 1
    elif deck_obj.get_rank(comp_play) < deck_obj.get_rank(man_play):
        # Human wins
        return 2
    else: # return 0 if there is a draw
        return 0

def can_play(num_cards):
    ''' Check if each player has enough cards to play the upcoming round, if not the one the other player that does wins the game '''
    
    if len(computer.get_hand()) < num_cards:
        return 2  
    elif len(human.get_hand()) < num_cards:
        return 1
         
def play_game_manual():
    ''' Plays the game manually '''

    draw_checker = 0  # checks number of draws per round

    while True:
        # PLAY: If no draw, players play a card each, if first draw occurrence then players play 4 cards each if subsequent draw they play two cards each. Default 0 for no draw, 1 for first draw, >1 for subsequent draws.
            
        if draw_checker == 0:
            print('\n----------------------------------------')

            # If either the comp or human does not have enough cards for this round, end the game
            if can_play(1) == 2:
                print("\n'{}' has run out of cards, YOU WIN the game!".format(computer.player_name))
                break
            elif can_play(1) == 1:
                print("\nYou have run out of cards, '{}' wins the game.".format(computer.player_name))
                break
            
            else:         
                # Normal play
                print('{} has '.format(computer.player_name), len(computer.get_hand()), ' cards left.')
                print('Your have ', len(human.get_hand()) , ' cards left.')

                input("\nPress enter to play your turn: ")

                man_play_pool.append(human.play_cards())
                print("You have played a '{}'".format(man_play_pool[-1]))

                comp_play_pool.append(computer.play_cards())
                print("{} has played a '{}'\n".format(computer.player_name, comp_play_pool[-1]))

                hand_result = check_win_hand()

        elif draw_checker == 1:

            # If either the comp or human does not have enough cards for this round, end the game
            if can_play(4) == 2:
                print("\n'{}' has run out of cards, YOU WIN the game!".format(computer.player_name))
                break
            elif can_play(4) == 1:
                print("\nYou have run out of cards, '{}' wins the game.".format(computer.player_name))
                break
            
            else:
                # Play first draw
                print("The play is tied, this is WAR! You will have to play an additional four cards to attempt to win this turn, 3 will be face down and the last one face up to compare with the computer's similar play")

                input("\nPress enter to play your turn: ")

                for i in range(0, 4):
                    man_play_pool.append(human.play_cards())
                    comp_play_pool.append(computer.play_cards())
# Use extend() instead

                print("You have played a '{}' plus 3 other unknown cards".format(man_play_pool[-1]))
                print("'{} ' has played a '{}' plus 3 other unknown cards\n".format(computer.player_name, comp_play_pool[-1]))
                
                hand_result = check_win_hand()

        elif draw_checker > 1:

            # If either the comp or human does not have enough cards for this round, end the game
            if can_play(2) == 2:
                print("\n'{}' has run out of cards, YOU WIN the game!".format(computer.player_name))
                break
            elif can_play(2) == 1:
                print("\nYou have run out of cards, '{}' wins the game.".format(computer.player_name))
                break

            else:
                # Play subsequent draw
                print("\nThe play is tied again, this is NUCLEAR WAR! You will have to play an additional two cards for this turn, 1 will be face down and the last one face up to compare with the computer's similar play")

                input("\nPress enter to play your turn: ")

                for i in range(0, 2):
                    comp_play_pool.append(computer.play_cards())
                    man_play_pool.append(human.play_cards())
# Use extend() instead

                print("You have played a '{}' plus 1 other unknown card".format(man_play_pool[-1]))
                print("'{}' has played a '{}' plus 1 other unknown card".format(computer.player_name, comp_play_pool[-1]))

                hand_result = check_win_hand()

                
        # Check for a draw, or if the round has been won
        if hand_result == 1:
            # Comp wins
            print("{} wins this round.".format(computer.player_name))
            computer.hand_obj.add_hand(comp_play_pool + man_play_pool)
            comp_play_pool.clear()
            man_play_pool.clear()
            draw_checker = 0
            hand_result = 0

        elif hand_result == 2:
            # Human wins
            print("You win this round!!")
            human.hand_obj.add_hand(comp_play_pool + man_play_pool)
            comp_play_pool.clear()
            man_play_pool.clear()
            draw_checker = 0
            hand_result = 0

        else:
            # A draw
            draw_checker +=1
            hand_result = 0

    print('----------------------------------------\n')

def play_game_auto():
    ''' Auto plays the game '''

    rounds = 0  # tracks no. of rounds played
    wars = 0  # tracks no. of 1st war occurrences
    nuclear_wars = 0  # tracks no. of subsequent war occurrences
    draw_checker = 0  # checks number of draws per round

    while True:
        # PLAY: If no draw, players play a card each, if first draw occurrence then players play 4 cards each if subsequent draw they play two cards each. Default 0 for no draw, 1 for first draw, >1 for subsequent draws.

        rounds += 1

        if rounds > 9999:
            # Limit auto play to 10,000 rounds
            print('\nMax number of rounds reached, no winner found.')
            break
            
        if draw_checker == 0:
            
            # If either the comp or human does not have enough cards for this round, end the game
            if can_play(1) == 2:
                print("\n'{}' has run out of cards, YOU WIN the game!".format(computer.player_name))
                break
            elif can_play(1) == 1:
                print("\nYou have run out of cards, '{}' wins the game.".format(computer.player_name))
                break
            
            else:
                # Normal play
                man_play_pool.append(human.play_cards())
                comp_play_pool.append(computer.play_cards())

                hand_result = check_win_hand()

        elif draw_checker == 1:
            # Initial war occurence
            wars += 1

            # If either the comp or human does not have enough cards for this round, end the game
            if can_play(4) == 2:
                print("\n'{}' has run out of cards, YOU WIN the game!".format(computer.player_name))
                break
            elif can_play(4) == 1:
                print("\nYou have run out of cards, '{}' wins the game.".format(computer.player_name))
                break
            
            else:
                # Play first draw occurrence
                for i in range(0, 4):
                    man_play_pool.append(human.play_cards())
                    comp_play_pool.append(computer.play_cards())
# Use extend() instead
                
                hand_result = check_win_hand()

        elif draw_checker > 1:
            # Subsequent war occurrences
            nuclear_wars += 1

            # If either the comp or human does not have enough cards for this round, end the game
            if can_play(2) == 2:
                print("\n'{}' has run out of cards, YOU WIN the game!".format(computer.player_name))
                break
            elif can_play(2) == 1:
                print("\nYou have run out of cards, '{}' wins the game.".format(computer.player_name))
                break

            else:
                # Play subsequent draw
                for i in range(0, 2):
                    comp_play_pool.append(computer.play_cards())
                    man_play_pool.append(human.play_cards())
# Use extend() instead

                hand_result = check_win_hand()


        # Check for a draw, or if the round has been won
        if hand_result == 1:
            # Comp wins
            computer.hand_obj.add_hand(comp_play_pool + man_play_pool)
            comp_play_pool.clear()
            man_play_pool.clear()
            draw_checker = 0
            hand_result = 0

        elif hand_result == 2:
            # Human wins
            human.hand_obj.add_hand(comp_play_pool + man_play_pool)
            comp_play_pool.clear()
            man_play_pool.clear()
            draw_checker = 0
            hand_result = 0

        else:
            # A draw
            draw_checker +=1
            hand_result = 0
    
    print('\nNo of rounds played: ', rounds)
    print('\nNo of wars: ', wars)
    print('\nNo of nuclear wars: ', nuclear_wars)
    print('----------------------------------------\n')

# ---------
# ACTUAL GAME PLAY
# -------------------------------------------------------------------

initialize_game()  # Set up game

# Start game
print("\nWelcome to War {}, your opponent is {} the computer, press ctrl + C at any point in manual game mode to exit, let's play ...".format(human.player_name, computer.player_name))

game_mode = input('\nPlay manually (y) or let the game autoplay (enter)?')

if game_mode == 'y':
    play_game_manual()
else:
    play_game_auto()