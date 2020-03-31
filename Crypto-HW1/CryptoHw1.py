from collections import Counter
import math
from itertools import starmap, cycle


# Uses Counter to get the frequency of letters in provided text
def frequencyAnalysis(input_text):
    frequency = Counter(input_text)
    return frequency


# Shift Cipher encrypt
def shiftCipherEncrypt(input_text, input_shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    input_shift = int(input_shift)


    # Iterate over the characters in the input text
    # find location of character in comparision to its location in the aplhabet
    # Mod 26 the sum of the location and shift
    # Append new letter to output
    for i in range(len(input_text)):
        current_letter = input_text[i]
        current_location_of_letter = alphabet.find(current_letter)
        new_location_letter = (current_location_of_letter + input_shift) % 26
        output += alphabet[new_location_letter]
    return output

# Shift Cipher decrypt
def shiftCipherDecrypt(input_cipher_text, input_shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''

    # Iterate over the characters in the cipher text
    # find location of character in comparision to its location in the aplhabet
    # Mod 26 the difference of the location and shift
    # Append new letter to output
    for i in range(len(input_cipher_text)):
        current_letter = input_cipher_text[i]
        index = alphabet.find(current_letter)
        index = (index - input_shift) % 26
        output = output + alphabet[index]

    return output


# Affine Cipher encrypt
def affineCipherEncrypt(input_text, a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''

    # If a is not a co-prime of a then raise error
    if math.gcd(a, 26) != 1:
        raise ValueError("a and 26 are not co-primes. Try again.")

    # If input text contains white spaces, raise an error
    if ' ' in input_text:
        raise ValueError("Please enter a text with no spaces")

    # Iterate over input text
    # Get location of letter in comparision to its location in the alphabet
    # x is the product of a and the index plus b mod 26
    # x index is x mod 26
    # Append i to the output text
    for i in range(len(input_text)):
        current_letter = input_text[i]
        index = alphabet.find(current_letter)
        x = a * index + b % 26
        x_index = x % 26
        i = alphabet[x_index]
        output += i

    return output

# Gets inverse of a based of 26
def getInverse(a):
    result = 1
    for i in range(1, 26):
        if (a * i) % 26 == 1:
            result = i
    return result



# Affine Cipher decrypt
def affineCipherDecrypt(input_cipher_text, a, b):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''

    # If a is not a co-prime of 26 then raise error
    if math.gcd(a, 26) != 1:
        raise ValueError("a and 26 are not co-primes. Try again.")

    # Iterate over cipher text
    # Get location of letter in comparision to its location in the alphabet
    # Get the inverse of a
    # set plain text input to a * (character index-b) mod 26
    # Check is the plain text iindex is less than 0
    # append character found to plaintext
    # appends plain text to output
    for character in input_cipher_text:
        character_index = alphabet.index(character)
        inverse_of_a = getInverse(a)
        plain_text_index = inverse_of_a * (character_index - b) % 26
        if plain_text_index < 0:
            plain_text_index += 26
        plain_text = alphabet[plain_text_index]
        output += plain_text

    return output

# Viginere Encryption
def viginereEncrpyt(input_text, input_key):

    # Converts input_text to all uppercase letters
    input_text = filter(str.isalpha, input_text.upper())

    # Encrypts charachter-by-charachter
    # ord() returns an integer representing the unicode code point of the character
    # chr() function takes integer argument and return the string representing a character at that code point
    def encrypt(character, key):
        return chr(((ord(key) + ord(character) - 2 * ord('A')) % 26) + ord('A'))

    # Zips the characters back together to make the cipher text
    return ''.join(starmap(encrypt, zip(input_text, cycle(input_key))))

# Viginere Decryption
def viginereDecrypt(cipher_text, key):

    # Decrypts character-by-charcter
    def decrypt(character, key):
        return chr(((ord(character) - ord(key) - 2 * ord('A')) % 26) + ord('A'))

    # Zips plain text characters back into plain text message as all Uppercase and no spaces
    return ''.join(starmap(decrypt, zip(cipher_text, cycle(key))))


if __name__ == '__main__':

    # Implementation of Frequency Analysis
    user_input = input("Please enter text you would like to get analysed: ")
    freq_result = frequencyAnalysis(user_input)
    print(f"Frequency of letters in text provided: {freq_result}")
    
    # Implementation of Shift Cipher encrypt
    user_input = input("Please enter text you would like to encrypt with shift cipher: ")
    shift = input("Please enter shift you would like to use: ")
    cipher_text = shiftCipherEncrypt(user_input, shift)
    print(f"Encrypted cipher text: {cipher_text}")
    
    # Implmentation of Shift Cipher decrypt using freq_analysis function from Question 1
    cipher_text = "xultpaajcxitltlxaarpjhtiwtgxktghidhipxciwtvgtpilpitghlxiwiwtxgqadd"
    freq_result = frequencyAnalysis(cipher_text)
    print(f"Text provided: {cipher_text}")
    print(f"Frequency of letters in text provided: {freq_result}")
    # Most frequent letter in the cipher text was 't', postion from 'e' -> 't' is 15
    # Determined key for this cipher text was 15
    shift = int(input("Please enter key: "))
    plain_text = shiftCipherDecrypt(cipher_text, shift)
    print(f"Plain text message: {plain_text}")
    
    # Implementation of Affine cipher encrypt and decrypt
    user_input = input("Please enter text you would like to get encrypted: ")
    print("Make sure a is a co-prime of 26!!!")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    cipher_text = affineCipherEncrypt(user_input, a, b)
    print(f"Your cipher text: {cipher_text}")
    plain_text = affineCipherDecrypt(cipher_text, a , b)
    print(f"Your plain text: {plain_text}")


    # Implementation of Viginere encrypt and decrypt
    # Uses two keys
    plain_text = "Hellenism was the combination of Greek, Persian, and Egyptian cultures. During this remarkable time period, people were encouraged to pursue a formal education and produce many different kinds of art. New forms of math, science, and design made a great impact on society"
    input_key_1 = "How much wood would a woodchuck chuck if a woodchuck could chuck wood?"
    cipher_text = viginereEncrpyt(plain_text, input_key_1)
    print(f"Cipher text using key #1: {cipher_text}")
    plain_text = viginereDecrypt(cipher_text, input_key_1)
    print(f"Plain text: {plain_text}")
    input_key_2 = "Out of the three operating systems, linux is by far my favorite."
    cipher_text = viginereEncrpyt(plain_text, input_key_2)
    print(f"Cipher text using key #1: {cipher_text}")
    plain_text = viginereDecrypt(cipher_text, input_key_2)
    print(f"Plain text: {plain_text}")
   



   
