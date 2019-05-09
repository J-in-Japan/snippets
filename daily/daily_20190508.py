raw_str = "bedbathandbeyond"

dic = ["bed", "bath", "bedbath", "and", "beyond"]

def check_word_fit(s_in, words, s_out):
    if len(s_in) == 0:
        print(s_out)
        s_out = ""
    for w in words:
        if s_in.startswith(w):
            s_out += w + "_"
            xwords = words.copy()
            xwords.remove(w)
            check_word_fit(s_in[len(w):], xwords, s_out)
    return s_out

check_word_fit(raw_str, dic, "")
