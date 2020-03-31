import math

# Uses Counter to get the frequency of letters in provided text
def frequencyAnalysis(input_text):
    frequency = {}
    for keys in input_text:
        frequency[keys] = frequency.get(keys, 0) + 1
    return frequency

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


    for i in range(len(input_text)):
        current_letter = input_text[i]
        index = alphabet.find(current_letter)
        c = a * index + b % 26
        cIdx = c % 26
        i = alphabet[cIdx]
        output += i

    return output



def IndexOfCoincidence(input_text, freq):
    string_length = len(input_text)
    x = 0
    for value in freq.values():
        x += ((value / string_length) ** 2)
    return x




if __name__ == '__main__':
    string = "Alexander the Great was a successful ruler because his actions created long lasting effects on cultures that continue to the present day. One example of his legacy was the creation of a Hellenistic society. Hellenism was the combination of Greek, Persian, and Egyptian cultures. During this remarkable time period, people were encouraged to pursue a formal education and produce many different kinds of art. New forms of math, science, and design made a great impact on society."
    string = string.replace(" ", "")
    string = string.replace(".", "")
    string = string.replace(",", "")
    string = string.lower()

    print("Make sure a is a co-prime of 26!!!")
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    cipher_text = affineCipherEncrypt(string, a, b)
    print(f"Your cipher text: {cipher_text}")
    print(f"Your plain text: {string}")

    dict = frequencyAnalysis(cipher_text)
    dicts = frequencyAnalysis(string)
    print(f"Frequency of letters in cipher text {dict}")
    print(f"Frequency of letters in plain text {dicts}")

    IOCCipher = IndexOfCoincidence(cipher_text, dict)
    IOCPlain = IndexOfCoincidence(string, dicts)
    print(f"Index of coincidence for cipher text {IOCCipher}")
    print(f"Index of coincidence for plain text {IOCPlain}")
