import numpy as np

def padded_hex8(i):
    given_int = i
    given_len = 8

    hex_result = hex(given_int)[2:] # remove '0x' from beginning of str
    num_hex_chars = len(hex_result)
    extra_zeros = '0' * (given_len - num_hex_chars) # may not get used..

    return (hex_result if num_hex_chars == given_len else
            extra_zeros + hex_result)

def xor2to8(hex_1, hex_2):
    ans = padded_hex8(int(hex_1, 16) ^ int(hex_2, 16))
    return ans

def padded_hex(i):
    given_int = i
    given_len = 2

    hex_result = hex(given_int)[2:] # remove '0x' from beginning of str
    num_hex_chars = len(hex_result)
    extra_zeros = '0' * (given_len - num_hex_chars) # may not get used..

    return (hex_result if num_hex_chars == given_len else
            extra_zeros + hex_result )

#function to XOR(2 hexadecimal numbers)
def xor2(hex_1,hex_2):
    ans = padded_hex(int(hex_1, 16) ^ int(hex_2, 16))
    return ans

#function to shift the word by 2 to the left or, simply said, the function to find rotword
def rotword(word):
    res = word[2:] + word[:2]
    return res

#function to XOR(4 hexadecimal numbers)
def xor(hex_1,hex_2,hex_3,hex_4):
    ans = padded_hex(int(hex_1, 16) ^ int(hex_2, 16) ^ int(hex_3, 16) ^ int(hex_4, 16))
    return ans


#https://www.infosecwriters.com/text_resources/pdf/AESbyExample.pdf
# E table
def e(h2): #input should not have '0x'

    E = (
    [0x01, 0x03, 0x05, 0x0F, 0x11, 0x33, 0x55, 0xFF, 0x1A, 0x2E, 0x72, 0x96, 0xA1, 0xF8, 0x13, 0x35],
    [0x5F, 0xE1, 0x38, 0x48, 0xD8, 0x73, 0x95, 0xA4, 0xF7, 0x02, 0x06, 0x0A, 0x1E, 0x22, 0x66, 0xAA],
    [0xE5, 0x34, 0x5C, 0xE4, 0x37, 0x59, 0xEB, 0x26, 0x6A, 0xBE, 0xD9, 0x70, 0x90, 0xAB, 0xE6, 0x31],
    [0x53, 0xF5, 0x04, 0x0C, 0x14, 0x3C, 0x44, 0xCC, 0x4F, 0xD1, 0x68, 0xB8, 0xD3, 0x6E, 0xB2, 0xCD],
    [0x4C, 0xD4, 0x67, 0xA9, 0xE0, 0x3B, 0x4D, 0xD7, 0x62, 0xA6, 0xF1, 0x08, 0x18, 0x28, 0x78, 0x88],
    [0x83, 0x9E, 0xB9, 0xD0, 0x6B, 0xBD, 0xDC, 0x7F, 0x81, 0x98, 0xB3, 0xCE, 0x49, 0xDB, 0x76, 0x9A],
    [0xB5, 0xC4, 0x57, 0xF9, 0x10, 0x30, 0x50, 0xF0, 0x0B, 0x1D, 0x27, 0x69, 0xBB, 0xD6, 0x61, 0xA3],
    [0xFE, 0x19, 0x2B, 0x7D, 0x87, 0x92, 0xAD, 0xEC, 0x2F, 0x71, 0x93, 0xAE, 0xE9, 0x20, 0x60, 0xA0],
    [0xFB, 0x16, 0x3A, 0x4E, 0xD2, 0x6D, 0xB7, 0xC2, 0x5D, 0xE7, 0x32, 0x56, 0xFA, 0x15, 0x3F, 0x41],
    [0xC3, 0x5E, 0xE2, 0x3D, 0x47, 0xC9, 0x40, 0xC0, 0x5B, 0xED, 0x2C, 0x74, 0x9C, 0xBF, 0xDA, 0x75],
    [0x9F, 0xBA, 0xD5, 0x64, 0xAC, 0xEF, 0x2A, 0x7E, 0x82, 0x9D, 0xBC, 0xDF, 0x7A, 0x8E, 0x89, 0x80],
    [0x9B, 0xB6, 0xC1, 0x58, 0xE8, 0x23, 0x65, 0xAF, 0xEA, 0x25, 0x6F, 0xB1, 0xC8, 0x43, 0xC5, 0x54],
    [0xFC, 0x1F, 0x21, 0x63, 0xA5, 0xF4, 0x07, 0x09, 0x1B, 0x2D, 0x77, 0x99, 0xB0, 0xCB, 0x46, 0xCA],
    [0x45, 0xCF, 0x4A, 0xDE, 0x79, 0x8B, 0x86, 0x91, 0xA8, 0xE3, 0x3E, 0x42, 0xC6, 0x51, 0xF3, 0x0E],
    [0x12, 0x36, 0x5A, 0xEE, 0x29, 0x7B, 0x8D, 0x8C, 0x8F, 0x8A, 0x85, 0x94, 0xA7, 0xF2, 0x0D, 0x17],
    [0x39, 0x4B, 0xDD, 0x7C, 0x84, 0x97, 0xA2, 0xFD, 0x1C, 0x24, 0x6C, 0xB4, 0xC7, 0x52, 0xF6, 0x01]
    )

    # splitting the word in two parts (eg.- '0f' becomes ['0', 'f'])
    d = []
    for i in range(0, 2):
        z = (h2[i:i + 1])
        d.append(z)

    # using every two letters as index to find the corresponding word in L table (eg.- '0'(row),'f'(column) is one point in L table)
    j = []
    m = hex(E[int(d[0], 16)][int(d[1], 16)])

    return m[2:]

#L table
def l(h1): #input should not have '0x'
    L = (
     ['', 0x00, 0x19, 0x01, 0x32, 0x02, 0x1A, 0xC6, 0x4B, 0xC7, 0x1B, 0x68, 0x33, 0xEE, 0xDF, 0x03],
     [0x64, 0x04, 0xE0, 0x0E, 0x34, 0x8D, 0x81, 0xEF, 0x4C, 0x71, 0x08, 0xC8, 0xF8, 0x69, 0x1C, 0xC1],
     [0x7D, 0xC2, 0x1D, 0xB5, 0xF9, 0xB9, 0x27, 0x6A, 0x4D, 0xE4, 0xA6, 0x72, 0x9A, 0xC9, 0x09, 0x78],
     [0x65, 0x2F, 0x8A, 0x05, 0x21, 0x0F, 0xE1, 0x24, 0x12, 0xF0, 0x82, 0x45, 0x35, 0x93, 0xDA, 0x8E],
     [0x96, 0x8F, 0xDB, 0xBD, 0x36, 0xD0, 0xCE, 0x94, 0x13, 0x5C, 0xD2, 0xF1, 0x40, 0x46, 0x83, 0x38],
     [0x66, 0xDD, 0xFD, 0x30, 0xBF, 0x06, 0x8B, 0x62, 0xB3, 0x25, 0xE2, 0x98, 0x22, 0x88, 0x91, 0x10],
     [0x7E, 0x6E, 0x48, 0xC3, 0xA3, 0xB6, 0x1E, 0x42, 0x3A, 0x6B, 0x28, 0x54, 0xFA, 0x85, 0x3D, 0xBA],
     [0x2B, 0x79, 0x0A, 0x15, 0x9B, 0x9F, 0x5E, 0xCA, 0x4E, 0xD4, 0xAC, 0xE5, 0xF3, 0x73, 0xA7, 0x57],
     [0xAF, 0x58, 0xA8, 0x50, 0xF4, 0xEA, 0xD6, 0x74, 0x4F, 0xAE, 0xE9, 0xD5, 0xE7, 0xE6, 0xAD, 0xE8],
     [0x2C, 0xD7, 0x75, 0x7A, 0xEB, 0x16, 0x0B, 0xF5, 0x59, 0xCB, 0x5F, 0xB0, 0x9C, 0xA9, 0x51, 0xA0],
     [0x7F, 0x0C, 0xF6, 0x6F, 0x17, 0xC4, 0x49, 0xEC, 0xD8, 0x43, 0x1F, 0x2D, 0xA4, 0x76, 0x7B, 0xB7],
     [0xCC, 0xBB, 0x3E, 0x5A, 0xFB, 0x60, 0xB1, 0x86, 0x3B, 0x52, 0xA1, 0x6C, 0xAA, 0x55, 0x29, 0x9D],
     [0x97, 0xB2, 0x87, 0x90, 0x61, 0xBE, 0xDC, 0xFC, 0xBC, 0x95, 0xCF, 0xCD, 0x37, 0x3F, 0x5B, 0xD1],
     [0x53, 0x39, 0x84, 0x3C, 0x41, 0xA2, 0x6D, 0x47, 0x14, 0x2A, 0x9E, 0x5D, 0x56, 0xF2, 0xD3, 0xAB],
     [0x44, 0x11, 0x92, 0xD9, 0x23, 0x20, 0x2E, 0x89, 0xB4, 0x7C, 0xB8, 0x26, 0x77, 0x99, 0xE3, 0xA5],
     [0x67, 0x4A, 0xED, 0xDE, 0xC5, 0x31, 0xFE, 0x18, 0x0D, 0x63, 0x8C, 0x80, 0xC0, 0xF7, 0x70, 0x07]
    )
    # splitting the word in two parts (eg.- '0f' becomes ['0', 'f'])
    d = []
    for i in range(0, 2):
        z = (h1[i:i + 1])
        d.append(z)

    # using every two letters as index to find the corresponding word in L table (eg.- '0'(row),'f'(column) is one point in L table)
    j = []
    m = hex(L[int(d[0], 16)][int(d[1], 16)])

    return m[2:]

def e_l_table_calc(a,b):
    if a == '00':
        u = padded_hex(int('00', 16))
    else:
        a = padded_hex(int(l(a), 16) + int(l('02'), 16))
        u = e(a)
        if int(a, 16) > int('FF', 16):  # if the value of y is greater than 'ff', then 'ff' has to be subtracted from y
            a = padded_hex(int(a, 16) - int('FF', 16))
            u = e(a)
    if b == '00':
        z = padded_hex(int('00', 16))
    else:
        b = padded_hex(int(l(b), 16) + int(l('03'), 16))
        z = e(b)
        if int(b, 16) > int('FF', 16):  # if the value of y is greater than 'ff', then 'ff' has to be subtracted from y
            b = padded_hex(int(b, 16) - int('FF', 16))
            b = padded_hex(int(l(b), 16) + int(l('03'), 16))
            z = e(b)

    return u,z

#function to find subword
def sbox(word):

    s_box = (
        [0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76],
        [0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0],
        [0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15],
        [0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75],
        [0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84],
        [0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF],
        [0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8],
        [0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2],
        [0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73],
        [0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB],
        [0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79],
        [0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08],
        [0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A],
        [0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E],
        [0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF],
        [0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16]
    )

    #splitting the word in eight parts (eg.- '0f569892' becomes ['0', 'f', '5', '6', '9', '8', '9', '2'])
    d = []
    for i in range(0, 8):
        z = (word[i:i + 1])
        d.append(z)

    #using every two letters as index to find the corresponding word in s_box (eg.- '0'(row),'f'(column) is one point in s_box)
    j = []
    for i in range(0, len(d), 2):
        m = hex(s_box[int(d[i], 16)][int(d[i + 1], 16)])
        if len(m) < 4:
            m = m[0] + m[1] + '0' + m[2] #for conditions such as 0x8, it converts it to 0x08 (keeps the length of 4)
        j.append(m)
    #o/p: j is ['0x76', '0xb1', '0x46', '0x4f'] --> values from s_box

    return j

def r_con(word, round_number):
    # r-constants for 10 rounds
    r_con = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']
    #Actual round number is (round_number + 1) as we started with 0
    # XORing r-constant of the round with first element of fourth word
    word = hex(int(word, 16) ^ int(r_con[round_number], 16))
    return word

#Function to shift rows
def shift_row(matrix):

    #shift second row left by 1
    t = 0
    t = matrix[1][0]
    matrix[1][0] = matrix[1][1]
    matrix[1][1] = matrix[1][2]
    matrix[1][2] = matrix[1][3]
    matrix[1][3] = t

    # shift third row left by 2
    t1 = 0
    t2 = 0
    t1 = matrix[2][0]
    matrix[2][0] = matrix[2][2]
    matrix[2][2] = t1
    t2 = matrix[2][1]
    matrix[2][1] = matrix[2][3]
    matrix[2][3] = t2

    # shift fourth row left by 3
    t4 = 0
    t4 = matrix[3][3]
    matrix[3][3] = matrix[3][2]
    matrix[3][2] = matrix[3][1]
    matrix[3][1] = matrix[3][0]
    matrix[3][0] = t4

    return matrix

#Function to find the mix-column matrix
def mix_column(array):

    m = array

    #the below statements are used to find all the 16 elements of 4X4 mic_column matrix(b00,b01,b02,...)
    u,z = e_l_table_calc(m[0],m[1])
    b00 = xor(u , z, m[2] , m[3]) #value of b00 calculated using 'xor', 'e' and 'l' function

    u,z = e_l_table_calc(m[1],m[2])
    b10 = xor(m[0] , u , z , m[3])

    u,z = e_l_table_calc(m[2],m[3])
    b20 = xor(m[0] , m[1] , u , z)

    u,z = e_l_table_calc(m[3],m[0])
    b30 = xor(z , m[1] , m[2] , u)

    u,z = e_l_table_calc(m[4],m[5])
    b01 = xor(u , z , m[6] , m[7])

    u,z = e_l_table_calc(m[5],m[6])
    b11 = xor(m[4] , u , z , m[7])

    u,z = e_l_table_calc(m[6],m[7])
    b21 = xor(m[4] , m[5] , u , z)

    u,z = e_l_table_calc(m[7],m[4])
    b31 = xor(z , m[5] , m[6] , u)

    u,z = e_l_table_calc(m[8],m[9])
    b02 = xor(u , z , m[10] , m[11])

    u,z = e_l_table_calc(m[9],m[10])
    b12 = xor(m[8] , u , z , m[11])

    u,z = e_l_table_calc(m[10],m[11])
    b22 = xor(m[8] , m[9] , u , z)

    u,z = e_l_table_calc(m[11],m[8])
    b32 = xor(z , m[9] , m[10] , u)

    u,z = e_l_table_calc(m[12],m[13])
    b03 = xor(u , z , m[14] , m[15])

    u,z = e_l_table_calc(m[13],m[14])
    b13 = xor(m[12] , u , z , m[15])

    u,z = e_l_table_calc(m[14],m[15])
    b23 = xor(m[12] , m[13] , u , z)

    u,z = e_l_table_calc(m[15],m[12])
    b33 = xor(z , m[13] , m[14] , u)

    matrix = np.array([ [b00,b01,b02,b03] , [b10,b11,b12,b13] , [b20,b21,b22,b23] , [b30,b31,b32,b33] ])
    return matrix

print("-------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------")
print("Plaintext:")
print("00 00 00 00 00 00 00 00 00 00 00 00 00 00 ab e8")
print("Key:")
print("1a 0c 24 f2 87 54 95 bc b7 08 0e 43 92 0f 56 98\n")
print("-------------------------------------------------------------------------------------------------")
print('Encrypted round keys:')
print("-------------------------------------------------------------------------------------------------")


# Taking the original key and separating every two letters
key_0 = "1a0c24f2875495bcb7080e43920f5698" #our key to be used

b = []
for i in range(0,32,2):
    x = (key_0[i:i+2])
    b.append(x)
print('round 0 key:')
print(b)
# o/p: b is  ['1a', '0c', '24', 'f2', '87', '54', '95', 'bc', 'b7', '08', '0e', '43', '92', '0f', '56', '98']

# Making a matrix of 4X4 (just to show)
M = np.array([ [b[0],b[4],b[8],b[12]], [b[1],b[5],b[9],b[13]], [b[2],b[6],b[10],b[14]], [b[3],b[7],b[11],b[15]] ])
#o/p: M is  [['1a' '87' 'b7' '92']
#            ['0c' '54' '08' '0f']
#            ['24' '95' '0e' '56']
#            ['f2' 'bc' '43' '98']]
count = 0
key_str = []
for n in range(10): #for 10 rounds
    key_str.append(key_0)  #key_0 = "1a0c24f2875495bcb7080e43920f5698" --> original key
    count += 1
    if count > 1:
        key_str.pop() #to remove the key_0 from key_str which gets appended in every loop

    #Forming words from key_0 --> w = [w1,w2,w3,w4] or [ w[0],w[1],w[2],w[3] ]
    w = []
    for i in range(0,32,8):
        y= (key_str[n][i:i+8])
        w.append(y)
    # o/p: w is ['1a0c24f2', '875495bc', 'b7080e43', '920f5698']

    Z = w[3] #will be later used to be find the w1_new

    w[3] = rotword(w[3]) #shift word 4 or w[3] to left by 2
    # o/p: 920f5698 becomes 0f569892
    w[3] = sbox(w[3]) #passing the word through SBox
    # o/p: ['0x76', '0xb1', '0x46', '0x4f']
    w[3][0] = r_con(w[3][0],n)
    #o/p: w[3][0] is 0x77


    #Dividing the first three words (w1,w2,w3) into pairs of 2 & then joining the fourth word (w4) with them
    w_new = []
    for i in range(0,3):
        for j in range(0,8,2):
           w_new.append(w[i][j] + w[i][j+1])
    for i in range(0,4):
        w_new.append(w[3][i][2:]) #[2:] is used to remove '0x' from w[3]
    #o/p: w_new is ['1a', '0c', '24', 'f2', '87', '54', '95', 'bc', 'b7', '08', '0e', '43', '77', 'b1', '46', '4f']

    # Matrix format (just to show)
    w = np.array([ [w_new[0],w_new[4],w_new[8],w_new[12]] , [w_new[1],w_new[5],w_new[9],w_new[13]] , [w_new[2],w_new[6],w_new[10],w_new[14]] , [w_new[3],w_new[7],w_new[11],w_new[15]] ])
    # o/p: w is [['1a' '87' 'b7' '77']
    #            ['0c' '54' '08' 'b1']
    #            ['24' '95' '0e' '46']
    #            ['f2' 'bc' '43' '4f']]

    w_str = ''.join(w_new)
    #o/p: w_str is 1a0c24f2875495bcb7080e4377b1464f

    w = []
    for i in range(0,32,8):
        y= (w_str[i:i+8])
        w.append(y)
    # o/p: w is ['1a0c24f2', '875495bc', 'b7080e43', '77b1464f'] = [w1,w2,w3,w4]

    w1_new = xor2to8(w[0],w[3])
    w2_new = xor2to8(w[1],w1_new)
    w3_new = xor2to8(w[2],w2_new)
    w4_new = xor2to8(Z,w3_new)

    w = [w1_new + w2_new + w3_new + w4_new]
    #o/p: w is ['6dbd62bdeae9f7015de1f942cfeeafda']

    b = []
    for i in range(0, 32, 2):
        x = (w[0][i:i + 2]) #[0] is used because w is a list with one item (w = ['6dbd62bdeae9f7015de1f942cfeeafda'])
        b.append(x)
    print("round ", n + 1 ," key:") #as 'n' starts with 0
    print(b)
    #o/p: b is ['6d', 'bd', '62', 'bd', 'ea', 'e9', 'f7', '01', '5d', 'e1', 'f9', '42', 'cf', 'ee', 'af', 'da'] --> this is the round (n+1) key to be diplayed

    w = w[0] #w is in list format with one element --> this converts it into a string and assigns it to 'w'

    key_str.append(w)

#key_str (after completing all the rounds) is ['1a0c24f2875495bcb7080e43920f5698', '6dbd62bdeae9f7015de1f942cfeeafda', '47c43537ad2dc236f0cc3b743f2294ae', 'd0e6d1427dcb13748d072800b225bcae', 'e78335759a482601174f0e01a56ab2af', 'f5b44c736ffc6a7278b36473ddd9d6dc', 'e042cab28fbea0c0f70dc4b32ad4126f', 'e88b62576735c29790380624baec144b', 'a671d1a3c1441334517c1510eb90015b', 'dd0de84a1c49fb7e4d35ee6ea6a5ef35', 'edd27e6ef19b8510bcae6b7e1a0b844b']
# the above key_str represents all the round keys from 0 to 10

print("-------------------------------------------------------------------------------------------------")
print("Encrypted data rounds:")
print("-------------------------------------------------------------------------------------------------")

input = "0000000000000000000000000000abe8" #our plaintext to be encrypted

# Dividing the key into two equal parts of two
b = []
for i in range(0,32,2):
    x = (input[i:i+2])
    b.append(x)
print("Input:")
print(b)
#o/p: b is ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', 'ab', 'e8']

#Making the above plaintext into a 4X4 matrix
b = np.array([ [b[0],b[4],b[8],b[12]], [b[1],b[5],b[9],b[13]], [b[2],b[6],b[10],b[14]], [b[3],b[7],b[11],b[15]] ])
#o/p: b is [['00' '00' '00' '00']
#           ['00' '00' '00' '00']
#           ['00' '00' '00' 'ab']
#           ['00' '00' '00' 'e8']]

#Adding initial round key 0 to the plaintext
d = []
for i in range(0,32,2):
    x = (key_str[0][i:i+2])
    d.append(x)
#o/p: d is ['1a', '0c', '24', 'f2', '87', '54', '95', 'bc', 'b7', '08', '0e', '43', '92', '0f', '56', '98']

# Making a matrix of 4X4 size
d = np.array([ [d[0],d[4],d[8],d[12]], [d[1],d[5],d[9],d[13]], [d[2],d[6],d[10],d[14]], [d[3],d[7],d[11],d[15]] ])
#o/p: d is [['1a' '87' 'b7' '92']
#           ['0c' '54' '08' '0f']
#           ['24' '95' '0e' '56']
#           ['f2' 'bc' '43' '98']]

c = [['','','',''],['','','',''],['','','',''],['','','','']]
for i in range(4):
    for j in range(4):
        c[i][j] = xor2(d[i][j],b[i][j])
b = c
#o/p: b is [['1a', '87', 'b7', '92'], ['0c', '54', '08', '0f'], ['24', '95', '0e', 'fd'], ['f2', 'bc', '43', '70']]

input_new = b[0][0] + b[1][0] + b[2][0] + b[3][0] + b[0][1] + b[1][1] + b[2][1] + b[3][1] + b[0][2] + b[1][2] + b[2][2] + b[3][2] + b[0][3] + b[1][3] + b[2][3] + b[3][3]
#o/p: input_new is 1a0c24f2875495bcb7080e43920ffd70

b = []
for i in range(0,32,2):
    x = (input_new[i:i+2])
    b.append(x)
print("Round 0:")
print(b)
#o/p: b is ['1a', '0c', '24', 'f2', '87', '54', '95', 'bc', 'b7', '08', '0e', '43', '92', '0f', 'fd', '70']

count = 0
for k in range(10): #for 10 rounds

    # Forming words from input --> w = [w1,w2,w3,w4] or [ w[0],w[1],w[2],w[3] ]
    w = []
    for i in range(0, 32, 8):
        y = input_new[i:i + 8]
        w.append(y)
    #o/p: w is ['1a0c24f2', '875495bc', 'b7080e43', '920ffd70']

    #Passing the words (w1,w2,w3,w4) through S-Box
    w[0] = sbox(w[0])
    #o/p: w[0] is ['0xa2', '0xfe', '0x36', '0x89']
    w[1] = sbox(w[1])
    #o/p: w[1] is ['0x17', '0x20', '0x2a', '0x65']
    w[2] = sbox(w[2])
    #o/p: w[2] is ['0xa9', '0x30', '0xab', '0x1a']
    w[3] = sbox(w[3])
    #o/p: w[3] is ['0x4f', '0x76', '0x54', '0x51']

    w = [ [w[0][0],w[1][0],w[2][0],w[3][0]] , [w[0][1],w[1][1],w[2][1],w[3][1]] , [w[0][2],w[1][2],w[2][2],w[3][2]] , [w[0][3],w[1][3],w[2][3],w[3][3]] ]
    #o/p: w is [['0xa2', '0x17', '0xa9', '0x4f'], ['0xfe', '0x20', '0x30', '0x76'], ['0x36', '0x2a', '0xab', '0x54'], ['0x89', '0x65', '0x1a', '0x51']]


    #Passing the matrix (w) through shift row block (function)
    w = shift_row(w)
    #o/p: w is [['0xa2', '0x17', '0xa9', '0x4f'], ['0x20', '0x30', '0x76', '0xfe'], ['0xab', '0x54', '0x36', '0x2a'], ['0x51', '0x89', '0x65', '0x1a']]

    m = []
    for i in range(4):
        for j in range(4):
            m.append(padded_hex(int(w[j][i], 16)))
    #o/p: w = [['0xa2', '0x17', '0xa9', '0x4f'], ['0x20', '0x30', '0x76', '0xfe'], ['0xab', '0x54', '0x36', '0x2a'], ['0x51', '0x89', '0x65', '0x1a']]
    # m will make w to ['a2', '20', 'ab', '51', '17', '30', '54', '89', 'a9', '76', '36', '65', '4f', 'fe', '2a', '1a']
    w = m

    #Passing the array (w) through Mix Column block (function)
    count += 1
    if count < 10: #no mix column block for 10th round
        w = mix_column(w)
    #o/p: w is [['c5' 'a3' '80' 'b7']
    #           ['55' '02' '7a' 'cc']
    #           ['3c' '0f' '1c' 'cb']
    #           ['d4' '54' '6a' '31']]
    else:
        w = np.array([ [w[0],w[4],w[8],w[12]] , [w[1],w[5],w[9],w[13]] , [w[2],w[6],w[10],w[14]] , [w[3],w[7],w[11],w[15]] ])

    #Adding Round key
    b = []
    for i in range(0,32,2):
        x = (key_str[k + 1][i:i+2])
        b.append(x)
    #o/p: b is ['6d', 'bd', '62', 'bd', 'ea', 'e9', 'f7', '01', '5d', 'e1', 'f9', '42', 'cf', 'ee', 'af', 'da']

    # Making a matrix of 4X4 (just to show)
    M = np.array([ [b[0],b[4],b[8],b[12]], [b[1],b[5],b[9],b[13]], [b[2],b[6],b[10],b[14]], [b[3],b[7],b[11],b[15]] ])
    #o/p: M is [['6d' 'ea' '5d' 'cf']
    #           ['bd' 'e9' 'e1' 'ee']
    #           ['62' 'f7' 'f9' 'af']
    #           ['bd' '01' '42' 'da']]

    c=[['','','',''],['','','',''],['','','',''],['','','','']]
    for i in range(4):
        for j in range(4):
            c[i][j] = xor2(M[i][j],w[i][j])
    #o/p: c is [['a8', '49', 'dd', '78'], ['e8', 'eb', '9b', '22'], ['5e', 'f8', 'e5', '64'], ['69', '55', '28', 'eb']]

    encrypted_data = []
    for i in range(4):
        for j in range(4):
            encrypted_data.append(c[j][i])
    #o/p: encrypted_data is ['a8', 'e8', '5e', '69', '49', 'eb', 'f8', '55', 'dd', '9b', 'e5', '28', '78', '22', '64', 'eb'] --> encrypted data for k+1 round to be displayed

    print("Round ", k + 1 ,": ") #because k starts with 0
    print(encrypted_data)

    x = ""
    for i in range(len(encrypted_data)):
        x = x + encrypted_data[i]
     #o/p: x is a8e85e6949ebf855dd9be528782264eb

    input_new = x #to be used for the next round

print("-------------------------------------------------------------------------------------------------")
print("Final Output:")
print(encrypted_data)
print("-------------------------------------------------------------------------------------------------")
