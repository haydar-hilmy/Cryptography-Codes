import random
import string
from terminal_modif import Color

class Playfair:

    def get_coordinate(self, a_k, a_p):
        arr_key = a_k
        arr_plain = ''.join(''.join(sub_arr) for sub_arr in a_p)
        arr_plain = list(arr_plain)

        # arr_coor = [[[] for _ in range(len(arr_plain[0]))] for _ in range(len(arr_plain))]
        arr_coor = []

        for chr_p in arr_plain:
            for row in range(len(arr_key)):
                for col in range(len(arr_key[row])):
                    if chr_p == arr_key[row][col]:
                        arr_coor.append([row, col])
                        continue
        
        new_arr_coor = [arr_coor[i:i+2] for i in range(0, len(arr_coor), 2)] # [[], [], [], []] -> [[[], []], [[], []]]

        return new_arr_coor
    
    def mapping(self, a_c, get_type):
        arr_coor = a_c

        arr = []
        if get_type == "1": # enkripsi
            for sub_arr in arr_coor: # [[_, _], [_, _]]
                if sub_arr[0][0] != sub_arr[1][0] and sub_arr[0][1] != sub_arr[1][1]:
                    arr.append([[sub_arr[0][0], sub_arr[1][1]], [sub_arr[1][0], sub_arr[0][1]]])
                elif sub_arr[0][0] == sub_arr[1][0]:
                    arr.append([[sub_arr[0][0], sub_arr[0][1] + 1], [sub_arr[1][0], sub_arr[1][1] + 1]])
                elif sub_arr[0][1] == sub_arr[1][1]:
                    arr.append([[sub_arr[0][0] + 1, sub_arr[0][1]], [sub_arr[1][0] + 1, sub_arr[1][1]]])
        elif get_type == "2": # dekripsi
            for sub_arr in arr_coor: # [[_, _], [_, _]]
                if sub_arr[0][0] != sub_arr[1][0] and sub_arr[0][1] != sub_arr[1][1]:
                    arr.append([[sub_arr[0][0], sub_arr[1][1]], [sub_arr[1][0], sub_arr[0][1]]])
                elif sub_arr[0][0] == sub_arr[1][0]:
                    arr.append([[sub_arr[0][0], sub_arr[0][1] - 1], [sub_arr[1][0], sub_arr[1][1] - 1]])
                elif sub_arr[0][1] == sub_arr[1][1]:
                    arr.append([[sub_arr[0][0] - 1, sub_arr[0][1]], [sub_arr[1][0] - 1, sub_arr[1][1]]])

        return arr

    def conv_use_matrix(self, a_k, a_c, get_type):
        arr_key = a_k
        arr_coor = a_c
        arr = []
        if get_type == "1":
            for i in arr_coor: # [[_, _], [_, _]]
                for ii in i: # [_, _]
                    if ii[0] >= 5 and ii[1] < 5:
                        arr.append(arr_key[0][ii[1]])
                    elif ii[1] >= 5 and ii[0] < 5:
                        arr.append(arr_key[ii[0]][0])
                    elif ii[0] >= 5 and ii[1] >= 5:
                        arr.append(arr_key[0][0])
                    else:
                        arr.append(arr_key[ii[0]][ii[1]])
        elif get_type == "2":
            for i in arr_coor: # [[_, _], [_, _]]
                for ii in i: # [_, _]
                    if ii[0] < 0 and ii[1] >= 0:
                        arr.append(arr_key[4][ii[1]])
                    elif ii[1] < 0 and ii[0] >= 0:
                        arr.append(arr_key[ii[0]][4])
                    elif ii[0] < 0 and ii[1] < 0:
                        arr.append(arr_key[4][4])
                    else:
                        arr.append(arr_key[ii[0]][ii[1]])

        return arr


    def make_key(self):
        print(Color.YELLOW + '-- Input Key --' + Color.RESET)
        key = input('Key: ')

        # SET DEFAULT: ubah semua char menjadi uppercase
        key = key.upper()

        # == ALGORITMA KEY PADA PLAYFAIR ==

        # HILANGKAN CHAR J dan space
        key = key.replace('J', '')
        key = key.replace(' ', '')

        # HILANGKAN DUPLIKASI HURUF
        res_chr = ""
        for char in key:
            if char not in res_chr:
                res_chr = res_chr + char
        key = res_chr

        # MENAMBAHKAN HURUF ALFABET YANG BELUM ADA
        huruf_A_Z = set(string.ascii_uppercase)
        huruf_A_Z = sorted(huruf_A_Z)

        # MENGHILANGKAN HURUF J
        huruf_A_Z.remove('J')

        for char in huruf_A_Z:
            if char not in key:
                key += char

        
        # MEMBUAT MATRIX 5x5 [[], [], [], [], []]
        arr_matrix = [[0 for _ in range(5)] for _ in range(5)]
        i = 0
        for row in range(len(arr_matrix)): # [[],[],[],[],[]]
            for col in range(len(arr_matrix[row])): # [_, _, _, _, _]
                arr_matrix[row][col] = key[i]
                i += 1
        
        return arr_matrix
    
    def make_plain_cipher(self, get_type):
        if get_type == "1":
            print(Color.CYAN + '-- Input Plaintext --' + Color.RESET)
            text = input('Plaintext: ')
        elif get_type == "2":
            print(Color.CYAN + '-- Input Ciphertext --' + Color.RESET)
            text = input('Ciphertext: ')

        # SET DEFAULT: ubah semua char menjadi uppercase
        text = text.upper()

        # UBAH HURUF J JADI I
        text = text.replace("J", "I")
        # HILANGKAN SPACE
        text = text.replace(" ", "")

        # JIKA ADA HURUF DUPLICATE, SISIPKAN Z
        arr_plain = list(text) # KONVERSI STR KE LIST/ARRAY
        for p in range(len(arr_plain)-1):
            if arr_plain[p] == arr_plain[p+1]:
                arr_plain = arr_plain[:p + 1] + ['Z'] + arr_plain[p + 1:]

        # BENTUK BIGRAM 2 2
        arr_bigram = [list(arr_plain[i:i+2]) for i in range(0, len(arr_plain), 2)]

        # JIKA ADA BIGRAM YANG GANJIL, TAMBAHKAN Z
        if len(arr_bigram[-1]) == 1:
            arr_bigram[-1].append('Z')

        return arr_bigram

    def encryption(self): # self untuk memanggil fungsi lain yg sesama class
        key = self.make_key()
        print(key)
        plain = self.make_plain_cipher("1")
        print(plain)
        
        # GET COORDINATES
        get_coor = self.get_coordinate(key, plain) # untuk mendapatkan coordinate plain dari array key
        map = self.mapping(get_coor, "1")
        conv = self.conv_use_matrix(key, map, "1")
        print(f'Ciphertext: {conv}')

    def decryption(self):
        key = self.make_key()
        print(key)
        cipher = self.make_plain_cipher("2")
        print(cipher)

        # GET COORDINATES
        get_coor = self.get_coordinate(key, cipher) # untuk mendapatkan coordinate plain dari array key
        map = self.mapping(get_coor, "2")
        conv = self.conv_use_matrix(key, map, "2")
        print(f'Plaintext: {conv}')
