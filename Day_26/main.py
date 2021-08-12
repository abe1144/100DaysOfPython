import pandas as pd


nato = pd.read_csv("nato_phonetic_alphabet.csv")


nato_dict = {row['letter']: row['code'] for (index, row) in nato.iterrows()}

print(nato_dict)

# Create a list of the phonetic code words from a word that the user inputs.
word = input("Enter a word: ").upper()

print([nato_dict[letter] for letter in word])
