
# Lab: Calculator


For this lab, we'll create a simple calculator using jQuery and a CSS library. You can find some examples of calculators on [Google](https://www.google.com/search?q=calculator+screenshot&rlz=1C1CHBF_enUS752US752&source=lnms&tbm=isch&sa=X&ved=0ahUKEwie2JG15M3WAhUQ-mMKHUdsCnkQ_AUICigB&biw=1536&bih=772&dpr=1.25). It should support the following functions at minimum.

- 0-9 and . (decimal place)
- = (show result)
- +/- (negate the number)
- % (divide the number by 100)
- \+ \- \* \\ (basic arithmetic)
- backspace

## Advanced

You can pick from any of these advanced features.

- `^` (exponentiation)
- `sin`, `cos`, and `tan`
- `!` (factorial)

Enable keyboard input.

Use unicode charcters like ÷ and × rather than / and *

Show the ongoing operation above the main calculator screen. E.g. if the user enters `5` and then presses `*`, erase the screen and show `5*` above the main screen. If the user then presses `2` and presses `=`, show `5*2=` above the main screen, and `10` in the main screen.

If the user presses an operator after the result is shown, take the result and make it the first operand. E.g. if the user hits `5`, `*`, `2`, `=`, show `10`. If they then press `*` again, `10` would become the first operand, and it would erase the screen for the user to enter the second operand.

If the user presses `=` multiple times, keep applying the operation to the result. E.g. the user enters 5, *, 2, then hits = showing 10. If they hit = again, it'd show 20, and again, it'd show 40.


