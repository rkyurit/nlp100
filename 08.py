def cipher(s):
    return ''.join([chr(219-ord(c)) if 97 <= ord(c) and ord(c) <= 122 else c for c in list(s)])

if __name__ == "__main__":
    print(cipher('aaAa'))