# Blackjack

This is a simplified version of command-line Blackjack game, implemented in Python and the OO paradigm.

The solution includes features such as:
1. Implementation of classes and relationships between each class;
2. Game logic and its implementation using different types of control structures;
3. Asking users their names to make the interface more friendly and presentable;
4. List of instructions and rules provided in order to have the players familiar 
with the game; and
5. Users being able to choose to play again without restarting the application.

### How to Play
1. The deck is shuffled before every game.
2. At the beginning both players get two cards which are visible to both players.
3. Both players play in every game round.
4. In every round each player should decide whether he hits another card or stands. (When the hand is closing to 21 points, exceeding 21 total with a new card is more probable.) New cards in the game are still visible for both players.
5. The first player who exceeds the 21 or decides to stand, must wait for the opponent to play.

### Win/Lose Conditions
- The player wins after exceeding 21 points;
- Both players decide to stand before 21 points and the winner goes to the player with higher sum values of cards or 
  it is a draw when both get same value; 
- If one player gets blackjack at the beginning of the game, the only way to win for the opponent is to get exactly 21;
- Both get the blackjack and the game is a tie.

### How to Install

You can download the project directly from the master branch or clone it using gitbash:
```
git clone github.com/einyan03/blackjack.git
cd blackjack
```

If you have already installed python and want to run the script, open the terminal and run the following commend line: 
```
$ python blackjack.py
```

### Limitations
This provided solution only acts as the most simplified version of a Blackjack game that aims to provide understandings on OOP paradigm alongside the usage of proper control structures for the implementation of algorithms. Hence, the current solution lacks to provide intricate game play and features as per the standards of general Blackjack and there is room for improvement in terms of code style and quality followed by a more user-friendly approach.
