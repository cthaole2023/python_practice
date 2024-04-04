"""
parameter: a 2d list of ints, size no matter
purpose: finds the min in each list and stores them in a lil list and returns said list
"""
def find_min(num_list):
    the_min = num_list[0][0]
    # when finding the min, you cannot predict if the min will be 0, -100, or 1000, so you should ideally put the
    # first index as your min / max. however for a max, if you know the numbers are all positive, zero is a safe bet
    mins = []
    # stores all the minimums
    m = 0
    # iterates through the list, if you're uncomfortable with a while loop, i can also show a for loop ex as well
    while m < len(num_list):
    # while there are sublists in the 2d list you havent iterated
        for i in range(len(num_list[m])):
        # for each integer in the sublist
            if the_min > num_list[m][i]:
            # if the next int in the list is greater, there will be a new min
            # say if this was a max func, you would want to check something else, similar to what's written ^^
                the_min = num_list[m][i]
                print(f"the_min = {the_min}")
                # so you can see what the min is as its running
        mins.append(the_min)
        # appends the mins of each sublist to the list of mins
        m += 1
        # moves on to the next sublist
    return mins

"""
counts how many vowels they're in a given string, totaled, and prints all the vowels in the given string 
"""
def num_of_vowels(string):
    my_dict = {'a': 0, 'e': 0, 'i': 0, 'u': 0, 'o': 0}
    total = 0
    for char in string:
        if char in my_dict:
            my_dict[char] += 1
            total += 1
    print(f"they're {total} vowels in this string ")
    """
    another way to calc total while iterating through a dict, not practical but good practice w/dictionares 
    for vowel in my_dict:
        total += my_dict[vowel]
    """
    """
    practice to iterate through a dict and with a print statement you can also visualize string concatenation 
    """
    vowel_string = ''
    for vowel in my_dict:
        for i in range(my_dict[vowel]):
            #print(f"{vowel_string} += {vowel}")
            vowel_string += vowel
    return vowel_string


"""
given a num >= 2 it will give u that fibonacci number
"""
def fibonacci(num):
    # base case
    if num == 0:
        return 0
        # the sequence is assuming they're no neg number, fib of 0 = 0
    # base case
    if num == 1:
        return 1
        # the sequence is assuming they're no neg number, fib of 1 = 1
    else:
        total = fibonacci(num - 1) + fibonacci(num - 2)
        # the fibonacci sequence is defined as the sum of all the num before it up to but not including that last num
        # recursively it's defined as Fibonacci of n = Fibonacci of n - 1 + Fibonacci of n - 2
        # wiki the sequence if you don't know, the golden ratio deserves some love, this is python not calc 2.
        return total
        # try drawing it out all the way down to 1 and 0, wish you could draw on github


"""
string slices and recursion 
parameters is a string and the goal is to reverse whatever string is given and return said reversal 
"""
def recur_reverse_strings(string):
    new_string = ''
    # the reversal of the given string
    if string == '':
        return ''
        # once you go through the entire string, it returns '' bc that's the reverse of an empty string
    else:
        new_string = string[len(string) - 1] + recur_reverse_strings(string[:len(string) - 1])
        # you want start with the last letter in the string when writing the word in reverse. ex: apple -> "write" e 1st
        # len(string) - 1 refers to the last letter in the string
        # the recursive call is here because we're trying to get the new last letter in the string, by chopping off the
        # letter we already "wrote" down. chopping = string[:len(string) - 1]
        return new_string


def evaluating_booleans():
# guess the code output of these booleans
    the_str = ''
    print(not the_str)
    the_str = 'minions'
    print('m' in the_str or ' ' in the_str)
    print(('m' in the_str or ' ' in the_str) and (not 'i' in the_str))
    my_dict = {'apple': 5, 'banana': 3, 'blueberry': 1, 'orange': 4}
    print(5 in my_dict)
    print('banana' in my_dict)
    print(not 1 in my_dict)


if __name__ == '__main__':
    my_list = [[1, 4, 7, 8], [1, 3, 44], [9, 0, 5, 6]]
    print(find_min(my_list))
    word1 = "some random gibberish string of words that has vowels"
    word2 = "testing" # this word has 2 vowels and is used for testing purposes
    print(num_of_vowels(word1))
    print(num_of_vowels(word2))
    print(fibonacci(5))
    print(recur_reverse_strings("apple"))
    evaluating_booleans()