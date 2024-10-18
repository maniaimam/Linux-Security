import tkinter as tk
from tkinter import simpledialog
from itertools import starmap, cycle

title = "OS Encryption and Decryption Manager"

def main():
    root = tk.Tk()
    root.withdraw()

    msg1 = "Welcome, please pick a cryptosystem (Encryption, Decryption)."
    crypto_choices = ["Encryption", "Decryption"]
    crypto_mode = simpledialog.askstring(title, msg1, initialvalue=crypto_choices[0])

    msg2 = "Please pick a crypto mode to use (Affine Cipher, Vigenere Cipher)."
    cryptosystem_choices = ["Affine Cipher", "Vigenere Cipher"]
    cryptosystem_mode = simpledialog.askstring(title, msg2, initialvalue=cryptosystem_choices[0])

    msg3 = "Would you like plaintext or cipher text?"
    text_choices = ["Plaintext", "Cipher text"]
    text_mode = simpledialog.askstring(title, msg3, initialvalue=text_choices[0])

    msg4 = "Please enter your text and key."

    if cryptosystem_mode == 'Affine Cipher':
        field_names = ["Text", "A", "B"]
    elif cryptosystem_mode == 'Vigenere Cipher':
        field_names = ["Text", "Key"]

    field_values = [simpledialog.askstring(title, f"Enter {field}", initialvalue="") for field in field_names]

    # make sure that none of the fields was left blank
    while 1:
        if field_values is None:
            break
        errmsg = ""
        for i in range(len(field_names)):
            if field_values[i].strip() == "":
                errmsg = errmsg + ('"%s" is a required field.\n\n' % field_names[i])
        if errmsg == "":
            break  # no problems found
        field_values = [simpledialog.askstring(title, f"Enter {field}", initialvalue=field_values[i]) for i, field in enumerate(field_names)]

    my_text = field_values[0]

    if cryptosystem_mode == 'Affine Cipher':
        a = field_values[1]
        b = field_values[2]
        print("[Affine Cipher]")
        print('%s message' % (crypto_mode.title()))
        print(affine_cipher(a, b, my_text, crypto_mode, text_mode))

    elif cryptosystem_mode == 'Vigenere Cipher':
        my_key = field_values[1]
        print("[Vigenere Cipher]")
        print('%s message' % (crypto_mode.title()))
        print(vigenere_cipher(my_key, my_text, crypto_mode, text_mode))

    root.mainloop()

def vigenere_cipher(passed_key, msg, crypto, text_type):
    text = msg
    key = passed_key

    def encrypt(message, key):
        message = filter(str.isalpha, message.upper())

        def enc(c, k):
            return chr(((ord(k) + ord(c) - 2 * ord('A')) % 26) + ord('A'))
        return ''.join(starmap(enc, zip(message, cycle(key))))

    def decrypt(message, key):

        def dec(c, k):
            return chr(((ord(c) - ord(k) - 2 * ord('A')) % 26) + ord('A'))
        return ''.join(starmap(dec, zip(message, cycle(key))))

    encr = encrypt(text, key)
    decr = decrypt(encr, key)

    if crypto == 'Encryption' and text_type == 'Plaintext':
        return 'Original: ' + text + '\nEncrypted: ' + encr
    elif crypto == 'Decryption' and text_type == 'Cipher text':
        return 'Original: ' + text + '\nDecrypted: ' + decr
    else:
        return 'Please select the proper text type.'

def affine_cipher(a, b, msg, crypto, text_type):
    text = msg
    KEY = (int(a), int(b), 55)
    DIE = 128

    def encrypt_char(char):
        K1, K2, kI = KEY
        return chr((K1 * ord(char) + K2) % DIE)

    def encrypt(string):
        return "".join(map(encrypt_char, string))

    def decrypt_char(char):
        K1, K2, KI = KEY
        return chr(KI * (ord(char) - K2) % DIE)

    def decrypt(string):
        return "".join(map(decrypt_char, string))

    encr = encrypt(text)
    decr = decrypt(text)

    if crypto == 'Encryption' and text_type == 'Plaintext':
        return 'Original: ' + text + '\nEncrypted: ' + encr
    elif crypto == 'Decryption' and text_type == 'Cipher text':
        return 'Original: ' + text + '\nDecrypted: ' + decr
    else:
        return 'Please select the proper text type.'

if __name__ == '__main__':
    main()
