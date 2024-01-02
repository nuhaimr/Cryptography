#Name: Nuha Imran
#ID: 20696366
#Date: 16/06/23
#Title: Letter frequency Analysis Attack

import string
import sys

# Step 1: Reading the file that has to be decrypted
if len(sys.argv) != 2:
    print("Usage: python Q1a.py <file_path>")
    exit(1)

try:
    with open(sys.argv[1]) as f:
        message = f.read()
except FileNotFoundError:
    print("File not found.")
    exit(1)

# Step 2: Removing all characters and formatting that would interfere with the process
message = message.lower()

# Step 3: Checking all occurrences of letters in the text to evaluate the repeated frequencies this part only counts total length
message_length = len(message)

#Storing the letter count in a dictionary as letter: count
letter_counts = {letter: message.lower().count(letter) for letter in string.ascii_lowercase}
#Based on the count forming a dictionary for frequency as letter : frequency
letter_frequencies = {letter: (count / message_length) for letter, count in letter_counts.items()}


# Step 4: Putting in the dictionary of English letter analysis because the encrypted text is in English
eng = {
    'e': 12.49, 't': 9.28, 'a': 8.04, 'o': 7.64, 'i': 7.57, 'n': 7.23,
    's': 6.51, 'r': 6.28, 'h': 5.05, 'l': 4.07, 'd': 3.82, 'c': 3.34,
    'u': 2.73, 'm': 2.51, 'f': 2.40, 'p': 2.14, 'g': 1.87, 'w': 1.68,
    'y': 1.66, 'b': 1.48, 'v': 1.05, 'k': 0.54, 'x': 0.23, 'j': 0.16,
    'q': 0.12, 'z': 0.09
}

# Step 5: Creating a mapping dictionary based on the frequencies in a logical way as text letter frequency:english letter frequency after sorting them
mapping_dict = {}
sorted_text_frequencies = sorted(letter_frequencies, key=lambda x: letter_frequencies[x], reverse=True)
sorted_eng_frequencies = sorted(eng, key=lambda x: eng[x], reverse=True)

for i in range(len(sorted_text_frequencies)):
    mapping_dict[sorted_text_frequencies[i]] = sorted_eng_frequencies[i]
    
for cipher_letter, plain_letter in mapping_dict.items():
    print(f"{cipher_letter} -> {plain_letter}")

# Step 6: Decrypting the text based on the mapping dictionary
decrypted_text = ""
for letter in message:
    decrypted_letter = mapping_dict.get(letter, letter)
    decrypted_text += decrypted_letter

# Step 7: Writing the decrypted text to an output file
with open('decrypted_output.txt', 'w') as f:
    f.write(decrypted_text)
























