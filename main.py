# Assignment 5

#  I certify, that this computer program submitted by me is all of my own work.
#  Signed: Layla Heath
'''
This program uses words from a text document to translate basic
English sentences to Hmong.
'''

def load_dictionary(filename):
    # Read the file containing the tuples, insert the entries into the dictionary 
    # and return the dictionary object
    dict = {}
    word_file = open(filename, 'r')
    for line in word_file:
        num, hmong, eng = line.strip().split(",")
        dict[eng] = hmong
    return dict


def translate(sentence):
    # Take a sentence in English and return a sentence in Hmong
    new_sent = []
    hmong_words = []


    for i in sentence:
        if i.isalpha() or i.isspace():
            new_sent += i
    new_sent = ''.join(new_sent).lower()

    word_list = new_sent.split(' ')

    # print(f"Separated English Words: {word_list}")
    for word in word_list:
        try:
            hmong_words += [dictionary[word]]
        except KeyError:
            hmong_words += ["?"]
    # print(f"Hmong list:{hmong_words}")
    hmong_sent = " ".join(hmong_words)
    return hmong_sent


def print_word_frequency(dictionary, word_list):
    filtered_list = []
    for word in word_list:
        new_word = []
        for i in word:
            if i.isalpha() or i.isspace():
                new_word += i
        filtered_list += [''.join(new_word)]
    for word in word_list:
        if word in dictionary:
            print(f"{word} : {word_list.count(word)}")


# print the frequency of English words   that were translated

def main():  # main logic loop
    print("This program will translate basic English sentences into a Hmong sentence.")
    # established 'dictionary' as a global variable so it can be accessed by the entire program
    global dictionary
    # sets filename to the file we were given "HmongWords.txt"
    filename = "HmongWords.txt"
    # loads a dictionary from the assigned file
    dictionary = load_dictionary(filename)
    # An empty list is created that will alter be filled with all the words translated
    words_used = []
    another = 'Y'
    while another != 'N':
        sentence = input("\nType your English sentence: ")


        for i in sentence.split(' '):
            words_used += [i.lower()]


        translation = translate(sentence)
        print(f"\nHmong: {translation}")

        try:
            # exception handler in the case that the user does not input a Y or N that ends the loop
            another = input("\nAnother translation [Y/N]: ")
            if another != 'Y' and another != 'N':
                raise ValueError
        except ValueError:
            print("Invalid Entry. ")
            break
    print("\n", "-"*20,"\n")
    print_word_frequency(dictionary, words_used)


main()
