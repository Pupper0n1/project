import sys
import random

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
cipher_list = []

while True:
    setting = input('Would you like to encrypt to decrypt? ')
    if 'en' in setting.lower(): # Encryption path
        ans = input("Would you like to generate a random key? ")
        if 'y' in ans.lower():
            random.shuffle(alphabet) # Random encryption key generator
            for i in alphabet:
                cipher_list.append(i)
            for i in range(2):
                print('')
            print("Encryption key is: ")
            print('==========================')
            for i in cipher_list:
                print(i, end='')
            print('')
            print('==========================')
            for i in range(2):
                print('')
        else:
            while True: # Custom encryption key input
                cipher_input = input('Input cipher_list: ')

                if len(cipher_input) != 26:
                    continue

                for i in cipher_input:
                    if i.upper() not in cipher_list:
                        cipher_list.append(i.upper()) 
                    else:
                        continue

                if len(cipher_list) == 26:
                    break
        text = input('Type some text: ')
        print('')
        print('----------------------------------------')
        for i in range(len(text)): 
            if text[i].isupper() == True and text[i].isalpha() == True:
                temp = ord(text[i]) - 65
                print(cipher_list[temp], end='')

            elif text[i].islower() == True and text[i].isalpha() == True:
                temp = ord(text[i]) - 97
                print(cipher_list[temp].lower(), end='')

            else:
                print(text[i], end='')
        print('')
        print('----------------------------------------')
        print('')
        sys.exit(0)

    elif 'de' in setting.lower(): # Decryption path
        while True:
            cipher_input = input('Input cipher key: ')

            if len(cipher_input) != 26:
                continue

            for i in cipher_input:
                if i.upper() in cipher_list or i.isalpha() == False:
                    continue
                else:
                    cipher_list.append(i.upper())

            if len(cipher_list) == 26:
                break
        print('')
        text = input("Type message to decode: ")
        print('')
        print('----------------------------------------')
        for i in range(len(text)):
            if text[i].isalpha() == True and text[i].isupper() == True:
                buffer = ord(text[i]) - 65

                for j in range(len(cipher_list)):
                    if text[i] == cipher_list[j]:
                        break
                print(alphabet[j], end='')

            elif text[i].isalpha() == True and text[i].islower() == True:
                buffer = ord(text[i]) - 97

                for j in range(len(cipher_list)):
                    if text[i].upper() == cipher_list[j]:
                        break
                print(alphabet[j].lower(), end='')

            else:
                print(text[i], end='')
        print('')
        print('----------------------------------------')
        print('')
        sys.exit(0)
