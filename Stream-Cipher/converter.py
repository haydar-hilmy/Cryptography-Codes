class Converter:

    def key_same_plain(arr_key, len_plain):
        arr = ''
        for i in range(len_plain):
            arr += arr_key[(i % len(arr_key))]
        return arr

    def conv_char_to_biner(arr_karakter):
        arr = []
        for karakter in arr_karakter:
            biner = bin(ord(karakter))[2:] # [2:] untuk menghilangkan 0b
            biner = biner.zfill(8) # konversi menjadi 8 bit
            arr.append(biner)
        return arr

    def conv_hex_to_char(arr_hex):
        arr = ''
        for hx in arr_hex:
            decimal_value = int(hx, 16) # heksadesimal ke nilai desimal
            arr += chr(decimal_value) # konversi desimal ke karakter
        return arr

    def conv_hex_to_biner(arr_hex): # arr_hex berupa string
        arr = []
        arr_hex = arr_hex.replace(" ", "") # hilangkan spasi
        for hx in arr_hex:
            biner = int(hx, 16) # konversi hex ke desimal
            biner = bin(biner)[2:] # konversi desimal ke biner
            biner = biner.zfill(4)
            arr.append(biner) 
        return arr

    def conv_biner_to_char(arr_biner):
        arr = ''
        for bi in arr_biner:
            decimal_val = int(bi, 2) #konversi biner ke desimal
            arr += chr(decimal_val) # konversi desimal ke karakter
        return arr

    def conv_biner_to_hex(arr_biner):
        arr = ''
        for bi in arr_biner:
            decimal_value = int(bi, 2) # konversi biner ke desimal
            arr += hex(decimal_value)[2:] # konversi desimal ke heksadesimal
        return arr

    def conv_biner_to_8bit(arr_bit):
        if len(arr_bit) % 2 != 0:
            arr_bit.append(arr_bit[-1])
        arr = [arr_bit[i] + arr_bit[i + 1] for i in range(0, len(arr_bit), 2)]
        return arr
    
    def to_8bit_biner(arr_biner):
        arr = []
        for i in range(0, len(arr_biner), 8):
            # Menambahkan nol di belakang jika panjangnya kurang dari 8 bit
            bin_str = arr_biner[i:i+8].ljust(8, '0')
            arr.append(bin_str)
        return arr

    def xor_binary_array(bin_plain, bin_key):
        result = []
        for b1, b2 in zip(bin_plain, bin_key):
            xor_result = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(b1, b2))
            result.append(xor_result)
        return result