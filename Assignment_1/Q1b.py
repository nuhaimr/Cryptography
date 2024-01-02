#Name:Nuha Imran
#ID:20696366
#Date:17/06/2023
#Title: Affline Cipher Bruteforce-Attack

import sys #necessary for cmd arguments

# Step 1: Read the encrypted text from a file(Strip is to remove trailing white spaces for decryption process)
def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            encrypted_text = f.read().strip()
        return encrypted_text
    except FileNotFoundError:
        print("File not found.")
        exit(1)

# Step 2: Defining all necessary functions needed for the decryption
# Step 2a:Function to calculate the greatest common divisor (GCD) of two numbers
# Reasoning:Needed because if a and m are not coprimes the key a,b is not possible
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

# Step 2b: Function to find the modular inverse of a number
# Reasoning: If a modular inverse does not exist then the a,b keys cannot be used for decryption
def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Step 2c: Function to check if a word is present in the decrypted text
# Reasoning: Simply an extra function to ensure the right decrypted key is being chosen
def check_word_in_text(word, decrypted_text):
    decrypted_words = decrypted_text.lower().split()
    if word.lower() in decrypted_words:
        return True
    return False

# Step 3: Setting up all necessary variables and lists
# Step 3a: Define the alphabet (characters that can be encrypted)
alphabet = 'abcdefghijklmnopqrstuvwxyz'

#Step 3b: Basic English word list for checking words(small dictionary for checking words that exist in most sentences)
english_words = ['the', 'you', 'are', 'of', 'are', 'a']

# Step 4: Performing the brute-force attack
# Step 4a: Read the file path from command line argument & error checking
if len(sys.argv) < 2:
    print("Please provide the file path as a command line argument.")
    exit(1)
file_path = sys.argv[1]

# Step 4b: Read the encrypted text from the file
encrypted_text = read_file(file_path)

# Step 5: Decrypting the text using the brute-force approach
possible_keys = []

for a in range(1, 26):
    if gcd(a, 26) == 1:
        for b in range(26):
            decrypted_text = ''

            # Step 6: Decrypt the text using the current key pair
            for char in encrypted_text:
                if char.isalpha(): #checking if alphabetical then proceed if not append any symbol . etc
                    char_idx = alphabet.index(char.lower())
                    a_inverse = mod_inverse(a, 26)
                    decrypted_char_idx = (a_inverse * (char_idx - b)) % 26 #using formula for decryption of affine
                    decrypted_char = alphabet[decrypted_char_idx]
                    decrypted_text += decrypted_char
                else:
                    decrypted_text += char

            # Step 7: Check if the decrypted text contains basic English words
            if all(check_word_in_text(word, decrypted_text) for word in english_words):
                possible_keys.append((a, b))
                print("Possible key found: a={}, b={}".format(a, b))
                print("Decrypted text: {}".format(decrypted_text))
                print()
                
# Step 8: Decrypt the text using the correct key
if len(possible_keys) > 0: # checking if a key is found in brute force and exists then using that key to store entire decrypted text and priting it
    for key in possible_keys:
        a, b = key
        decrypted_text = ''

        for char in encrypted_text:
            if char.isalpha():
                char_idx = alphabet.index(char.lower())
                a_inverse = mod_inverse(a, 26)
                decrypted_char_idx = (a_inverse * (char_idx - b)) % 26
                decrypted_char = alphabet[decrypted_char_idx]
                decrypted_text += decrypted_char
            else:
                decrypted_text += char

        print("Decrypted text with key (a={}, b={}):".format(a, b))
        print(decrypted_text)
else:
    print("No possible keys found.")




