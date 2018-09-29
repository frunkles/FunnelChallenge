inputData = input('Enter a word: ')
dictionary = open('enable1.txt', 'r')
listDictionary = [];

for word in dictionary:
    listDictionary.append(word[:-1])

def funnel(string):
    most_words = 0

    # iterate through each letter to begin recursive method
    for char in range(0, len(string)):

        # set or reset numWords to 0
        num_words = 0

        # if the word is in the dictionary continue
        if string in listDictionary:
            # add one to numWords
            num_words += 1

            # set a temporary string to test without altering original
            # this will recursively happen so many strings are created and tested
            temp_string = string[0:char] + string[char + 1:len(string)]

            # begin recursion by calling funnel again using the temporary string
            # this will repeat the process using the new string and will add the number of words to the total
            num_words += funnel(temp_string)

        # if numWords is greater than mostWords found thus far, replace mostWords with numWords
        # this makes sure that only the best case scenario is used for the result
        if num_words > most_words:
            most_words = num_words

    return most_words


print(funnel(inputData))

for x in range(0, len(listDictionary)):
    if len(listDictionary[x]) > 10:
        funnel_length = funnel(listDictionary[x])
        print("Processing word", x, "of", len(listDictionary))
        if funnel_length == 10:
            print(word, "has 10 words its word funnel.")
            break