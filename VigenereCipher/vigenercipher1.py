import constants as c

class VigenereCipher:



    def __init__(self, msg, alphabeth="LATIN"):

        # Choose the alphabeth
        assert alphabeth in c.ALPHABETHS.keys(), f"The alphabeth ',{alphabeth},' does not exists."

        chosen_alphabeth = c.ALPHABETHS[alphabeth]

        # Inizialize the message to cipher
        check_msg = msg.replace(" ", "")
        assert self.only_admissible_letters(check_msg, chosen_alphabeth), 'You have entered an invalid message. You have to use only letter from latin alphabeth'

        self.msg = msg
        self.__key = "" # This is a private content
        self.vigmatrix = self.create_vig_cipher_matrix(chosen_alphabeth)
        self.cripedmsg = ""
        self.was_upper = [x.isupper() for x in self.msg]

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, key_val):
        if self.only_admissible_letters(key_val, alphabeth="Latin"):
            raise Exception("The key must contains values only from the alphabeth")
        elif key_val.islower():
            raise Exception("The key must be in Italics")
        else:
            self.__key = key_val

    @staticmethod
    def only_admissible_letters(text, alphabeth):
        # Check if a text contains only latin-letters
        # text is a string
        # alphabeth is a list containining symbols of an alphabeth

        # Turn my set is upper case
        text = text.upper()

        # Turn the alphabeth into a set
        myalphabeth = set(alphabeth)

        mytext = set(text)

        return mytext.issubset(myalphabeth)

    @staticmethod
    def create_vig_cipher_matrix(alphabeth):
        # Create the vigenere matrix from a given alphabeth
        n = len(alphabeth)

        vig_cipher = [None]*n

        for i in range(n):
            vig_cipher[i] = alphabeth[i:] + alphabeth[0:i]

        return vig_cipher

    def encriptmsg(self):
        n = len(self.msg)
        msg_to_encript = self.msg.upper()
        nkey = len(self.__key)



        d = self.vigmatrix[0] # This is my dictionary

        j = 0 # This is needed to run over the ciphring string
        for i in range(n):
            if msg_to_encript[i] == ' ':
                ciphred = ' '
            else:
                val2cip = msg_to_encript[i]
                p = j % nkey
                j += 1

                col = d.index(val2cip)
                row = d.index(self.__key[p])
                ciphred = self.vigmatrix[row][col]

            self.cripedmsg += ciphred

    def decipher(self):
        n = len(self.msg)
        nkey = len(self.__key)
        d = self.vigmatrix[0] # This is my dictionary
        decripted_msg = ""

        j = 0

        for i in range(n):
            if self.cripedmsg[i] == ' ':
                # if there is an empty space you don't have anything to cipher
                deciphred = ' '
            else:
                val2dec = self.cripedmsg[i]
                # get the current position of the crypto string
                p = j % nkey
                j += 1

                row = d.index(self.__key[p])
                col = self.vigmatrix[row].index(val2dec.upper())
                deciphred = self.vigmatrix[0][col]

            # Restyle: this respect the input upper/lower case
            if not self.was_upper[i]:
                deciphred = deciphred.lower()

            decripted_msg += deciphred

        return decripted_msg



