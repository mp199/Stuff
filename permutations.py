def permutation(string, start, end):
    # Prints the permutations
    if start == end - 1:
        print(string)
    else:
        for current in range(start, end):
            # Fixing a character
            x = list(string)
            temp = x[start]
            x[start] = x[current]
            x[current] = temp

            # Recursively calling function permutation() for rest of the characters.
            # Every permutation loops "n" times (start increases by 1) until it is printed. Then it goes back to the
            # first for loop and computes the next permutation (current increases by 1) and repeats the process.
            permutation("".join(x), start + 1, end)


string = input('Enter a string: ')
n = len(string)
print("All the permutations of the string are: ")
permutation(string, 0, n)

