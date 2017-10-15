

# LCR Simulator

LCR is a dice game, one of pure chance. Therefore, we can write a simulator to avoid wasting the time playing it ourselves. Description from wikipedia:


> Each player receives at least 3 chips. Players take it in turn to roll three six-sided dice, each of which is marked with "L", "C", "R" on one side, and a single dot on the three remaining sides. For each "L" or "R" thrown, the player must pass one chip to the player to his left or right, respectively. A "C" indicates a chip to the center (pot). A dot has no effect.

>If a player has fewer than three chips left, he is still in the game but his number of chips is the number of dice he rolls on his turn, rather than rolling all three. When a player has zero chips, he passes the dice on his turn, but may receive chips from others and take his next turn accordingly. The winner is the last player with chips left. He does not roll the dice, and wins the center pot. If he chooses to play another round, he does not roll 3, he keeps his pot and plays with that.


When the program starts, it should ask for the names of the players, until the user enters 'done'. Then it should run the simulation, tell the user who won, and ask the player whether they'd like to play again.
