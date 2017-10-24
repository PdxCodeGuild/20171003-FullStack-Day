# Practice: Blackjack

Let's start modeling a game of [blackjack](https://en.wikipedia.org/wiki/Blackjack) with three classes and their methods:

- `Card` class with a suit and a rank
- `Deck` class with a collection of cards
    - return the shuffled deck
    - cut the deck
    - draw a card off the top of a deck
- `Hand` class with a collection of cards from a deck.
    * add a card to a hand
    * allow a user to type in a hand and have it be converted into a `Hand` object
- Implemement these top-level functions
    * Start a new game of Blackjack, or Quit
    * Score a hand
    * Bust if the score is over 21

## Scoring

Cards have integer point values. Aces are 1 or 11, number cards are their number, face cards are all 10. A hand is worth the sum of all the points of the cards in it.
An ace is worth 1 when the hand it's a part of would be over 21 if it was worth 11.

## Advanced

*   Bring in your dealer hitting logic from the [21 practice problem](/practice/21.md) into a top-level function it's own module `dealer`.
    Update it to take in a `Hand` instance and return whether to hit.

*   Add a "card counting assistant" function in a module `advisor`.
    Have it take in a deck and a hand and print out the probability that you will bust.
    You can find the [expectation value](http://www.wikihow.com/Calculate-an-Expected-Value) of the score of your hand given one more card; basically the sum of the probability of the card multiplied by the resulting score of the hand with that card.

*   Add in a UI so a single user can play versus the dealer.

*   Allow multiple hands to be played with the same deck.