# Lab 6: Magic 8-Ball

Let's write a program to simulate the classic "[Magic Eight Ball](https://en.wikipedia.org/wiki/Magic_8-Ball)"

## Concepts Covered

- input, print
- import
- random.choice

## Instructions

1. Print a welcome screen to the user.
2. Use the random module's `random.choice()` to choose a prediction.
3. Prompt the user to ask the 8-ball a question "will I win the lottery tomorrow?"
5. Display the result of the 8-ball.


Below are some example 'predictions':

- It is certain
- It is decidedly so
- Without a doubt
- Yes definitely
- You may rely on it
- As I see it, yes
- Most likely
- Outlook good
- Yes
- Signs point to yes
- Reply hazy try again
- Ask again later
- Better not tell you now
- Cannot predict now
- Concentrate and ask again
- Don't count on it
- My reply is no
- My sources say no
- Outlook not so good
- Very doubtful


## Version 2

Using a `while` loop, keep asking the user for a question, if they enter 'done', exit