
def Encrypt(text):
    substitute = {
        'a' : '!',
        'b' : '}',
        'c' : '{',
        'd' : '_',
        'e' : 'z',
        'f' : 'y',
        'g' : 'x',
        'h' : 'w',
        'i' : 'v',
        'j' : 'u',
        'k' : 't',
        'l' : 's',
        'm' : 'r',
        'n' : 'q',
        'o' : 'p',
        'p' : 'o',
        'q' : 'n',
        'r' : 'm',
        's' : 'l',
        't' : 'k',
        'u' : 'j',
        'v' : 'i',
        'w' : 'h',
        'x' : 'g',
        'y' : 'f',
        'z' : 'd',
        '{' : 'd',
        '}' : 'c',
        '!' : 'b',
        '_' : 'a'
    }
    res = ''
    for char in text:
        res += substitute[char]
    return res


with open('flag.txt', 'r') as f:
    flag = f.readline()
    output = Encrypt(flag)
    print(output)
