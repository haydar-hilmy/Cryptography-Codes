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

    def conv_biner_to_hex(arr_biner): # ['0100'] -> 4(hex)
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
    
    def conv_8bit_to_4bit(arr_8bit): # arr_8bit -> ex:['00000000', '00000000']
        arr = []
        for i in range(len(arr_8bit)):
            bit_1 = arr_8bit[i][0:4]
            bit_2 = arr_8bit[i][4:8]
            arr.append(bit_1)
            arr.append(bit_2)
        return arr
    
    def to_8bit_biner(arr_biner): # arr_biner4bit '00000' -> ['00000000']
        arr = []
        new_arr_biner = arr_biner.replace(" ", "")
        for i in range(0, len(new_arr_biner), 8):
            # Menambahkan nol di belakang jika panjangnya kurang dari 8 bit
            bin_str = new_arr_biner[i:i+8].ljust(8, '0')
            arr.append(bin_str)
        return arr

    # def xor_binary_array(bin_plain, bin_key):
    #     result = []
    #     for b1, b2 in zip(bin_plain, bin_key):
    #         xor_result = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(b1, b2))
    #         result.append(xor_result)
    #     return result
    
    def xor_binary_array(bin_key, bin_plain):
        result = []
        iv = '0000'
        for b1, b2 in zip(bin_key, bin_plain): # ['0000', '0000'] -> '0000'
            xor_result = ''
            for bit_p, bit_k, bit_iv in zip(b2, b1, iv): # '0000' -> 0
                xor_iv = str(int(bit_p) ^ int(bit_iv)) # 0(p) XOR 0(iv)
                xor_key = str(int(xor_iv) ^ int(bit_k)) # 0(p.iv) XOR 0(k)
                xor_result += xor_key

            # wrapping
            xor_result_list = list(xor_result)
            for i in range(0, len(xor_result_list)-1, 1):
                temp = xor_result_list[i]
                xor_result_list[i] = xor_result_list[i+1]
                xor_result_list[i+1] = temp
            xor_result = ''.join(xor_result_list)

            result.append(xor_result)
            iv = xor_result
        return result
    
    def xor_binary_array_decrypt(b_k, b_iv, b_c): # ['0000', '0000']
        arr_result = []
        arr_cipher = b_c
        arr_iv = b_iv
        arr_key = b_k

        # REVERSE CIPHERTEXT
        arr_cipher = arr_cipher[::-1]

        # REVERSE KEY
        arr_key = arr_key[::-1]

        # UNWRAP CIPHERTEXT
        new_arr_cipher = []
        for a_c in arr_cipher: # ['0000', '0000'] -> a_c = '0000'
            arr_wrap = list(a_c) # '0000' -> ['0','0','0','0']
            for i in range(len(arr_wrap)-1, 0, -1):
                temp = arr_wrap[i]
                arr_wrap[i] = arr_wrap[i-1]
                arr_wrap[i-1] = temp
            new_arr_cipher.append(''.join(arr_wrap))


        # PROSES XOR -> C(i) XOR Key(i) XOR Iv(i)
        for a_c, a_k, a_iv in zip(new_arr_cipher, arr_key, arr_iv): # ['0000', '0000'] -> '0000'
            arr_xor = ''
            for c, k, iv in zip(a_c, a_k, a_iv): # '0000' -> '0'
                xor_iv = str(int(c) ^ int(iv)) # 0(c) XOR 0(iv)
                xor_key = str(int(xor_iv) ^ int(k)) # 0(c.iv) XOR 0(k)
                arr_xor += xor_key
            arr_result.append(arr_xor)
            
        arr_result = arr_result[::-1]
        return arr_result

    def get_iv_from_cipher(arr_cipher): # ex: ['1100', '1111', '0101', '1010'] -> return ['0101', '1111', '1100', '0000']
        arr = []
        iv = '0000'
        arr = arr_cipher
        arr = arr[:len(arr)-1] #slice
        arr = arr[::-1] # reverse ['1111', '0000', '1010'] -> ['1010', '0000', '1111']
        arr.append(iv) # menambahkan iv pertama '0000'
        return arr