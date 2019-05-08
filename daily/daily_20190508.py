raw_str = "bedbathandbeyond"

dic = ["bed", "bath", "bedbath", "and", "beyond"]

def check_word_fit(s_in, words, s_out):
    for w in words:
        if s_in.startswith(w):
            s_out += w + "_"
            check_word_fit(s_in[len(w):], words.remove(w), s_out)
    return s_out

print(check_word_fit(raw_str, dic, ""))
