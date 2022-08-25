import pandas

nato = pandas.read_csv("nato_phonetic_alphabet.csv")

dictionary = {row.letter:row.code for (index,row) in nato.iterrows()}
print(dictionary)

on = True
while on:
    word = input("Enter a word: ").upper()
    try:
        codes = [dictionary[letter] for letter in word]
    except KeyError:
        print("Sorry, Only letters in the alphabet please.")
    else:
        print(codes)
        on = False
