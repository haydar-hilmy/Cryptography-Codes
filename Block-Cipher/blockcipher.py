import random
import string
from terminal_modif import Color
from converter import Converter

class ECB:
    # INISIALISASI CONVERTER
    def __init__(self):
       self.conv = Converter

    def generate_key(self, type_key, len_plain):
        key = ''
        if type_key == "1": # jika memilih char
            get_characters = string.ascii_letters + string.digits # get char A-z 0-9
            random_chars = random.choices(get_characters, k=len_plain) # get random char
            key = ''.join(random_chars)
        elif type_key == "2": # jika memilih biner
            binary_list = ['1', '0']
            i = 0
            while i < len_plain:
                key += random.choice(binary_list)
                i += 1
        elif type_key == "3": # jika memilih hexa
            random_int = random.getrandbits(len_plain * 4)
            hex_string = hex(random_int)[2:]  # Menghilangkan awalan '0x'
            key = hex_string.zfill(len_plain)
        return key


    def make_key(self, chs, plain_len):
        isLoop = True
        key = ''
        while isLoop:
            print('-- Create Key --')
            print('1. Shuffle')
            print('2. Input Key')
            chs_key = input('choose [1/2]: ')
            if chs_key == '1':
                key = self.generate_key(chs, plain_len)
                isLoop = False
            elif chs_key == '2':
                if chs == "1":
                    key = input("Key (char): ")
                    isLoop = False
                elif chs == "2":
                    key = input("Key (biner): ")
                    isLoop = False
                elif chs == "3":
                    key = input("Key (hexa): ")
                    isLoop = False
                else:
                    isLoop = False
                    return ''
                key = Converter.key_same_plain(key, plain_len)
            else:
                isLoop = True
                Color.Color.clear_terminal()
        return key





    def encryption(self): # Self untuk menginisialisasikan def lain
        isLoop = True

        while isLoop:
            arr_plain = []
            arr_key = []
            arr_xor = []
            print(Color.GREEN + 'Choosed Encryption' + Color.RESET)
            print("-- Input Plaintext/Key Use --")
            print("1. Character")
            print("2. Binary")
            print("3. Hexa Decimal")
            print("4. (Cancel)")
            choose_type = input("Choose: ")
            if choose_type == "1":
                Color.clear_terminal()

                print(Color.GREEN + 'Encryption' + Color.RESET)
                print('Input Use' +  Color.YELLOW + ' Character' + Color.RESET)
                plaintext = input("Plaintext (char): ")
                key = self.make_key("1", len(plaintext))
                arr_plain = Converter.conv_char_to_biner(plaintext)
                arr_key = Converter.conv_char_to_biner(key)
                arr_plain_4bit = Converter.conv_8bit_to_4bit(arr_plain)
                arr_key_4bit = Converter.conv_8bit_to_4bit(arr_key)
                arr_xor = Converter.xor_binary_array(arr_key_4bit, arr_plain_4bit)

                Color.clear_terminal()
                print(Color.GREEN + '== RESULT ==' + Color.RESET)
                print(f'Plaintext (char): {plaintext}')
                print(f'Key (char): {key}')

                print(f'\nPlaintext (biner 8bit): {arr_plain}')
                print(f'Key (biner 8bit): {arr_key}')
                print(f'Key (hexa): {Converter.conv_biner_to_hex(Converter.conv_8bit_to_4bit(arr_key))}')

                print(f'\nPlaintext biner 4bit: {arr_plain_4bit}')
                print(f'Key biner 4bit: {arr_key_4bit}')
                print(f'(P XOR iv) XOR K -> Wrapping: {arr_xor}') 

                print(f'\nCiphertext (biner 8bit): {Converter.conv_biner_to_8bit(arr_xor)}')
                print(f'Ciphertext (hex): {Converter.conv_biner_to_hex(arr_xor)}')
                print(f'Ciphertext (char): {Converter.conv_biner_to_char(Converter.conv_biner_to_8bit(arr_xor))}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    Color.clear_terminal()
                else:
                    isLoop = True
                    Color.clear_terminal()

            elif choose_type == "2":
                Color.clear_terminal()

                print(Color.GREEN + 'Encryption' + Color.RESET)
                print('Input Use' + Color.YELLOW + ' Binary' + Color.RESET)
                plaintext = input("Plaintext (biner): ")
                key = self.make_key("2", len(plaintext))
                arr_plain = Converter.to_8bit_biner(plaintext) # masih dalam bentuk string dan diubah ke dalam biner 8 bit
                arr_key = Converter.to_8bit_biner(key)
                arr_plain_4bit = Converter.conv_8bit_to_4bit(arr_plain)
                arr_key_4bit = Converter.conv_8bit_to_4bit(arr_key)
                arr_xor = Converter.xor_binary_array(arr_key_4bit, arr_plain_4bit)

                # Color.clear_terminal()
                print(Color.GREEN + '== RESULT ==' + Color.RESET)
                print(f'Plaintext (biner 8bit): {arr_plain}')
                print(f'Key (biner 8bit): {arr_key}')

                print(f'\nPlaintext (biner 4bit): {arr_plain_4bit}')
                print(f'Key (biner 4bit): {arr_key_4bit}')
                print(f'(P XOR iv) XOR K -> Wrapping: {arr_xor}')

                print(f'\nCiphertext (biner 8bit): {Converter.conv_biner_to_8bit(arr_xor)}')
                print(f'Ciphertext (hex): {Converter.conv_biner_to_hex(arr_xor)}')
                print(f'Ciphertext (char): {Converter.conv_biner_to_char(Converter.conv_biner_to_8bit(arr_xor))}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    Color.clear_terminal()
                else:
                    isLoop = True
                    Color.clear_terminal()

            elif choose_type == "3":
                Color.clear_terminal()

                print(Color.GREEN + 'Encryption' + Color.RESET)
                print('Input Use' + Color.YELLOW + ' HexaDecimal' + Color.RESET)
                plaintext = input("Plaintext (hexa): ")
                arr_plain = Converter.conv_hex_to_biner(plaintext)
                key = self.make_key("3", len(arr_plain))
                arr_key = Converter.conv_hex_to_biner(key)

                arr_key_8bit = Converter.conv_biner_to_8bit(arr_key)
                arr_plain_8bit = Converter.conv_biner_to_8bit(arr_plain)
                arr_xor = Converter.xor_binary_array(arr_key, arr_plain)
                
                Color.clear_terminal()
                print(Color.GREEN + '== RESULT ==' + Color.RESET)
                print(f'Plaintext (hex): {Converter.conv_biner_to_hex(arr_plain)}')
                print(f'Key (biner 4bit): {Converter.conv_biner_to_hex(arr_key)}')

                print(f'\nPlaintext (biner 4bit): {arr_plain}')
                print(f'Key (biner 4bit): {arr_key}')
                print(f'(P XOR iv) XOR K -> Wrapping: {arr_xor}')

                print(f'\nCiphertext (biner 8bit): {Converter.conv_biner_to_8bit(arr_xor)}')
                print(f'Ciphertext (hex): {Converter.conv_biner_to_hex(arr_xor)}')
                print(f'Ciphertext (char): {Converter.conv_biner_to_char(Converter.conv_biner_to_8bit(arr_xor))}')
                

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    Color.clear_terminal()
                else:
                    isLoop = True
                    Color.clear_terminal()

            elif choose_type == "4":
                isLoop = False
                Color.clear_terminal()
            else:
                Color.clear_terminal()
                





    def decryption(self):
        isLoop = True

        while isLoop:
            arr_plain = []
            arr_key = []
            arr_xor = []
            print(Color.BLUE + 'Choosed Decryption' + Color.RESET)
            print("-- Input Ciphertext/Key Use --")
            print("1. Character")
            print("2. Binary")
            print("3. Hexa Decimal")
            print("4. (Cancel)")
            choose_type = input("Choose: ")

            if choose_type == "1":
                Color.clear_terminal()

                print(Color.GREEN + 'Decryption' + Color.RESET)
                print('Input Use' +  Color.YELLOW + ' Character' + Color.RESET)
                ciphertext = input("Ciphertext (char): ")
                key = self.make_key("1", len(ciphertext))

                # PROSES KONVERSI
                arr_cipher = Converter.conv_char_to_biner(ciphertext) # konversi char ke biner 8 bit
                arr_cipher_4bit = Converter.conv_8bit_to_4bit(arr_cipher) # konversi biner 8bit ke 4bit
                arr_key = Converter.conv_char_to_biner(key)
                arr_key_4bit = Converter.conv_8bit_to_4bit(arr_key)
                arr_iv_4bit = Converter.get_iv_from_cipher(arr_cipher_4bit)
                arr_xor = Converter.xor_binary_array_decrypt(arr_key_4bit, arr_iv_4bit, arr_cipher_4bit)

                Color.clear_terminal()
                print(Color.BLUE + '== RESULT ==' + Color.RESET)
                print(f'Ciphertext (char): {ciphertext}')
                print(f'Key (char): {key}')
                
                print(f'\nCiphertext (biner 4bit): {arr_cipher_4bit}')
                print(f'Key (biner 4bit): {arr_key_4bit}')
                print(f'IV (biner 4bit): {arr_iv_4bit}')

                print(f'\nUnwrapping Ciphertext -> Ciphertext XOR Key XOR IV: {arr_xor}')
                print(f'\nPlaintext (biner 8bit): {Converter.conv_biner_to_8bit(arr_xor)}')
                print(f'Plaintext (hex): {Converter.conv_biner_to_hex(arr_xor)}')
                print(f'Plaintext (char): {Converter.conv_biner_to_char(Converter.conv_biner_to_8bit(arr_xor))}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    Color.clear_terminal()
                else:
                    isLoop = True
                    Color.clear_terminal()

            elif choose_type == "2":
                Color.clear_terminal()

                print(Color.GREEN + 'Decryption' + Color.RESET)
                print('Input Use' +  Color.YELLOW + ' Binary' + Color.RESET)
                ciphertext = input("Ciphertext (biner): ")
                key = self.make_key("2", len(ciphertext))

                # PROSES KONVERSI
                arr_cipher = Converter.to_8bit_biner(ciphertext)
                arr_cipher_4bit = Converter.conv_8bit_to_4bit(arr_cipher)
                arr_key = Converter.to_8bit_biner(key)
                arr_key_4bit = Converter.conv_8bit_to_4bit(arr_key)
                arr_iv_4bit = Converter.get_iv_from_cipher(arr_cipher_4bit)
                arr_xor = Converter.xor_binary_array_decrypt(arr_key_4bit, arr_iv_4bit, arr_cipher_4bit)

                Color.clear_terminal()
                print(Color.BLUE + '== RESULT ==' + Color.RESET)
                print(f"Ciphertext (biner): {arr_cipher}")
                print(f"Key (biner): {arr_key}")

                print(f'\nCiphertext (biner 4bit): {arr_cipher_4bit}')
                print(f"Key (biner 4bit): {arr_key_4bit}")
                print(f"IV (biner 4bit): {arr_iv_4bit}")

                print(f'\nUnwrapping Ciphertext -> Ciphertext XOR Key XOR IV: {arr_xor}')
                print(f'\nPlaintext (biner 8bit): {Converter.conv_biner_to_8bit(arr_xor)}')
                print(f'Plaintext (Hex): {Converter.conv_biner_to_hex(arr_xor)}')
                print(f'Plaintext (Char): {Converter.conv_biner_to_char(Converter.conv_biner_to_8bit(arr_xor))}')


                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    Color.clear_terminal()
                else:
                    isLoop = True
                    Color.clear_terminal()


            elif choose_type == "3":
                Color.clear_terminal()

                print(Color.GREEN + 'Decryption' + Color.RESET)
                print('Input Use' +  Color.YELLOW + ' Hexadecimal' + Color.RESET)
                ciphertext = input("Ciphertext (hexa): ")
                arr_cipher = Converter.conv_hex_to_biner(ciphertext)
                arr_cipher_4bit = arr_cipher
                key = self.make_key("3", len(arr_cipher))
                arr_key = Converter.conv_hex_to_biner(key)
                arr_key_4bit = arr_key
                arr_iv_4bit = Converter.get_iv_from_cipher(arr_cipher_4bit)
                arr_xor = Converter.xor_binary_array_decrypt(arr_key_4bit, arr_iv_4bit, arr_cipher_4bit)

                Color.clear_terminal()
                print(Color.GREEN + '== RESULT ==' + Color.RESET)
                print(f'Ciphertext (hex): {arr_cipher}')
                print(f'Key (hex): {arr_key}')

                print(f'\nCiphertext (biner 4bit): {arr_cipher_4bit}')
                print(f'Key (biner 4bit): {arr_key_4bit}')
                print(f'IV (biner 4bit): {arr_iv_4bit}')

                print(f'\nUnwrapping Ciphertext -> Ciphertext XOR Key XOR IV: {arr_xor}')
                print(f'\nPlaintext (biner 8bit): {Converter.conv_biner_to_8bit(arr_xor)}')
                print(f'Plaintext (Hex): {Converter.conv_biner_to_hex(arr_xor)}')
                print(f'Plaintext (Char): {Converter.conv_biner_to_char(Converter.conv_biner_to_8bit(arr_xor))}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    Color.clear_terminal()
                else:
                    isLoop = True
                    Color.clear_terminal()

            elif choose_type == "4":
                isLoop = False
                Color.clear_terminal()
            else:
                Color.clear_terminal()