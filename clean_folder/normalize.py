SYMBOLS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "h", "d", "e", "yo", "zh", "z", "y", "j", "k", "l", "m",
                "n", "o", "p", "r", "s", "t", "u",
               "f", "kh", "ts", "ch", "sh", "shch", "", "y", "", "e", "yu", "ia", "ie",
               "i", "yi", "g")

TRANS = {}
for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(name: str, suffix: str) -> str:
    new_name = ""
    t_name = name.translate(TRANS)
    t_name_list = []
    for char in range(len(t_name)):
        if t_name[char] not in SYMBOLS:
            t_name_list.append("_")
        else:
            t_name_list.append(t_name[char])
    t_name_join = "".join(t_name_list)
    if suffix:
        new_name = t_name_join + "." + suffix
    else:
        new_name = t_name_join
    return new_name