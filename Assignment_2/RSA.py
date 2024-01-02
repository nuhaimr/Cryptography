#Name:Nuha Imran
#ID: 20696366
#18/07/2023

#Random library for random prime numbers
#Sys for command line arguments
import random
import sys

'''Is a prime number test, if number less than 1 means not a prime so return false or go in the
loop if greater than 1 then iterate over range of 2 to the square root including plus 1 The reason for iterating up to the square root of num is that if num has any divisors greater than its square root, it must also have a corresponding divisor smaller than its square root. This property helps to reduce the number of iterations and improve the efficiency of the primality test,  If num is divisible by i, it means num is not a prime number, as it has a divisor other than 1 and itself. In this case, the function immediately returns False, indicating that num is not prime.If the loop completes without finding any divisors for num, it means that num is a prime number, as it has no divisors other than 1 and itself. In this case, the function returns True, indicating that num is prime. '''
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
    
'''This is a prime test called miller-rabin that checks if a number if prime or not'''
def is_probable_prime(n, k=10):
    # Miller-Rabin primality test
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Write n-1 as 2^r * d, where d is odd
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Perform k iterations of the Miller-Rabin test
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True

'''this function generates a large prime number greator than 2^64 using the random library'''
def generate_random_large_prime():
    num = random.randint(2**64, 2**65)
    while not is_probable_prime(num):
        num = random.randint(2**64, 2**65)
    return num

'''This is the extended euclidean algorithm that is used to find the greatest common divisor of two numbers 'a' and 'b' as well as their coeffecients x and y such that gcd = a*x + b*y this determines whether a numver is prime or not'''
def gcd_extended(a, b):
    if b == 0:
        return a, 1, 0
    else:
        gcd, x1, y1 = gcd_extended(b, a % b)
        x = y1
        y = x1 - (a // b) * y1
        return gcd, x, y

'''makes it easier to find phi because if a p*q = n where p and q are both primes then phi would be equal to eulers totient function'''
def euler_totient(p, q):
    return (p - 1) * (q - 1)

'''this ensures that RSA encryption and decryption operations are inverse operations, allowing to encrypt data using public key (n,e) and decrypt data using the private key (n,d)'''
def mod_inverse(a, m):
    gcd, x, y = gcd_extended(a, m)
    return x % m

'''this method simply generates keys generates to large numbers finds their products finds their pho performs the neceesary operations and forms both keys'''
def generate_keys():
    p = generate_random_large_prime()
    q = generate_random_large_prime()
    n = p * q
    phi = euler_totient(p, q)

    e = random.randint(2, phi - 1)
    while gcd_extended(e, phi)[0] != 1:
        e = random.randint(2, phi - 1)

    d = mod_inverse(e, phi)

    with open('public_key.txt', 'w') as key_file:
        key_file.write(f"{e}\n{n}")

    with open('private_key.txt', 'w') as private_key_file:
        private_key_file.write(f"{d}\n{n}")

    return e, d, n

'''this is the functions for binary modular exponetion however its implemented in python so i did not make one myself,this plays a role in encryption and decryption'''
def mod_exp(base, exponent, modulus):
    return pow(base, exponent, modulus)

'''converts a single letter from the plaintext using RSA encryption'''
def encrypt_character(character, e, n):
    ciphertext = mod_exp(ord(character), e, n)
    return ciphertext

'''ecrypts entire text message using RSA algo'''
def encrypt_text(text, e, n):
    encrypted_text = [encrypt_character(char, e, n) for char in text]
    return encrypted_text

'''converts the cipher text that is a list of integers to a hexadecimal string'''
def convert_to_hex(ciphertext):
    hex_ciphertext = ' '.join([hex(char)[2:].zfill(2) for char in ciphertext])
    return hex_ciphertext

'''converts ciphertext into its decimal then performs mod_exp in reverse passing the decimal ciphertext and d and n as arguments this decrypts the integer value back to its plaintext representation'''
def decrypt_character(ciphertext, d, n):
    decimal_ciphertext = int(ciphertext, 16)
    plaintext = chr(mod_exp(decimal_ciphertext, d, n))
    return plaintext

def decrypt_text(ciphertext, d, n):
    # Decrypt the entire ciphertext character by character
    decrypted_text = [decrypt_character(char, d, n) for char in ciphertext]
    return "".join(decrypted_text)

def main():
#basic command line arguments with choices
    if len(sys.argv) != 4:
        print("Usage: python program.py [input_file] [output_file] [operation]")
        print("Operation should be E for Encryption or D for decryption.")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]
    operation = sys.argv[3]

    if operation.upper() == 'E':
        e, d, n = generate_keys()

        with open(input_file, 'r') as file:
            plaintext = file.read()

        encrypted_text = encrypt_text(plaintext, e, n)
        hex_encrypted_text = convert_to_hex(encrypted_text)

        with open(output_file, 'w') as file:
            file.write(hex_encrypted_text)

        print("Encryption is completed.")
    elif operation.upper() == 'D':
        # Read 'd' and 'n' from the file & split it back
        with open('private_key.txt', 'r') as key_file:
            d, n = map(int, key_file.read().split())

        with open(input_file, 'r') as file:
            hex_ciphertext = file.read()
            #ciphertext = [int(hex_ciphertext[i:i+2], 16) for i in range(0, len(hex_ciphertext), 2)]
            ciphertext = hex_ciphertext.split(" ")

        decrypted_text = decrypt_text(ciphertext, d, n)

        with open(output_file, 'w') as file:
            file.write(decrypted_text)

        print("Decryption is completed.")
    else:
        print("Invalid operation! Use 'E' for encryption or 'D' for decryption.")
        sys.exit(1)

if __name__ == '__main__':
    main()


