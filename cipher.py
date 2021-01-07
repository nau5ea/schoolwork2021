# -*- coding: utf-8 -*-
"""
Author username(s): moenchlm, thottans
Date: 10/13/2020
Assignment/problem number: P8
Assignment/problem title: Caesar Cipher
"""

def encipher(text, key, encoded):
    """
    

    Parameters
    ----------
    text : string
        The encrypted or ununcrypted version of the string 
        you want to en/decrypt.
    key : string
        The key which we will use to encrypt text.
    encoded : boolean
        Tells whether text is encrypted or unencrypted.

    Returns
    -------
    out : string
        The encrypted or decrypted version of text.

    """
    out = ''
    if encoded == 'e':
        for letter in text:
            if ord(letter) < 123 and ord(letter) > 96:
                out += chr((((ord(key[text.index(letter) % len(key)]) - 96) + 
                             (ord(letter) - 96)) % 26) + 96)
            elif ord(letter) < 91 and ord(letter) > 64:
                out += chr((((ord(key[text.index(letter) % len(key)]) - 96) + 
                             (ord(letter.lower()) - 96)) % 26) + 96)
            else:
                out += letter
    else:
        for letter in text:
            if ord(letter) < 123 and ord(letter) > 96:
                if letter == key[text.index(letter) % len(key)]:
                    out += chr(((ord(letter) - ord(key[text.index(letter) % 
                                                       len(key)])) % 26) + 97)
                else:
                    out += chr(((ord(letter) - ord(key[text.index(letter) % 
                                                       len(key)])) % 26) + 96)
            elif ord(letter) < 91 and ord(letter) > 64:
                if letter.lower() == key[text.index(letter) % len(key)]:
                    out += chr(((ord(letter.lower()) - 
                                 ord(key[text.index(letter) % len(key)])) % 26)
                               + 97)
                else:
                    out += chr((((ord(letter.lower()) - 96)) % 26) - 
                               ((ord(key[text.index(letter) % len(key)]) - 96)
                                + 96))
            else:
                out += letter
    return out

def main():
    """
    Asks the user if they want to encode or decode. Allow the user to specify
    this with either e or d as input.
    Asks the user for the name of the text file that contains the message.
    Asks the user for the key. 
    Reads the contents of the file named by the user.
    Calls the encipher function, passing the appropriate parameters, and print
    out the encoded or decoded message.
    """
    encoded = input("""Would you like to encode a string or decode a string? 
                    (Please type "e" to encode a string and "d" to
                     decode one.)
                    """)
    text = input("What string (text file) would you like to encode? ")
    key = input("What is the key with which you wish to encode your string? ")
    print(encipher(text, key, encoded))