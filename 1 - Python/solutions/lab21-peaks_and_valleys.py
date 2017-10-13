"""
Lab 21: Peaks and Valleys
find 'peaks' and 'valleys' in a list of ints
a 'peak' is a number which is greater than the number on the left and right
a 'valley' is a number which is less that the number on the left and right

                                                      X                 X
                                                   X  X  X           X  X
                              X                 X  X  X  X  X     X  X  X
                           X  X  X           X  X  X  X  X  X  X  X  X  X
                        X  X  X  X  X     X  X  X  X  X  X  X  X  X  X  X
                     X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
                  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
               X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
            X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X  X
>>> data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
>>> peaks(data)
[6, 14]
>>> valleys(data)
[9, 17]
"""


# find the indices of the peaks
def peaks(data):
    peak_indices = []
    for i in range(1, len(data)-1): #loop through the list, avoiding the end-points
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak_indices.append(i)
    return peak_indices


# find the indices of the valleys
def valleys(data):
    valley_indices = []
    for i in range(1, len(data)-1):
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left > middle and right > middle:
            valley_indices.append(i)
    return valley_indices


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    print(peaks(data))
    print(valleys(data))

main()

'''
Here's an alternative version, using a regular for-loop with continue to over the first and last values.

def peaks(data):
    peak_indices = []
    for i in range(0, len(data)): #loop through the list, avoiding the end-points
        if i == 0 or i == len(data)-1:
            continue
        left = data[i-1]
        middle = data[i]
        right = data[i+1]
        if left < middle and right < middle:
            peak_indices.append(i)
    return peak_indices
'''


