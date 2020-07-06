"""@package docstring

Blackjack game by Htet Ein Yan

This is the second part of Blackjack game assignment which is to implement a solution 
in the python language and evaluate in the OO paradigm, already prepared in the first part.

The following solution includes features such as:
1- Implementation of classes and relationships between each class;
2- Game logic and its implementation using different types of control structures;
3- Asking users their names to make the interface more friendly and presentable;
4- List of instructions and rules provided in order to have the players familiar 
with the game; and
5- Users being able to choose to play again without restarting the application
"""

import random

"""Format text into paragraph"""
import textwrap

"""Initialize the constants--cards"""
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14] * 4

class Deck:
    """Deck class:        
    This class is to keep records of its 52 cards, shuffle the cards, and remove the card
    after being dealt to the players.
    """

    def __init__(self):
        """The constructor: initializing deck list"""
        self.deck = []
       
        for card in cards:
            """Cards with 11, 12, 13, and 14 points to represent as Jack, Queen, King, and 
            Ace cards"""
            if card == 11: card = "J"
            if card == 12: card = "Q"
            if card == 13: card = "K"
            if card == 14: card = "A"
            self.deck.append(card)

    def shuffle(self):
        """Shuffle the cards--randomize"""
        random.shuffle(self.deck)
        
    def deal(self):
        """Deal a card to players and remove it from the deck"""
        return self.deck.pop()
  
class Player:
    """Player class:        
    This class is associated with Deck class to retrieve new cards being added in his hand, 
    determine and return the values of each card and the total points of all the cards 
    the player has in representable string.
    """
    stand = False 
    
    def __init__(self, deck):
        """The constructor: initializing hand to keep record of cards being added
        and Deck object"""
        self.hand = []
        self.deck = deck
    
    def add_card(self):
        """Keep records of the values of the cards the player has"""
        self.hand.append(self.deck.deal())
        
    def get_points(self):
        """Get the total values of the cards the player has"""
        total_points = 0
        
        for card in self.hand:
            """10 points being added for Jack, Queen, King cards; 
            1 point being added for Ace card when the player has more than 10 points; and
            11 points being added for Ace card when the player has less than 11 points
            """
            if card == "J" or card == "Q" or card == "K":
                total_points += 10
            elif card == "A":
                if total_points >= 11:
                    total_points += 1
                else:
                    total_points += 11
            else:
                total_points += card
        
        """return the current total values the player has"""
        return total_points

    def __str__(self):
        """Return a list of cards in representable string formatted with space"""
        
        player_cards = ''
        for player_card in self.hand:
            player_cards += str(player_card) + "  "
        return player_cards.strip()

class UI:
    """UI class:        
    This class is associated with Player class in order to retrieve the card values of each player
    from Player class and to determine various types of results upon the choices made by each player--
    blackjack at the beginning of the game, outcomes at the end of the game, and 
    if any player busts the game (i.e. card values exceeding 21 points)
    """    
    
    """Keep track of the record of players' names"""
    global player1_name, player2_name
    hs_choice = None
    current_player = None
    
    def __init__(self, player1, player2):
        """The constructor: initiazling players objects"""
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1
        
    def print_points(self):
        """Display the values of each player's cards and its total values"""
        print(player1_name + ": " + str(self.player1) + " = " + str(self.player1.get_points()) + "\n")
        print(player2_name + ": " + str(self.player2) + " = " + str(self.player2.get_points()) + "\n")        
             
    def choice(self, current_player):
        """Ask the players for their Hit-Stand choice"""
        
        """Get the current player of the game"""
        self.current_player = current_player
        
        if self.current_player == self.player1: name = player1_name
        if self.current_player == self.player2: name = player2_name
            
        """Ask the current player if he wants to hit or stand"""
        self.hs_choice = input(name + ", what is your choice - hit(H) or stand(S): ").lower()
        print()
        
        """In the case of invalid inputs"""
        while self.hs_choice != 'h' and self.hs_choice != 's':
            self.hs_choice = input(name + ", invalid input. Please choose again - H or S: ").lower()
        
        """A new card is added after choosing hit or check if the current player chooses to stand"""
        if self.hs_choice == 'h':
            self.current_player.add_card()
            self.print_points()
        elif self.hs_choice == 's':
            self.current_player.stand = True
            self.print_points()
            
    def play_again(self):
        """Ask players if they want to play the game again"""
        
        self.again = input("Do you want to play again - yes(Y) or no(N): ").lower()
        if self.again == 'y':
            Blackjack.__init__(blackjack)
            Blackjack.start_game(blackjack)
        elif self.again == 'n':
            print("Thank you for playing. See you again!")        
            
class Rules:
    """Rules class:
    This class is associated with UI class in order to retrieve the card values of each player
    and to determine various types of results upon the choices made by each player--
    blackjack at the beginning of the game, outcomes at the end of the game, and 
    if any player busts the game (i.e. card values exceeding 21 points)
    """    
    
    """Keep track of the record of players' names"""
    global player1_name, player2_name
    
    blackjack = False
    bust = False
    
    def __init__(self, ui):
        """The constructor: initializing UI object"""
        self.ui = ui
                
    def check_blackjack(self):
        """Check if any player has Blackjack after getting their first two cards"""
        
        if self.ui.player1.get_points() == 21:
            print("Blackjack!!!", player1_name, "wins!\n")
            self.blackjack = True
        elif self.ui.player2.get_points() == 21:
            print("Blackjack!!!", player2_name, "wins!\n")
            self.blackjack = True
            
    def check_result(self):
        """Check the results of the game after both players are done"""
        
        if self.ui.player1.get_points() == self.ui.player2.get_points():
            print("This game is a tie!\n")
        elif self.ui.player1.get_points() > self.ui.player2.get_points():
            print(player1_name, "wins!\n")
        else:
            print(player2_name, "wins!\n")
            
    def check_bust(self):
        """Check if any of the players has busted the game"""
        
        if self.ui.player1.get_points() > 21:
            print(player1_name, "busted.", player2_name, "wins!\n")
            self.bust = True
        elif self.ui.player2.get_points() > 21:
            print(player2_name, "busted.", player1_name, "wins!\n")
            self.bust = True

def game_instructions():
    """This function is to assist the players with the instructions on 
    how to play and a set of rules to follow by displaying on the interface
    before playing the game. 
    """
    
    instructions = '''
        "Welcome to Blackjack Game"
        ----------------------------------------------------
        Here are the instructions of Blackjack:
        1. The deck is shuffled before every game;
        2. Players will receive two cards at the beginning of the game; 
        3. Both players play in every round and each should decides whether 
           to hit another card or stand.
        
        The game ends when:
        - One player exceeds 21;
        - Both players decide to stand before 21 points and the winner 
          goes to the player with higher sum values of cards or 
          it is a draw when both get same value; 
        - One player gets blackjack at the beginning of the game;
        - Both get the blackjack and the game is a tie.
        
        Let's start the game!   
        ----------------------------------------------------
        '''    
    print(textwrap.dedent(instructions))
    
"""Display the instructions and rules before playing the game"""
game_instructions()

"""global variables to collect names of the players"""
player1_name = input("Player 1, enter your name: ")
player2_name = input("Player 2, enter your name: ")

print()

class Blackjack:
    """Blackjack class:        
    This class, composed of Deck, Player, UI, and Rules classes, is to create
    the game play and the user interface by taking in the inputs from the players 
    and determine the logic of the procedures and results at the end of the game.
    """  
    
    deck = None
    player1 = None
    player2 = None
    ui = None
    rules = None
    
    def __init__(self):
        """The constructor: initializing the objects"""
        self.deck = Deck()
        self.player1 = Player(self.deck)
        self.player2 = Player(self.deck)
        self.ui = UI(self.player1, self.player2)
        self.rules = Rules(self.ui)

    def start_game(self):
        """This method is to execute the game according to the game procedures: 
        shuffling deck, distributing cards to the players, checking the condition 
        of the values, determining the end results of the game upon the Hit-Stand 
        choices by the players and values of each player followed by asking players
        whether to play the game again.
        """        
        
        """Shuffle the deck"""
        self.deck.shuffle()
        
        print("----------------------------------------------------")
        print("Starting the game...\n")

        for i in range(2):
            """Distribute two cards to each player"""
            self.player1.add_card()
            self.player2.add_card()
        self.ui.print_points()
        
        """Check if any/both player(s) have a Blackjack"""
        self.rules.check_blackjack()
        
        if not self.rules.blackjack:
            """In the case of no Blackjack"""
            while not self.rules.bust and (not self.player1.stand or not self.player2.stand): 
                """while none of the players has busted the game and either player has not 
                chosen to stand"""
                
                """Check if any player has busted the game in their turn"""
                if self.ui.current_player == self.player1:
                    self.ui.choice(self.player1)
                    self.rules.check_bust()
                else:
                    self.ui.choice(self.player2)
                    self.rules.check_bust()
                    
                """Change turns to another player"""
                if self.ui.current_player == self.player1 and not self.player2.stand:
                    self.ui.current_player = self.player2
                elif self.ui.current_player == self.player2 and not self.player1.stand:
                    self.ui.current_player = self.player1
                
            """Check the final result if the players have chosen to stand but
            has not busted the game"""
            if not self.rules.bust:
                self.rules.check_result()
        
        print("----------------------------------------------------")
        
        """ask players if they want to play the game again"""
        self.ui.play_again()
        
"""Main Program"""
blackjack = Blackjack()
blackjack.start_game()
