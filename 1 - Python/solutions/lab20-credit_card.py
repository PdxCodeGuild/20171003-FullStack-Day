# lab 20: validate a credit card number

# 1) Slice off the last digit. That is the check digit.
# 2) Reverse the digits.
# 3) Double every other element in the reversed list.
# 4) Subtract nine from numbers over nine.
# 5) Sum all values.
# 6) Take the second digit of that sum.
# 7) If that matches the check digit, the whole card number is valid.


def get_second_digit(num):
    if num < 10:
        return None
    #num_str = str(num)
    #return int(num_str[1])
    return num%10


def validate_credit_card(cc_str):
    if len(cc_str) != 16:
        return False

    # convert the string into a list of ints
    cc = []
    for i in range(len(cc_str)):
        cc.append(int(cc_str[i]))

    check_digit = cc.pop(-1)       # step 1
    cc.reverse()                   # step 2
    for i in range(0, len(cc), 2):
        cc[i] *= 2                 # step 3
    total = 0
    for i in range(len(cc)):
        if cc[i] > 9:
            cc[i] -= 9             # step 4
        total += cc[i]             # step 5
    second_digit = get_second_digit(total)  # step 6
    return second_digit == check_digit


# credit_card_str = input('enter your credit card: ')
credit_card_str = '4556737586899855'
print(validate_credit_card(credit_card_str))