import random
import os
import string
from color import Color
from converter import Converter

def clear_terminal():
    os_name = os.name
    if os_name == 'posix':  # Unix/Linux/MacOS
        os.system('clear')
    elif os_name == 'nt':  # Windows
        os.system('cls')
    else:
        print("\nNo OS suitable\n")

class StreamCipher:

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
                clear_terminal()
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
                clear_terminal()

                print(Color.GREEN + 'Encryption' + Color.RESET)
                print('Input Use' +  Color.YELLOW + ' Character' + Color.RESET)
                plaintext = input("Plaintext (char): ")
                key = self.make_key("1", len(plaintext))
                arr_plain = Converter.conv_char_to_biner(plaintext)
                arr_key = Converter.conv_char_to_biner(key)
                arr_xor = Converter.xor_binary_array(arr_key, arr_plain)

                clear_terminal()
                print(Color.GREEN + '== RESULT ==' + Color.RESET)
                print(f'Plaintext Biner: {arr_plain}')
                print(f'Key Biner: {arr_key}')
                print(f'P (XOR) K : {arr_xor}')
                print(f'Plaintext Char: {plaintext}')
                print(f'Key Char: {key}')
                print(f'Ciphertext Char: {Converter.conv_biner_to_char(arr_xor)}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    clear_terminal()
                else:
                    isLoop = True
                    clear_terminal()

            elif choose_type == "2":
                clear_terminal()

                print(Color.GREEN + 'Encryption' + Color.RESET)
                print('Input Use' + Color.YELLOW + ' Binary' + Color.RESET)
                plaintext = input("Plaintext (biner): ")
                key = self.make_key("2", len(plaintext))
                arr_plain = Converter.to_8bit_biner(plaintext) # masih dalam bentuk string dan diubah ke dalam biner 8 bit
                arr_key = Converter.to_8bit_biner(key)
                arr_xor = Converter.xor_binary_array(arr_key, arr_plain)

                clear_terminal()
                print(Color.GREEN + '== RESULT ==' + Color.RESET)
                print(f'Plaintext Biner: {arr_plain}')
                print(f'Key Biner: {arr_key}')
                print(f'P (XOR) K : {arr_xor}')
                print(f'Plaintext Char: {Converter.conv_biner_to_char(arr_plain)}')
                print(f'Key Char: {Converter.conv_biner_to_char(arr_key)}')
                print(f'Ciphertext Char: {Converter.conv_biner_to_char(arr_xor)}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    clear_terminal()
                else:
                    isLoop = True
                    clear_terminal()

            elif choose_type == "3":
                clear_terminal()

                print(Color.GREEN + 'Encryption' + Color.RESET)
                print('Input Use' + Color.YELLOW + ' HexaDecimal' + Color.RESET)
                plaintext = input("Plaintext (hexa): ")
                arr_plain = Converter.conv_hex_to_biner(plaintext)
                key = self.make_key("3", len(arr_plain))
                arr_key = Converter.conv_hex_to_biner(key)

                arr_key_8bit = Converter.conv_biner_to_8bit(arr_key)
                arr_plain_8bit = Converter.conv_biner_to_8bit(arr_plain)
                arr_xor = Converter.xor_binary_array(arr_key_8bit, arr_plain_8bit)
                
                clear_terminal()
                print(Color.GREEN + '== RESULT ==' + Color.RESET)
                print(f'Plaintext Biner: {arr_plain_8bit}')
                print(f'Key Biner: {arr_key_8bit}')
                print(f'P (XOR) K : {arr_xor}')

                print(f'\nPlaintext hex: {plaintext}')
                print(f'Key hex: {key}')
                print(f'Ciphertext hex: {Converter.conv_biner_to_hex(arr_xor)}')

                print(f'\nPlaintext Char: {Converter.conv_biner_to_char(arr_plain_8bit)}')
                print(f'Key Char: {Converter.conv_biner_to_char(arr_key_8bit)}')
                print(f'Ciphertext Char: {Converter.conv_biner_to_char(arr_xor)}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    clear_terminal()
                else:
                    isLoop = True
                    clear_terminal()

            elif choose_type == "4":
                isLoop = False
                clear_terminal()
            else:
                clear_terminal()
                
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
                clear_terminal()

                print(Color.GREEN + 'Decryption' + Color.RESET)
                print('Input Use' +  Color.YELLOW + ' Character' + Color.RESET)
                ciphertext = input("Ciphertext (char): ")
                key = self.make_key("1", len(ciphertext))
                arr_cipher = Converter.conv_char_to_biner(ciphertext)
                arr_key = Converter.conv_char_to_biner(key)
                arr_xor = Converter.xor_binary_array(arr_key, arr_cipher)

                clear_terminal()
                print(Color.BLUE + '== RESULT ==' + Color.RESET)
                print(f'Ciphertext Biner: {arr_cipher}')
                print(f'Key Biner: {arr_key}')
                print(f'C (XOR) K : {arr_xor}')
                print(f'Ciphertext Char: {ciphertext}')
                print(f'Key Char: {key}')
                print(f'Plaintext Char: {Converter.conv_biner_to_char(arr_xor)}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    clear_terminal()
                else:
                    isLoop = True
                    clear_terminal()

            elif choose_type == "2":
                clear_terminal()

                print(Color.GREEN + 'Decryption' + Color.RESET)
                print('Input Use' +  Color.YELLOW + ' Binary' + Color.RESET)
                ciphertext = input("Ciphertext (biner): ")
                key = self.make_key("2", len(ciphertext))
                arr_cipher = Converter.to_8bit_biner(ciphertext)
                arr_key = Converter.to_8bit_biner(key)
                arr_xor = Converter.xor_binary_array(arr_key, arr_cipher)

                clear_terminal()
                print(Color.BLUE + '== RESULT ==' + Color.RESET)
                print(f'Ciphertext Biner: {arr_cipher}')
                print(f'Key Biner: {arr_key}')
                print(f'C (XOR) K : {arr_xor}')
                print(f'Ciphertext Char: {Converter.conv_biner_to_char(arr_cipher)}')
                print(f'Key Char: {Converter.conv_biner_to_char(arr_key)}')
                print(f'Plaintext Char: {Converter.conv_biner_to_char(arr_xor)}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    clear_terminal()
                else:
                    isLoop = True
                    clear_terminal()


            elif choose_type == "3":
                clear_terminal()

                print(Color.GREEN + 'Decryption' + Color.RESET)
                print('Input Use' +  Color.YELLOW + ' Hexadecimal' + Color.RESET)
                ciphertext = input("Ciphertext (hexa): ")
                arr_plain = Converter.conv_hex_to_biner(ciphertext)
                key = self.make_key("3", len(arr_plain))
                arr_key = Converter.conv_hex_to_biner(key)

                arr_key_8bit = Converter.conv_biner_to_8bit(arr_key)
                arr_cipher_8bit = Converter.conv_biner_to_8bit(arr_plain)
                arr_xor = Converter.xor_binary_array(arr_key_8bit, arr_cipher_8bit)

                clear_terminal()
                print(Color.GREEN + '== RESULT ==' + Color.RESET)
                print(f'Ciphertext Biner: {arr_cipher_8bit}')
                print(f'Key Biner: {arr_key_8bit}')
                print(f'C (XOR) K : {arr_xor}')

                print(f'\nCiphertext hex: {ciphertext}')
                print(f'Key hex: {key}')
                print(f'Plaintext hex: {Converter.conv_biner_to_hex(arr_xor)}')

                print(f'\nCiphertext Char: {Converter.conv_biner_to_char(arr_cipher_8bit)}')
                print(f'Key Char: {Converter.conv_biner_to_char(arr_key_8bit)}')
                print(f'Plaintext Char: {Converter.conv_biner_to_char(arr_xor)}')

                try_again = input("\ntry again? [y/n]: ")
                if try_again == "n":
                    isLoop = False
                    clear_terminal()
                else:
                    isLoop = True
                    clear_terminal()

            elif choose_type == "4":
                isLoop = False  
                clear_terminal()
            else:
                clear_terminal()





    

isLoop = True

stream_cipher = StreamCipher()

while isLoop:
  print('--- STREAM CIPHER ---')
  print('1. Encryption')
  print('2. Decryption')
  print('3. Exit')
  choose = input('choose [1/2/3]: ')

  if choose == "1":
    clear_terminal()
    stream_cipher.encryption()
  elif choose == "2":
    clear_terminal()
    stream_cipher.decryption()
  elif choose == "3":
    isLoop = False
    clear_terminal()
    print(Color.CYAN + '\n=== Thank You ===' + Color.RESET)
  else:
    clear_terminal()
    print('\nNo Suitable Input\n')

