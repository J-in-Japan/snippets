# implement run-pass string encoding and decoding
# AAABCC = A3B1C2

def run_length_encode(s: str):
    enc_str = ''
    current_char = ''
    current_char_count = 0
    for i in range(len(s)):
        if i == 0:
            current_char = s[i]
            current_char_count = 1
        else:
            if s[i] == current_char:
                current_char_count += 1
            else:
                enc_str += current_char + str(current_char_count)
                current_char = s[i]
                current_char_count = 1
        if i == len(s)-1:
            enc_str += current_char + str(current_char_count)
    return enc_str

def run_length_decode(s: str):
    dec_str = ''
    i = 0
    while i < len(s):
        for j in range(int(s[i+1])):
           dec_str += s[i]
        i += 2
    return dec_str

print(run_length_encode('AA'))
print(run_length_encode('AABBBCDDDD'))
print(run_length_decode('A2'))
print(run_length_decode('A2B3C1D4'))