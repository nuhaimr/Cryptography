#Name:Nuha Imran
#ID: 20696366
#Date: 19/06/23
#Title: DES encryption and decryption

import sys
import string
import binascii

# Initial Permutation (IP) table
initial_permutation = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

# Define the P-box permutation table
p_box_permutation = [
    16,  7, 20, 21,
    29, 12, 28, 17,
    1, 15, 23, 26,
    5, 18, 31, 10,
    2,  8, 24, 14,
    32, 27,  3,  9,
    19, 13, 30,  6,
    22, 11,  4, 25
]

# Expansion table (E)
EXPANSION_TABLE = [
    32, 1, 2, 3, 4, 5,
    4, 5, 6, 7, 8, 9,
    8, 9, 10, 11, 12, 13,
    12, 13, 14, 15, 16, 17,
    16, 17, 18, 19, 20, 21,
    20, 21, 22, 23, 24, 25,
    24, 25, 26, 27, 28, 29,
    28, 29, 30, 31, 32, 1
]

# S-boxes
S_BOXES = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

# Permutation (P) table
PERMUTATION_TABLE = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]

PC_1_TABLE = [
    57, 49, 41, 33, 25, 17, 9, 1,
    58, 50, 42, 34, 26, 18, 10, 2,
    59, 51, 43, 35, 27, 19, 11, 3,
    60, 52, 44, 36, 63, 55, 47, 39,
    31, 23, 15, 7, 62, 54, 46, 38,
    30, 22, 14, 6, 61, 53, 45, 37,
    29, 21, 13, 5, 28, 20, 12, 4
]

# Define the left shift values for each iteration
LSHIFT_MAP = {
    1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2,
    9: 1, 10: 2, 11: 2, 12: 2, 13: 2, 14: 2, 15: 2, 16: 1
}

# Final Permutation (FP) table
final_permutation = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

# Permutation 2 (PC-2) table
PC_2_TABLE = [
    14, 17, 11, 24, 1, 5, 3, 28,
    15, 6, 21, 10, 23, 19, 12, 4,
    26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40,
    51, 45, 33, 48, 44, 49, 39, 56,
    34, 53, 46, 42, 50, 36, 29, 32
]

# Step 1: Converting the hex to plaintext(hexadecimal string to binary representation
def hex_to_binary(hex_str):
    binary_val = ''
    for i in hex_str:
        binary_val += format(ord(i), '08b')
    return binary_val 

# Step 2: Converting plain text back to hex
def binary_to_hex(binstr):
    """convert a binary string to a hex"""
    yourString = ""
    for i in range(0, len(binstr), 8):
        bits = binstr[i:i+8]
        temp_char = chr(int(bits, 2))
        yourString += temp_char
    return yourString
#converting binary string to decimal value
def binary_to_decimal(input_bin):
    temp_binary = input_bin
    decimal_value, a, b = 0, 0, 0
    while(input_bin != 0):
        temp_decimal = input_bin % 10
        decimal_value = decimal_value + temp_decimal * pow(2, a)
        input_bin = input_bin // 10
        a += 1
    return decimal_value
#converting decimal value to binary string
def decimal_to_binary(number):
    binary_output = bin(number)
    binary_output = binary_output.replace("0b", "")
    if(len(binary_output) % 4 != 0):
        temp = len(binary_output) / 4
        temp = int(temp)

        count = (4 * (temp + 1)) - len(binary_output)
        for num in range(0, count):
            binary_output = '0' + binary_output
    return binary_output

# Step 3: Ensuring the plain text length is 64bits by padding
def pad_binary(binary):
    padding_length = 64 - (len(binary) % 64)
    for i in range(0, padding_length):
       binary = binary + '0'
    return binary

#Step 4: Ensure if key length is 64bits(padding and chopping)
def adjust_key_length(key):
    if len(key) > 64:
        key = key[:64]  
    elif len(key) < 64:
        key = pad_binary(key) 
    return key
    
#Step 5: Making a permute function
def permute(bits, permutation_table):
    permuted_bits = [bits[index - 1] for index in permutation_table]
    return ''.join(permuted_bits)

#Step 6: XOR function(just does basic XOR)
def xor(bits1, bits2):
    bits = []

    for i in range(len(bits1)):
        b1 = int(bits1[i])
        b2 = int(bits2[i])
        xor_bit = int(bool(b1) ^ bool(b2))
        bits.append(xor_bit)

    return ''.join(map(str, bits))
    
#Step 7: Left shift function:performs left shift
def lshift(c, d, iteration):
    for i in range(LSHIFT_MAP[iteration]):
        c = '%s%s' % (c[1:], c[0])
        d = '%s%s' % (d[1:], d[0])

    return (c, d)

# Step 8: Key Scheduler
def key_scheduler(initial_key):

    initial_key = hex_to_binary(initial_key)
    initial_key = adjust_key_length(initial_key)

    # Step 8.1: Perform PC-1 permutation
    key_permuted = permute(initial_key, PC_1_TABLE)

    # Step 8.2: Remove 8 parity bits
    key_no_parity = key_permuted[0:56]

    # Step 8.3: Break the 56 bits into two halves
    c = key_no_parity[0:28]
    d = key_no_parity[28:56]

    # Step 8.4: Perform left circular shift on each half
    round_keys = []
    for i in range(1, 17):
        c, d = lshift(c, d, i)
        round_key = permute(c + d, PC_2_TABLE)  # Perform PC-2 permutation
        round_keys.append(round_key)

    return round_keys
    
# Step 9: Expansion Permutation
def expansion_permutation(bits):
    expanded_bits = [bits[index - 1] for index in EXPANSION_TABLE]
    return ''.join(expanded_bits)
    
# Step 10: S-box substitution
def s_box_substitution(bits):
    sbox_output = ''
    for i in range(8):
        row = binary_to_decimal(int(bits[i * 6] + bits[i * 6 + 5]))
        column = binary_to_decimal(int(bits[i * 6 + 1] + bits[i * 6 + 2] + bits[i * 6 + 3] + bits[i * 6 + 4]))
        value = S_BOXES[i][row][column]
        sbox_output = sbox_output + decimal_to_binary(value)

    return sbox_output
    
# Step 11: The f function
def f(left, right, subkey, iteration):
    # Step 1: Expansion permutation
    expanded_right = expansion_permutation(right)

    # Step 2: First XOR
    xored_right1 = xor(expanded_right, subkey)

    # Step 3: S-box substitution
    sbox_output = s_box_substitution(xored_right1)

    # Step 4: Permutation
    permuted_output = permute(sbox_output, p_box_permutation)

    # Step 5: Second XOR
    xor_right2 = xor(left, permuted_output)

    left = xor_right2

    if iteration != 15:
        left, right = right, left
    

    return left, right
    
def des_encrypt(plaintext, round_keys):
    # Step 1: Convert the plaintext and key to binary strings
    plaintext_binary = hex_to_binary(plaintext)
    
    if len(plaintext_binary) % 64 != 0:
        plaintext_binary = pad_binary(plaintext_binary)
    
    # Step 4: Initial permutation
    list_block= []
    no_of_blocks = int(len(plaintext_binary) / 64)
    for i in range(no_of_blocks):
        block = plaintext_binary[i * 64:(i+1) * 64]
        block = permute(block, initial_permutation)
        left = block[0:32]
        right = block[32:64]
        for j in range(16):
            left, right = f(left, right, round_keys[j], j)
        combined = left + right
        ciphertext = permute(combined, final_permutation)
        list_block.append(ciphertext)

    ciphertext_hex = ''.join(list_block)

    return ciphertext_hex

#Doing reverse of encrypt
def des_decrypt(ciphertext, key):
    keys_reversed = key[::-1]
    plainText = des_encrypt(ciphertext, keys_reversed)
    return plainText
    
#method to write to file
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        file.write(data)
#method to read from file
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

#main menu function
def main():
    print("Welcome to the DES File Encryption/Decryption Program!")

    if len(sys.argv) != 3:
        print("Usage: python program.py <file_path> <operation> operation is either E for Encryption & D for decryption")
        exit(1)

    file = sys.argv[1]
    with open(file, 'r') as reader:
        plaintext = reader.read()

    choice = sys.argv[2]
    if choice.upper() == 'E':
        key = input("Enter the encryption key: ")
        round_keys = key_scheduler(key)
        cipher_text = des_encrypt(plaintext, round_keys)
        
        cipher_text1 = int(cipher_text, 2)
        cipher_text2 = hex(cipher_text1)[2:].zfill(len(cipher_text) // 4)
        output_file = input("Please enter the filename to write the encrypted text: ")
        write_to_file(output_file, cipher_text2)
    elif choice.upper() == 'D':
        key = input("Enter the decryption key: ")
        round_keys = key_scheduler(key)
        cipher_text3 = int(plaintext, 16)
        cipher_text4 = bin(cipher_text3)[2:]
        cipher_text5 = cipher_text4.zfill(len(plaintext) * 4)

        cipher_text5 = binary_to_hex(cipher_text5)
        text_decrypt = binary_to_hex(des_decrypt(cipher_text5, round_keys))
        
        output_file = input("Please enter the filename to write the decrypted text: ")
        write_to_file(output_file, text_decrypt)
    else:
        print("Invalid choice! Exiting...")

if __name__ == '__main__':
    main()


