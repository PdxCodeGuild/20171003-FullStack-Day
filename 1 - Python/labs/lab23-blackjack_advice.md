# Lab 23: Blackjack I


Let's write a python program to give basic blackjack playing advice during a game by asking the player for cards.

First, ask the user for _three_ playing cards.
Save the user's inputs as a _string_: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K.

Then, figure out the point value of each card individually.
Number cards are worth their number, all face cards are worth 10.
At this point, assume aces are worth 1.

Now, in Blackjack, aces can be worth 11 if they won't put the total point value of both cards over 21.

Lastly, figure out what the playing advice will be.  Use the following rules:

* Less than 17, advise to "Hit"
* Over or equal to 17, advise to "Stay"
* Exactly 21, advise "Blackjack!"
* Over 21, advise "Already Busted"

Then print out the current total point value and the advice.

```
What's your first card?
> Q

What's your second card?
> 2

What's your third card?
> 3

15 Hit

What's your first card?
> K

What's your second card?
> 5

What's your third card?
> 5

> 20 Stay

What's your first card?
> Q

What's your second card?
> J

What's your third card?
> A

21 Blackjack!
```

-------------------------------
