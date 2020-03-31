import operator
import math


def freqAnalysis(data):
    result = {}
    for keys in data:
        result[keys] = result.get(keys, 0) + 1
    result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    return result


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


def LRT(input_text):
    alphabet_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                'u', 'v', 'w', 'x', 'y', 'z']

    alpha_length = len(alphabet_list)
    input_text_length = len(input_text)

    alphabet_frequency_table = [.082, .015, .028, .043, .127, .022, .020,
                          .061, .070, .002, .008, .040, .024, .067,
                          .075, .019, .001, .060, .063, .091, .028,
                          .010, .023, .001, .020, .001]
    list_of_zeros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for i in range(alpha_length):
        for j in range(input_text_length):
            if alphabet_list[i] == input_text[j]:
                list_of_zeros[i] += 1.0

    lrt = 0.0
    pNoise = 1.0 / 26.0

    length_of_zero_list = len(list_of_zeros)

    for x in range(length_of_zero_list):
        frequency = (list_of_zeros[x] / input_text_length)
        lrt += (frequency * math.log(alphabet_frequency_table[x] / pNoise))

    return round(lrt, 4)






if __name__ == '__main__':
    cipher_text = "gyznkjgeycktzheznkkburazoutulroqkotzurubkcgygiikrkxgzkjcnozklgtmnosykrlhkmgtzumxucgcgxkulozznuamnotnoyiutyiouaytkyynkqtkctuzcngzrubkcgyozsgtolkyzkjozykrlzunosgygbuojotnoyhkotmgnatmxeginotmekgxtotmbuojzngzirgsuaxkjzuhklorrkjozcgygvgotgtjgtatxkyzgtjozxkikobkjkgyksktzutreheznkzuainulznktkcmujoyvxkyktikgzyainzoskyrubkcgypuezunosgcorjqkktznxorrotmygzoylgizouthazcnktgcgelxusnoymujznkvgotgtjznkatxkyzxkzaxtkjznkbuojotnosyvxgtmavgtjvxkyykjgmgotyznoscoznozyksvzotkyygtjznknatmkxmtgckjgtjmtgckjatikgyotmre"
    freq = freqAnalysis(cipher_text)
    print(freq)


    # Iterating over different shifts and testing them in the LRT Test
    # if LRT Test returns a positive number then print out the plain text and the shift
    i = 0
    while i < 26:
        plain_text = shiftCipherDecrypt(cipher_text, i)
        lrt = LRT(plain_text)
        if lrt >= 0.0:
            print(plain_text)
            print(lrt)
            print(f"Shift is {i}")
        i += 1


