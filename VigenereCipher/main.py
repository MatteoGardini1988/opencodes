import vigenercipher1 as VC

if __name__ == '__main__':

    testo = "I am Matteo Gardini and this is a Vigenere Cipher"

    # Create the object
    cipher = VC.VigenereCipher(testo)

    # testo = "Ciao, così così."
    # cipher = VC.VigenereCipher(testo, 'LATIN_EXTENDED')

    # Choose an encripting key
    key_val = "LEMON"

    # set the key
    cipher.key = key_val

    cipher.encriptmsg()

    msg_def = cipher.decipher()

    print(testo)
    print(cipher.cripedmsg)
    print(msg_def)

